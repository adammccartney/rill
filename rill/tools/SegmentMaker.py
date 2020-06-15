import abjad
import copy
import rill
from .RhythmDefinition import RhythmDefinition
from .ScoreTemplate import ScoreTemplate

class SegmentMaker(abjad.SegmentMaker):
    """
    Segment-maker.

    >>> import rill

    .. container:: example

        >>> maker = rill.SegmentMaker()
        >>> abjad.f(maker)
        rill.SegmentMaker(
                )

    """

    __documentation_section__ = None

    __slots__ = (
        "_lilypond_file",
        "_metadata",
        "_rhythm_definitions",
        "_score",
        "name",
        "time_signatures",
    )

    ## INITIALIZER ##

    def __init__(
            self,
            name=None,
            time_signatures=None,
        ):
            super(SegmentMaker, self).__init__()
            self._lilypond_file = None
            self._rhythm_definitions = []
            self._segment_directory = None
            self._score = None
            self.name=name
            self.time_signatures = time_signatures or []
  
    ### PRIVATE PROPERTIES ###

    @property
    def _music_voices(self):
        return(
                self._score["Violin_Music_Voice"],
                self._score["MonoSynth_Music_Voice"],
                self._score["RH_Voice_I"],
                self._score["RH_Voice_II"],
                self._score["LH_Voice_I"],
                self._score["LH_Voice_II"],
            )

    ### PRIVATE METHODS ###
    
    def _call_rhythm_definitions(self):
        for rhythm_definition in self._rhythm_definitions:
            rhythm_definition(self._score)

    def _configure_lilypond_file(self):
        for rhythm_definition in self._rhythm_definitions:
            rhythm_definition(self._score)

    def _configure_score(self):
        lilypond_file = self._lilypond_file
        lilypond_file.header_block.title = None
        lilypond_file.header_block.composer = None
    
    def _get_staves(self):
        return (
            self._score["Violin"], 
            self._score["MonoSynth"],
            self._score["PolySynth"],
        )

    def _handle_time_signatures(self):
        if not self.metronome_marks:
            return
        context = self._score["Global_Skips"]
        skips = []
        for item in self.time_signatures:
            skip = abjad.Skip(1, multiplier=item)
            time_signature = abjad.TimeSignature(item)
            abjad.attach(time_signature, skip, context="Score")
            skips.append(skip)
        context.extend(skips)
        context = self._score["Global_Rests"]
        rests = []
        for item in self.time_signatures:
            rest = abjad.MultimeasureRest(1, multiplier=item)
            rests.append(rest)
        context.extend(rests)

    def _make_lilypond_file(self, midi=False):
        path = "../../stylesheets/stylesheet.ily"
        lilypond_file = abjad.LilyPondFile.new(
                music=self._score, includes=[path], use_relative_includes=True
                )
        delattr(lilypond_file.header_block, "tagline")
        for item in lilypond_file.items[:]:
            if getattr(item, "name", None) in ("layout", "paper"):
                lilypond_file.items.remove(item)
        self._lilypond_file = lilypond_file

    def _make_score(self):
        template = ScoreTemplate()
        score = template()
        self._score = score

    ### PUBLIC PROPERTIES ###

    @property
    def metadata(self):
        """
        Gets metadata after run.
        """
        return self._metadata

    ### PUBLIC METHODS ###

    def define_rhythm(self):
        """
        Makes rhythm definition.
        Returns rhythm definition. 
        """
        rhythm_definition = RhythmDefinition()
        self._rhythm_definitions.append(rhythm_definition)
        return rhythm_definition

    def run(
            self,
            metadata=None,
            persist=None,
            previous_metadata=None,
            previous_persist=None,
            segment_directory=None,
        ):
        """
        Runs segment-maker.
        
        Returns LilyPond file.
        """
        self._metadata = abjad.OrderedDict(metadata)
        self._persist = abjad.OrderedDict(persist)
        self._previous_metadata = abjad.OrderedDict(previous_metadata)
        self._previous_persist = abjad.OrderedDict(previous_persist)
        self._segment_directory = segment_directory
        self._make_score()
        self._make_lilypond_file()
        self._configure_lilypond_file()
        self._call_rhythm_definitions()
        self._configure_score()
        score_block = self._lilypond_file["score"]
        score = score_block["Score"]
        #        if not abjad.inspect(score).wellformed():
        #            string = abjad.inspect(score).tabulate_wellformedness()
        #            raise Exception(string)
        return self._lilypond_file



