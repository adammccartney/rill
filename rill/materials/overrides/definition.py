import abjad
import rill

from dataclasses import dataclass, field

from rill.tools.OverrideMaker import NoteHeadOverrideMaker


def make_cross_note_head_override():
    cross_note_head_override = NoteHeadOverrideMaker('crgss')
    return cross_note_head_override

def make_harmonic_mixed_note_head_override():
    harmonic_mixed_note_head_override = NoteHeadOverrideMaker('harmonic-mixed')
    return harmonic_mixed_note_head_override

@dataclass
class NoteHeadOverrideData:
    cross: NoteHeadOverrideMaker = field(
        default_factory=make_cross_note_head_override
    )
    harmonic_mixed: NoteHeadOverrideMaker = field(
        default_factory=make_harmonic_mixed_note_head_override
    )
