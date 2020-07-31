import abjad
import rill 

from rill.tools.FuzzyHarmony import FuzzyHarmony as FuzzyHarmony
from rill.tools.FuzzyHarmony import Diad as Diad
from rill.tools.FuzzyHarmony import LegatoArpeggio as LegatoArpeggio
from rill.tools.FuzzyHarmony import Progression as Progression

from rill.tools.FuzzyHarmony import ( 
        replace_and_make_new_progression as replace_and_make_new_progression,
        get_global_minima as get_global_minima,
        get_global_maxima as get_global_maxima, 
        invert_up as invert_up,
        invert_down as invert_downi,
        )

# Testing Classes in the FuzzyHarmony Module

def test_defaults():
    """Using no paramaters should init defaults"""
    d1 = Diad()
    d2 = Diad(None)
    assert d1 == d2

def test_pitch_equality():
    d1 = Diad((abjad.NamedPitch("c'"), abjad.NamedPitch("g'")))
    d2 = Diad((abjad.NamedPitch("c'"), abjad.NamedPitch("g'")))
    assert d1 == d2
