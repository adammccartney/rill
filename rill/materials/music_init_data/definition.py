import re
import abjad

from dataclasses import dataclass, field
from typing import Dict, List, Sequence

from rill.tools.AttachmentMaker import (AttachmentMaker,
                                        AccentAttachmentMaker)
from rill.materials.pitch.definition import chord_voice

def make_default_pitches():
    default_pitch_materials = chord_voice["black"][5][0:3]
    default_pitch_materials += chord_voice["red"][5][0:3]
    default_pitches = abjad.CyclicTuple(default_pitch_materials)
    return default_pitches


def make_default_attachments():
    tenuto_attachment_maker = AccentAttachmentMaker(
        selector=abjad.select().logical_ties(),
        attachment=abjad.Articulation("tenuto")
    )

    staccato_attachment_maker = AccentAttachmentMaker(
        selector=abjad.select().logical_ties(),
        attachment=abjad.Staccato()
    )

    default_attachments = [tenuto_attachment_maker, staccato_attachment_maker]
    return default_attachments


default_denominator = 16


def make_default_tsig_pairs():
    default_tsig_pairs = [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4)]
    return default_tsig_pairs


def make_default_talea():
    default_talea = [1, 2, -3, 4]
    return default_talea

@dataclass
class InstrumentMusicData:
    pitches: abjad.CyclicTuple = field(default_factory=make_default_pitches)
    attachments: Sequence[AttachmentMaker] = field(
        default_factory=make_default_attachments)
    denominator: int = default_denominator
    time_signature_pairs: Sequence[tuple] = field(
        default_factory=make_default_tsig_pairs)
    talea: List[int] = field(default_factory=make_default_talea)


    def __getitem__(self, key):
        return getattr(self, key)


from rill.materials.instruments.definition import instruments


def get_instrument_names():
    instrument_names = []
    for key, item in instruments.items():
        instrument_names.append(key)
    return instrument_names


def make_segment_music_default():
    instrument_names = get_instrument_names()
    segment_defaults = {}
    for iname in instrument_names:
        instrument_input = "{instrument_name}_music_data"
        instrument_input.format(instrument_name=iname)
        instrument_input = InstrumentMusicData()
        segment_defaults[iname] = instrument_input
    return segment_defaults


@dataclass
class SegmentMusicData:
    """Stores a dictionary of segment defaults
    Access through instance.instrument_music_data[instrument]
    """
    instrument_music_data: Sequence[InstrumentMusicData] = field(
        default_factory=make_segment_music_default)

    def __getitem__(self, key):
        return getattr(self, key)


def make_empty_string():
    return ""


@dataclass
class SegmentPitchData:
    "Stores pitch data per segment as string"
    _chord_voice1: str = field(default_factory=make_empty_string)
    _chord_voice2: str = field(default_factory=make_empty_string)
    _chord_voice3: str = field(default_factory=make_empty_string)
    _chord_voice4: str = field(default_factory=make_empty_string)
    _melody_voice: str = field(default_factory=make_empty_string)
    _tremolo_voice1: str = field(default_factory=make_empty_string)
    _tremolo_voice2: str = field(default_factory=make_empty_string)

    def _replace_brackets(self, pitch_segment_as_string):
        pitch_segment = re.sub("<|>", '"', pitch_segment_as_string)
        return pitch_segment
    
    @property
    def chord_voice1(self) -> str:
        pitch_segment = self._chord_voice1
        pitch_segment_as_string = self._replace_brackets(pitch_segment)
        return pitch_segment_as_string

    @chord_voice1.setter
    def chord_voice1(self, v: str) -> None:
        self._chord_voice1 = v

    @property
    def chord_voice2(self) -> str:
        pitch_segment_as_string = self._replace_brackets(self._chord_voice2)
        return pitch_segment_as_string

    @chord_voice2.setter
    def chord_voice2(self, v: str) -> None:
        self._chord_voice2 = v

    @property
    def chord_voice3(self) -> str:
        pitch_segment_as_string = self._replace_brackets(self._chord_voice3)
        return pitch_segment_as_string

    @chord_voice3.setter
    def chord_voice3(self, v: str) -> None:
        self._chord_voice3 = v

    @property
    def chord_voice4(self) -> str:
        pitch_segment_as_string = self._replace_brackets(self._chord_voice4)
        return pitch_segment_as_string

    @chord_voice4.setter
    def chord_voice4(self, v: str) -> None:
        self._chord_voice4 = v

    @property
    def melody_voice(self) -> str:
        pitch_segment_as_string = self._replace_brackets(self._melody_voice)
        return pitch_segment_as_string

    @melody_voice.setter
    def melody_voice(self, v: str) -> None:
        self._melody_voice = v

    @property
    def tremolo_voice1(self) -> str:
        pitch_segment_as_string = self._replace_brackets(self._tremolo_voice1)
        return pitch_segment_as_string

    @tremolo_voice1.setter
    def tremolo_voice1(self, v: str) -> None:
        self._tremolo_voice1 = v

    @property
    def tremolo_voice2(self) -> str:
        pitch_segment_as_string = self._replace_brackets(self._tremolo_voice2)
        return pitch_segment_as_string

    @tremolo_voice2.setter
    def tremolo_voice2(self, v: str) -> None:
        self._tremolo_voice1 = v


if __name__ == '__main__':
   # default_init_data = InstrumentMusicData()
   # print(default_init_data)
   # def make_new_talea():
   #     return [2, 3, -4, 5]
   # adapted_data = InstrumentMusicData(talea=[2, 3, -4, 5])
   # print(adapted_data)
   # instrument_names = get_instrument_names()
   # print(instrument_names)
    #segment_defaults = make_segment_music_default()
    #for instrument_music_data in segment_defaults:
    #    print(instrument_music_data)
    #segment_test_music_data = SegmentMusicData()
    #segment_dict = segment_test_music_data.instrument_music_data
    #for instrument in instruments:
    #    print(instrument, ": ", segment_dict[instrument], '\n')

    default_pitch_materials = chord_voice["black"][5][0:3]
    default_pitch_materials += chord_voice["red"][5][0:3]
    default_pitch_data = str(default_pitch_materials)
    test_segment_pitch_data = SegmentPitchData(_chord_voice3=default_pitch_data)
    test_segment_cv3_pitch_segment = test_segment_pitch_data.chord_voice3
    print(test_segment_pitch_data)
    print(test_segment_cv3_pitch_segment)
