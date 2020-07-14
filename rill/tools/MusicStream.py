import abjad
import copy
import typing

from abjadext import rmakers

class VoiceContainer(object):
    """Container for sequential voices"""
    def __init__(self, voices=None, instrument_name=None):
        self._voices = voices or []
        self.instrument_name = instrument_name or ""
    
    def __format__(self, format_specification="") -> str:
        """
        Formats articulation.
        """
        return abjad.StorageFormatManager(self).get_storage_format()
    
    def __iter__(self) -> typing.Iterator:
        """
        Iterates voice container

        Iterates items only once.

        Does not iterate infinitely.
        """
        return self._voices.__iter__()

    ### PUBLIC METHODS ###
    
    def update(self, new_voices):
        del(self._voices)
        self._voices = new_voices

    ### PUBLIC PROPERTIES ###

    @property
    def voices(self) -> list:
        """Getter for voices"""
        return self._voices

    @voices.setter
    def voices(self, voices):
        """Appends new voices to those currently stored in object"""
        for voice in voices:
            self._voices.append(voice)

    @voices.deleter
    def voices(self):
        """Deletes all current voices stored in object"""
        del self._voices


class PitchVoice(object):
    """Creates a voice with notes
    """
    def __init__(self, notes=None):
        self.notes = notes or []
        self._handle_notes()
    
    def __format__(self, format_specification="") -> str:
        """
        Formats articulation.
        """
        return abjad.StorageFormatManager(self).get_storage_format()
    
    def __iter__(self) -> typing.Iterator:
        """
        Iterates voice only once.

        Does not iterate infinitely.
        """
        return self._voice.__iter__()


     ### PRIVATE METHODS ###

    def _handle_notes(self):
        self._voice = abjad.Voice()
        for argument in self.notes:
            if isinstance(argument, abjad.Component):
                copied_expr = copy.deepcopy(argument)
                self._voice.append(copied_expr)
            elif isinstance(argument, str):
                if argument.startswith("r"):
                    rest = abjad.Rest(argument)
                    self._voice.append(rest)
                else:
                    raise ValueError(f"what is {argument!r}?")
            elif isinstance(argument, tuple):
                component = self._tuple_to_component(argument)
                self._voice.append(component)
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

    @property
    def voice(self) -> abjad.Voice:
        """Getter for voice"""
        return self._voice

class DynamicVoice(object):
    """Voice of articulations"""
    
    def __init__(self, pitch_voice=None, dynamics=None):
        self._pitch_voice = pitch_voice or rill.PitchVoice()
        self._voice = copy.deepcopy(pitch_voice)
        self.dynamics = dynamics
        self._handle_dynamics()

    def __format__(self, format_specification="") -> str:
        """
        Formats articulation.
        """
        return abjad.StorageFormatManager(self).get_storage_format()

    ### PRIVATE METHODS ###

    def _handle_dynamics(self): 
        voice = self._pitch_voice
        leaves = abjad.select(voice).leaves()
        if not leaves:
            return
        music_durations = [abjad.inspect(_).duration() for _ in leaves]
        maker = rmakers.multiplied_duration(abjad.Skip)
        dynamics_skips = maker(music_durations)
        dynamics_voice = self._voice
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

    ### PUBLIC PROPERTIES ###
    
    @property
    def voice(self) -> abjad.Voice:
        """Getter for voice"""
        return self._voice


class MarkupVoice():
    """Voice of markup"""
    def __init__(self, dynamic_voice=None, markup=None):
        self._dynamic_voice = dynamic_voice or rill.DynamicVoice()
        self._voice = copy.deepcopy(dynamic_voice)
        self.markup = markup

    def __format__(self, format_specification="") -> str:
        """
        Formats articulation.
        """
        return abjad.StorageFormatManager(self).get_storage_format()

    ### PRIVATE METHODS ###
    
    def _handle_markup(self):
        voice = self._dynamic_voice
        leaves = abjad.select(voice).leaves()
        if not leaves:
            return
        music_durations = [abjad.inspect(_).duration() for _ in leaves]
        maker = rmakers.multiplied_duration(abjad.Skip)
        selections = maker(music_durations)
        skips = abjad.select(selections).components(abjad.Skip)
        markup_voice = self._voice
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

class MusicReservoir():
    """Stores up all voices used per instrument in a score"""
    pass

class MusicOutflow():
    """Streams voices into staves in a score per instrument"""
    pass

if __name__ == '__main__':
    import abjad
    import rill
    
    notes = [
            ("c'", abjad.Duration(1,2), rill.tremolo(16)), 
            ("d'", abjad.Duration(1,4)), 
            (abjad.Chord("<c e g>"), abjad.Duration(1,1)),
            ]
    container = VoiceContainer(instrument_name="Violin")
    
    voice = PitchVoice(notes)
    
    more_notes = [
            ("f'", abjad.Duration(1,8)), 
            ("g'", abjad.Duration(1,2)), 
            (abjad.Chord("<d e f>"), abjad.Duration(1,4)),
            ]
    new_voice = PitchVoice(more_notes)
    
    dynamics = [
            (0, abjad.Dynamic('pp'), 1.5),
            (2, abjad.Dynamic('fp')),
            ]

    new_phrase = DynamicVoice(new_voice, dynamics)
    abjad.f(new_phrase)
