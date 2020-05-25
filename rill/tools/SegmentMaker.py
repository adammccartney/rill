import abjad
import copy
from rill.tools.ScoreTemplate import ScoreTemplate


class SegmentMaker(abjad.SegmentMaker):
    """
    Segment-maker.

    >>> import rill

    .. container:: example

        >>> maker = rill.SegmentMaker()
        >>> abjad.f(maker)
        rill.SegmentMaker(
                metronome_marks=[],
                time_signatures=[],
                )

    """
    
    ### CLASS ATTRIBUTES ###

    __documentation_section__ = None

    __slots__ = (
            "_lilypond_file",
            "_metadata",
            "_score",
            "name",
<<<<<<< HEAD
            "time_signatures"
=======
>>>>>>> e80f6ac349904029993ef76d044eac87f8ee41d3
            )

    ### INITIALIZER ###

    def __init__(
            self, 
            name=None,
<<<<<<< HEAD
            time_signatures=None
        ):
            super(SegmentMaker, self).__init__()
            self._lilypond_file = None
            self._rhythm_definitions = []
            self._segment_directory = None
            self._score = None
            self.name = name
            self.time_signatures = time_signatures or []
=======
        ):
            super(SegmentMaker, self).__init__()
            self.__lilypond_file = None
>>>>>>> e80f6ac349904029993ef76d044eac87f8ee41d3


    ### PRIVATE PROPERTIES ###

    @property 
    def _music_voices(self):
        return(
                self._score["Flute_Music_Voice"],
                self._score["Bb_Clarinet_Music_Voice"],
                self._score["Guitar_Music_Voice"],
                self._score["Viola_Music_Voice"],
                )

    ### PRIVATE METHODS ###
<<<<<<< HEAD

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

=======
    
>>>>>>> e80f6ac349904029993ef76d044eac87f8ee41d3
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


    ### PUBLIC METHODS ###

    def run(
        self,
        metadata=None,
        persist=None,
        previous_metadata=None,
        previous_persist=None,
        segment_directory=None,
    ):
        """
        Runs segment-maker

<<<<<<< HEAD
=======
    def _make_score(self):
        template = Score.Template()
        score = template()
        self._score = score


    ### PUBLIC METHODS ###

    def run(
        self,
        metadata=None,
        persist=None,
        previous_metadata=None,
        previous_persist=None,
        segment_directory=None,
    ):
        """
        Runs segment-maker

>>>>>>> e80f6ac349904029993ef76d044eac87f8ee41d3
        Returns LilyPond file.
        """
        self._metadata = abjad.OrderedDict(metadata)
        self._persist = abjad.OrderedDict(persist)
        self._segment_directory = segment_directory
        self._make_score()
        self._make_lilypond_file()
<<<<<<< HEAD
        self._handle_time_signatures()
=======
>>>>>>> e80f6ac349904029993ef76d044eac87f8ee41d3
        return self._lilypond_file
