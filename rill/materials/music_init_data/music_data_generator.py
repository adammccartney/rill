import abjad

from dataclasses import dataclass
from typing import List, Sequence

from rill.tools.AttachmentMaker import (AttachmentMaker,
                                        AccentAttachmentMaker)
from rill.materials.pitch.definition import chord_voice


@dataclass
class InstrumentMusicData:
    pitches: abjad.CyclicTuple
    attachments: List[AttachmentMaker]
    denominator: int
    time_signature_pairs: Sequence[tuple]
    talea: List[int]


@dataclass
class SegmentMusicData:
    mu_makers: List[InstrumentMusicData]


# Pitches
v1_pitch_materials = chord_voice["black"][5][0:3]
v1_pitch_materials += chord_voice["red"][5][0:3]

v1_pitches_segment_A = abjad.CyclicTuple(v1_pitch_materials)

tenuto_attachment_maker = AccentAttachmentMaker(
    selector=abjad.select().logical_ties(),
    attachment=abjad.Articulation("tenuto")
)

staccato_attachment_maker = AccentAttachmentMaker(
    selector=abjad.select().logical_ties(),
    attachment=abjad.Staccato()
)

v1_attachments_segment_A = [tenuto_attachment_maker, staccato_attachment_maker]
v1_denominator_segment_A = 16
v1_tsig_pairs_segment_A = [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4)]
v1_talea_segment_A = [1, 2, -3, 4]

v1_init_data_segment_A = InstrumentMusicData(
    pitches=v1_pitches_segment_A,
    attachments=v1_attachments_segment_A,
    denominator=v1_denominator_segment_A,
    time_signature_pairs=v1_tsig_pairs_segment_A,
    talea=v1_talea_segment_A,
)

if __name__ == '__main__':
    print(v1_init_data_segment_A)
    for attachment in v1_init_data_segment_A.attachments:
        print(attachment)
