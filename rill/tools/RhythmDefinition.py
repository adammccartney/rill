import abjad 
import copy 
from abjadext import rmakers
import mccartney

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

    def __init__(
        self, dynamics=None, instrument_name=None, markup=None, notes=None
    ):
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
            self._score["Flute_Music_Voice"],
            self._score["Bb_Clarinet_Music_Voice"],
            self._score["Guitar_Music_Voice"],
            self._score["Viola_Music_Voice"],
        )

    def _get_staves(self):
        return (
            self._score["Flute"], 
            self._score["Bb_Clarinet"],
            self._score["Guitar"], 
            self._score["Viola"],
        )

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
        skips = mccartney.select(selections).skips()
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
                string = fr"\once \override TextScript.extra-offset"
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
            start_text_span = abjad.StartTextSpan(
                left_text=markup, style=style
            )
            abjad.attach(start_text_span, skip)
            if len(expression) == 3:
                staff_padding = expression[2]
                string = (
                    fr"\override TextScript.staff-padding = {staff_padding}"
                )
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
