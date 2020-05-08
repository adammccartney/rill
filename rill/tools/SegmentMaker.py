import abjad
import baca
import copy
from .RhythmDefinition import RhythmDefinition
from .ScoreTemplate import ScoreTemplate


class SegmentMaker(abjad.SegmentMaker):
    """
    Segment-maker.

    >>> import ins_wasser

    ..  container:: example

        >>> maker = ins_wasser.SegmentMaker()
        >>> abjad.f(maker)
        ins_wasser.SegmentMaker(
            metronome_marks=[],
            time_signatures=[],
            )

    """

    ### CLASS ATTRIBUTES ###

    __documentation_section__ = None

    __slots__ = (
        "_lilypond_file",
        "_metadata",
        "_rhythm_definitions",
        "_score",
        "markup_leaves",
        "metronome_marks",
        "name",
        "time_signatures",
    )

    ### INITIALIZER ###

    def __init__(
        self,
        markup_leaves=None,
        name=None,
        metronome_marks=None,
        time_signatures=None,
    ):
        super(SegmentMaker, self).__init__()
        self._lilypond_file = None
        self._rhythm_definitions = []
        self._segment_directory = None
        self._score = None
        self.markup_leaves = markup_leaves
        self.name = name
        self.metronome_marks = metronome_marks or []
        self.time_signatures = time_signatures or []

    ### PRIVATE PROPERTIES ###

    @property
    def _music_voices(self):
        return (
            self._score["Viola_I_Music_Voice"],
            self._score["Viola_II_Music_Voice"],
        )

    ### PRIVATE METHODS ###

    def _attach_leaf_index_markup(self):
        if not self.markup_leaves:
            return
        for voice in self._music_voices:
            logical_ties = abjad.iterate(voice).logical_ties()
            for i, logical_tie in enumerate(logical_ties):
                markup = abjad.Markup(i)
                abjad.attach(markup, logical_tie.head)

    def _call_rhythm_definitions(self):
        for rhythm_definition in self._rhythm_definitions:
            rhythm_definition(self._score)

    def _configure_lilypond_file(self):
        lilypond_file = self._lilypond_file
        lilypond_file.header_block.title = None
        lilypond_file.header_block.composer = None

    def _configure_score(self):
        for staff in self._get_staves():
            leaf = abjad.inspect(staff).leaf(0)
            abjad.attach(abjad.Clef("alto"), leaf)

    def _get_staves(self):
        return (self._score["Viola_I"], self._score["Viola_II"])

    def _handle_metronome_marks(self):
        if not self.metronome_marks:
            return
        context = self._score["Global_Skips"]
        skips = baca.select(context).skips()
        skip_count = len(skips)
        prototype = (
            baca.Accelerando,
            abjad.Fermata,
            abjad.MetronomeMark,
            baca.Ritardando,
        )
        for i, expression in enumerate(self.metronome_marks):
            index = expression[0]
            if index < 0:
                index = skip_count + index
            skip = skips[index]
            indicator = expression[1]
            trend = None
            if isinstance(indicator, list):
                assert len(indicator) == 2, repr(indicator)
                indicator, trend = indicator
                trend = copy.copy(trend)
            indicator = copy.copy(indicator)
            assert isinstance(indicator, prototype), repr(indicator)
            if isinstance(indicator, abjad.Fermata):
                abjad.attach(indicator, skip)
            elif isinstance(indicator, abjad.MetronomeMark):
                left_text = indicator._get_markup()
                if trend:
                    style = "dashed-line-with-arrow"
                else:
                    style = "invisible-line"
                start_text_span = abjad.StartTextSpan(
                    left_text=left_text, style=style
                )
                abjad.attach(start_text_span, skip)
                indicator._hide = True
                abjad.attach(indicator, skip)
                if trend:
                    trend._hide = True
                    abjad.attach(trend, skip)
            else:
                trend_prototype = (baca.Accelerando, baca.Ritardando)
                assert isinstance(indicator, trend_prototype)
                left_text = indicator._get_markup()
                start_text_span = abjad.StartTextSpan(
                    left_text=left_text, style="dashed-line-with-arrow"
                )
                abjad.attach(start_text_span, skip)
                indicator._hide = True
                abjad.attach(indicator, skip)
            if 0 < i and not isinstance(indicator, abjad.Fermata):
                stop_text_span = abjad.StopTextSpan()
                abjad.attach(stop_text_span, skip)
            if len(expression) == 3:
                staff_padding = expression[2]
                string = f"\override Script.staff-padding = {staff_padding}"
                command = abjad.LilyPondLiteral(string)
                abjad.attach(command, skip)
                string = (
                    f"\override TextScript.staff-padding = {staff_padding}"
                )
                command = abjad.LilyPondLiteral(string)
                abjad.attach(command, skip)
                value = staff_padding + 0.75
                string = f"\override TextSpanner.staff-padding = {value}"
                command = abjad.LilyPondLiteral(string)
                abjad.attach(command, skip)
        stop_text_span = abjad.StopTextSpan()
        abjad.attach(stop_text_span, skips[-1])

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

    def _make_lilypond_file(self):
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
        self._handle_time_signatures()
        self._handle_metronome_marks()
        self._call_rhythm_definitions()
        self._configure_score()
        self._attach_leaf_index_markup()
        self._add_container_identifiers()
        score_block = self._lilypond_file["score"]
        score = score_block["Score"]
        #        if not abjad.inspect(score).wellformed():
        #            string = abjad.inspect(score).tabulate_wellformedness()
        #            raise Exception(string)
        return self._lilypond_file
