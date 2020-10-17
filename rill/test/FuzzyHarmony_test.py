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

def test_defaults():
    """Using no paramaters should initialize defaults"""
    d1 = Diad()
    d2 = Diad(None)
    assert d1.pitches == d2.pitches
    fz1 = FuzzyHarmony()
    fz2 = FuzzyHarmony("",None)
    assert fz1.shortname == fz2.shortname
    assert fz1.segment == fz2.segment

def test_pitch_equality():
    """Using the same pitches to construct should lead to equality"""
    d1 = Diad((abjad.NamedPitch("c'"), abjad.NamedPitch("g'")))
    d2 = Diad((abjad.NamedPitch("c'"), abjad.NamedPitch("g'")))
    assert d1.pitches == d2.pitches

def test_member_access():
    """Check field functionality of Diad, FuzzyHarmony, LegatoArpeggio"""
    d = Diad((abjad.NamedPitch("c'"), abjad.NamedPitch("g'")))
    assert d.pitches == (abjad.NamedPitch("c'"), abjad.NamedPitch("g'"))
    assert d.pitch_string == "c' g'"
    assert d.lower == "c'"
    assert d.upper == "g'"
    cmin7_6 = rill.tetrads['bf_ii']
    tetrad = (
            abjad.NamedPitch("ef'"), 
            abjad.NamedPitch("g'"), 
            abjad.NamedPitch("bf'"), 
            abjad.NamedPitch("c''"),
            )
    f = FuzzyHarmony('bf_ii', cmin7_6)
    assert abjad.NamedPitch("c''") in f.pitches
    assert abjad.NamedPitch("d''") not in f.pitches
