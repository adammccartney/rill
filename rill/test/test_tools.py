import pathlib
import pytest
import sys

import abjad
import rill 

def test_defaults():
    """Using no paramaters should initialize defaults"""
    d1 = rill.Diad()
    d2 = rill.Diad(None)
    assert d1.pitches == d2.pitches
    fz1 = rill.FuzzyHarmony()
    fz2 = rill.FuzzyHarmony("",None)
    assert fz1.shortname == fz2.shortname
    assert fz1.segment == fz2.segment

def test_pitch_equality():
    """Using the same pitches to construct should lead to equality"""
    d1 = rill.Diad((abjad.NamedPitch("c'"), abjad.NamedPitch("g'")))
    d2 = rill.Diad((abjad.NamedPitch("c'"), abjad.NamedPitch("g'")))
    assert d1.pitches == d2.pitches

def test_member_access():
    """Check field functionality of rill.Diad, rill.FuzzyHarmony, LegatoArpeggio"""
    d = rill.Diad((abjad.NamedPitch("c'"), abjad.NamedPitch("g'")))
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
    f = rill.FuzzyHarmony('bf_ii', cmin7_6)
    assert abjad.NamedPitch("c''") in f.pitches
    assert abjad.NamedPitch("d''") not in f.pitches
