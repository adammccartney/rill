import abjad

from dataclasses import dataclass, field
from typing import List, Sequence

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


@dataclass
class SegmentMusicData:
    mu_makers: List[InstrumentMusicData]


if __name__ == '__main__':
    default_init_data = InstrumentMusicData()
    print(default_init_data)
    def make_new_talea():
        return [2, 3, -4, 5]
    adapted_data = InstrumentMusicData(talea=[2, 3, -4, 5])
    print(adapted_data)
