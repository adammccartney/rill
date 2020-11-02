import abjad
import rill

from collections import namedtuple
from dataclasses import dataclass
from typing import List

from rill.tools.AttachmentMaker import *
from rill.materials.pitch.definition import *


@dataclass
class MusicInitData:
    pitches: abjad.CyclicTuple
    attachments: List[AttachmentMaker]
    denonimator: int
    time_signature_pairs: List[tuple[int, int]]
    talea: List[int]


# Pitches
v1_pitch_materials = rill.chord_voice["black"][5][0:3] + rill.chord_voice["red"][5][0:3]
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

v1_args_segment_A = MusicInitData(
                     v1_pitches_segment_A,
                     v1_attachments_segment_A,
                     v1_denominator_segment_A,
                     v1_tsig_pairs_segment_A,
                     v1_talea_segment_A)

MuData = namedtuple('instrument', ['pitches',
                                   'attachments',
                                   'denominator',
                                   'ts_pairs',
                                   'talea'])

#Flute1_segment_A = MuData('Flute1', [v1_args_segment_A])

if __name__ == '__main__':
    print(v1_args_segment_A)
