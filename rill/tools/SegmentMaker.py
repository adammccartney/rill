import abjad
import copy
import rill
import mccartney 

from abjadext import rmakers 
from .ScoreTemplate import ScoreTemplate


class PhraseCatcher(abjad.Container):
    """

    """

class RhythmDefinition(object):
    """
    Rhythm definition.
    >>> import rill
    ..  container:: example
        >>> music_maker = rill.RhythmDefinition()
        >>> abjad.f(music_maker)
        rill.RhythmDefinition(
            dynamics=[],
            markup=[],
            notes=[],
            )
    """

    ### CLASS ATTRIBUTES ###

    __slots__ = ("_score", "dynamics", "instrument_name", "markup", "notes")

    ### INITIALIZER ###

    def __init__(self, dynamics=None, instrument_name=None, markup=None, notes=None):
        self.dynamics = dynamics or []
        self.instrument_name = instrument_name
        self.markup = markup or []
        self.notes = notes or []

    ### SPECIAL METHODS ###

    def __call__(self, score):
        """
        Calls rhythm definition.
        Returns none.
        """
        self._score = score
        self._handle_notes()
        self._handle_dynamics()
        self._handle_markup()

    def __format__(self, format_specification="") -> str:
        """
        Formats articulation.
        """
        return abjad.StorageFormatManager(self).get_storage_format()

    ### PRIVATE METHODS ###

    def _get_music_voices(self):
        return (
            self._score["Viola_I_Music_Voice"],
            self._score["Viola_II_Music_Voice"],
        )

    def _get_staves(self):
        return (self._score["Viola_I"], self._score["Viola_II"])

    def _handle_dynamics(self):
        voice = self._score[f"{self.instrument_name}_Music_Voice"]
        leaves = abjad.select(voice).leaves()
        if not leaves:
            return
        music_durations = [abjad.inspect(_).duration() for _ in leaves]
        maker = rmakers.multiplied_duration(abjad.Skip)
        dynamics_skips = maker(music_durations)
        dynamics_voice = self._score[f"{self.instrument_name}_Dynamics_Voice"]
        dynamics_voice.extend(dynamics_skips)
        for expression in self.dynamics:
            index = expression[0]
            string = expression[1]
            leaf = dynamics_voice[index]
            if string in ("<", ">"):
                indicator = abjad.LilyPondLiteral("\\" + string, "after")
            elif string == "-|":
                indicator = abjad.LilyPondLiteral(r"\<", "after")
                stencil = abjad.Scheme("constante-hairpin")
                abjad.override(leaf).hairpin.stencil = stencil
            elif string == "<!":
                indicator = abjad.LilyPondLiteral(r"\<", "after")
                stencil = abjad.Scheme("abjad-flared-hairpin")
                abjad.override(leaf).hairpin.stencil = stencil
            elif string == "!>":
                indicator = abjad.LilyPondLiteral(r"\>", "after")
                stencil = abjad.Scheme("abjad-flared-hairpin")
                abjad.override(leaf).hairpin.stencil = stencil
            else:
                indicator = abjad.Dynamic(string)
            abjad.attach(indicator, leaf)
            if len(expression) == 3:
                staff_padding = expression[2]
                string = r"\override DynamicLineSpanner.staff-padding ="
                string += f" {staff_padding}"
                command = abjad.LilyPondLiteral(string)
                abjad.attach(command, leaf)
        last_leaf = dynamics_voice[-1]
        prototype = abjad.LilyPondLiteral
        if not abjad.inspect(last_leaf).has_indicator(prototype):
            if not abjad.inspect(last_leaf).has_indicator(abjad.Dynamic):
                indicator = abjad.LilyPondLiteral(r"\!", "after")
                abjad.attach(indicator, last_leaf)

    def _handle_markup(self):
        voice = self._score[f"{self.instrument_name}_Music_Voice"]
        leaves = abjad.select(voice).leaves()
        if not leaves:
            return
        music_durations = [abjad.inspect(_).duration() for _ in leaves]
        maker = rmakers.multiplied_duration(abjad.Skip)
        selections = maker(music_durations)
        skips = abjad.select(selections).components(abjad.Skip)
        markup_voice = self._score[f"{self.instrument_name}_Markup_Voice"]
        markup_voice.extend(skips)
        expressions = self.markup
        for i, expression in enumerate(expressions):
            index = expression[0]
            markup = expression[1]
            skip = skips[index]
            if len(expression) == 3 and isinstance(expression[2], tuple):
                abjad.attach(markup, skip)
                extra_offset = expression[2]
                x, y = extra_offset
                string = r"\once \override TextScript.extra-offset"
                string += f" = #'({x} . {y})"
                command = abjad.LilyPondLiteral(string)
                abjad.attach(command, skip)
                continue
            if 0 < i:
                stop_text_span = abjad.StopTextSpan()
                abjad.attach(stop_text_span, skip)
            if isinstance(markup, list):
                markup = markup[0]
                style = "dashed-line-with-arrow"
            else:
                style = "invisible-line"
            start_text_span = abjad.StartTextSpan(left_text=markup, style=style)
            abjad.attach(start_text_span, skip)
            if len(expression) == 3:
                staff_padding = expression[2]
                string = fr"\override TextScript.staff-padding = {staff_padding}"
                command = abjad.LilyPondLiteral(string)
                abjad.attach(command, skip)
                value = staff_padding + 0.75
                string = fr"\override TextSpanner.staff-padding = {value}"
                command = abjad.LilyPondLiteral(string)
                abjad.attach(command, skip)
        stop_text_span = abjad.StopTextSpan()
        abjad.attach(stop_text_span, skips[-1])

    def _handle_notes(self):
        voice = self._score[f"{self.instrument_name}_Music_Voice"]
        for argument in self.notes:
            if isinstance(argument, abjad.Component):
                copied_expr = copy.deepcopy(argument)
                voice.append(copied_expr)
            elif isinstance(argument, str):
                if argument.startswith("r"):
                    rest = abjad.Rest(argument)
                    voice.append(rest)
                else:
                    raise ValueError(f"what is {argument!r}?")
            elif isinstance(argument, tuple):
                component = self._tuple_to_component(argument)
                voice.append(component)
            else:
                raise ValueError(f"what is {argument!r}?")

    def _make_leaf(self, pitch, duration_string):
        duration = abjad.Duration(duration_string)
        maker = abjad.LeafMaker()
        leaves = maker([pitch], [duration])
        return leaves

    def _tuple_to_component(self, argument):
        pitch_string = argument[0]
        duration = argument[1]
        if isinstance(argument[0], abjad.Component):
            component = argument[0]
        elif " " in pitch_string:
            component = abjad.Chord([], duration)
            pitches = pitch_string.split()
            for pitch in pitches:
                component.note_heads.append(pitch)
        else:
            component = abjad.Note(pitch_string, duration)
        for indicator in argument[2:]:
            if indicator == "parenthesize":
                if isinstance(component, abjad.Note):
                    component.note_head.is_parenthesized = True
                elif isinstance(component, abjad.Chord):
                    for note_head in component.note_heads:
                        note_head.is_parenthesized = True
            else:
                copied_indicator = copy.deepcopy(indicator)
                abjad.attach(copied_indicator, component)
        return component

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
        "markup_leaves",
        "name",
        "time_signatures",
    )

    ## INITIALIZER ##

    def __init__(
            self,
            markup_leaves=None,
            name=None,
            time_signatures=None,
        ):
            super(SegmentMaker, self).__init__()
            self._lilypond_file = None
            self._rhythm_definitions = []
            self._segment_directory = None
            self._score = None
            self.markup_leaves = markup_leaves
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

    def _handle_metronome_marks(self):
        if not self.metronome_marks:
            return
        context = self._score["Global_Skips"]
        skips = baca.select(context).skips()
        skip_count = len(skips)
        prototype = (
            abjad.Fermata,
            abjad.MetronomeMark,
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
                start_text_span = abjad.StartTextSpan(left_text=left_text, style=style)
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
                string = rf"\override Script.staff-padding = {staff_padding}"
                command = abjad.LilyPondLiteral(string)
                abjad.attach(command, skip)
                string = rf"\override TextScript.staff-padding = {staff_padding}"
                command = abjad.LilyPondLiteral(string)
                abjad.attach(command, skip)
                value = staff_padding + 0.75
                string = rf"\override TextSpanner.staff-padding = {value}"
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
        self._attach_leaf_index_markup()
        self._add_container_identifiers()
        #score_block = self._lilypond_file["score"]
        #score = score_block["Score"]
        return self._lilypond_file



