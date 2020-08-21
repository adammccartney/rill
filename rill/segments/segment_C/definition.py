import copy
import pathlib

import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony

from rill.tools.accents import staccato as stassato
from rill.tools.accents import tenuto as tenuto
from rill.tools.barlines import barline as barline
from rill.tools.clef import clef as clef
from rill.tools.FuzzyHarmony import Diad as Diad
from rill.tools.FuzzyHarmony import LegatoArpeggio as LegatoArpeggio
from rill.tools.grace import *
from rill.tools.material_methods import transpose_segment as transpose_segment
from rill.tools.tremolo import tremolo as tremolo

from abjad import NamedPitch as NamedPitch
from typing import List

#####################
# Setting up segment ### [C] ###
#####################

this_current_directory =  pathlib.Path(__file__).parent 
test_build_path = rill.build_path 
score = rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=rill.build_path,
                                segment_name='segment_C',
                                rehearsal_mark=3,
                                tempo=((1, 4), 50),
                                time_signatures=[(4, 4)] * 44,
                                )

#-----------------/________________________
# Pitch Material /  Constants for section /
#_______________/------------------------/

fd7b9_42 = rill.tetrads['bf_v']
fd7b9_6 = rill.invert_up(fd7b9_42, 1)
fd7b9_64 = rill.invert_up(fd7b9_42, 2)
fd7b9 = rill.invert_up(fd7b9_42, 3)

f7b9_42 = rill.FuzzyHarmony('bf_v', fd7b9_42) # emin7
f7b9_6 = rill.FuzzyHarmony('bf_v', fd7b9_6) 
f7b9_64 = rill.FuzzyHarmony('bf_v', fd7b9_64)   
f7b9 = rill.FuzzyHarmony('bf_v', fd7b9)

fsj9 = rill.tetrads['g_i']
fsj9_2 = rill.invert_up(fsj9, 1)
fsj9_6 = rill.invert_up(fsj9, 2)
fsj9_64 = rill.invert_up(fsj9, 3)

fs9 = rill.FuzzyHarmony('g_i', fsj9)
fs9_2 = rill.FuzzyHarmony('g_i', fsj9_2) 
fs9_6 = rill.FuzzyHarmony('g_i', fsj9_6)   
fs9_64 = rill.FuzzyHarmony('g_i', fsj9_64)

""" 
    Make harmonies and fifth offsets in all octaves
    Note: octave names are in german:
    gross, klein, 
    ein-, zwei-, dreigestr = ein,- zwei-, dreigestrichen
    """

auth_one_ein_zw = [f7b9_42, f7b9_6, f7b9_64, f7b9]
auth_one_gr = rill.transpose(auth_one_ein_zw, -24)
auth_one_kl_eing = rill.transpose(auth_one_ein_zw, -12)

plag_one_zw_dr = rill.transpose(auth_one_ein_zw, 19)
plag_one_ein_zw = rill.transpose(auth_one_ein_zw, 7)
plag_one_gr = rill.transpose(auth_one_ein_zw, -17)

auth_two_ein_zw = [fs9, fs9_2, fs9_6, fs9_64]

auth_two_gr_kln = rill.transpose(auth_two_ein_zw, -24)
auth_two_kln_eing = rill.transpose(auth_two_ein_zw, -12)
auth_two_zw_dr = rill.transpose(auth_two_ein_zw, 12)

plag_two_ein_zw = rill.transpose(auth_two_ein_zw, 7)
plag_two_zw_dr = rill.transpose(auth_two_ein_zw, 19)


# ---- Rest Leaf for time signature change to 5/8

astring = r"\time 5/8 r4 r4."
empty_58_measure = abjad.Container(astring)

bstring = r"\time 4/4 r1"
empty_44_measure = abjad.Container(bstring)

# -- sequences of notes for arpeggios

seq_one = (0, 1, 2, 3)
seq_two = (3, 2, 0, 1)
seq_three = (2, 0, 1, 3)

#--------------/
#   Violin    /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

sul_I = rill.vln_str_diads['I'].lower
sul_II = rill.vln_str_diads['II'].lower
sul_III = rill.vln_str_diads['III'].lower 
sul_IV = rill.vln_str_diads['IV'].lower

I_fl_2 = rill.pure_fifth_diads['I'].lower
II_fl_2 = rill.pure_fifth_diads['II'].lower
III_fl_2 = rill.pure_fifth_diads['III'].lower
IV_fl_2 = rill.pure_fifth_diads['IV'].lower

I_fl_3 = rill.pure_fifth_diads['I'].upper
II_fl_3 = rill.pure_fifth_diads['II'].upper
III_fl_3 = rill.pure_fifth_diads['III'].upper
IV_fl_3 = rill.pure_fifth_diads['IV'].upper

I_fl_4 = rill.pure_maj_third_diads['I'].lower
II_fl_4 = rill.pure_maj_third_diads['II'].lower
III_fl_4 = rill.pure_maj_third_diads['III'].lower
IV_fl_4 = rill.pure_maj_third_diads['IV'].lower

I_fl_5  = rill.pure_maj_third_diads['I'].upper
II_fl_5 = rill.pure_maj_third_diads['II'].upper
III_fl_5 = rill.pure_maj_third_diads['III'].upper
IV_fl_5 = rill.pure_maj_third_diads['IV'].upper

fifth_fl_trem_I = abjad.TremoloContainer(16, "{0}32 {1}".format(I_fl_2, I_fl_3))
fifth_fl_trem_II = abjad.TremoloContainer(16, "{0}32 {1}".format(II_fl_2, II_fl_3))
fifth_fl_trem_III = abjad.TremoloContainer(16, "{0}32 {1}".format(III_fl_2, III_fl_3))
fifth_fl_trem_IV = abjad.TremoloContainer(16, "{0}32 {1}".format(IV_fl_2, IV_fl_3))

third_fl_trem_I = abjad.TremoloContainer(16, "{0}32 {1}".format(I_fl_5, I_fl_4))
third_fl_trem_II = abjad.TremoloContainer(16, "{0}32 {1}".format(II_fl_5, II_fl_4))
third_fl_trem_III = abjad.TremoloContainer(16, "{0}32 {1}".format(III_fl_5, III_fl_4))
third_fl_trem_IV = abjad.TremoloContainer(16, "{0}32 {1}".format(IV_fl_5, IV_fl_4))

rhythm_definition.notes = [
        (sul_I, abjad.Duration(1), rill.time_signature("4/4"), rill.tie()),
        (sul_I, abjad.Duration(1), rill.tie()),
        (sul_I, abjad.Duration(1), rill.tie()),
        (I_fl_2, abjad.Duration(1), rill.harmonic_mixed_on()),
        #----------------Bar 5
        (fifth_fl_trem_I),
        (I_fl_3, abjad.Duration(1)),
        (third_fl_trem_I),
        (I_fl_3, abjad.Duration(1)),
        #----------------Bar 9
        (third_fl_trem_I),
        (I_fl_3, abjad.Duration(1)),
        (fifth_fl_trem_I),
        (I_fl_2, abjad.Duration(1)),
        #----------------Bar 13
        (sul_I, abjad.Duration(1), rill.default_on(), rill.tie()),
        (sul_I, abjad.Duration(1), rill.tie()),
        (sul_I, abjad.Duration(1)),
        ("r1"),
        #----------------Bar 17
        ("r1"),
        ("r1"),
        (sul_III, abjad.Duration(1), rill.tie(), rill.default_on()),
        (sul_III, abjad.Duration(1), rill.tie(), rill.default_on()),
        #----------------Bar 21
        (sul_III, abjad.Duration(1), rill.tie(), rill.default_on()),
        (III_fl_2, abjad.Duration(1), rill.harmonic_mixed_on()),
        (fifth_fl_trem_III),
        (III_fl_3, abjad.Duration(1), rill.tie()),
        #----------------Bar 25
        (third_fl_trem_III),
        (III_fl_3, abjad.Duration(1)),
        (third_fl_trem_III),
        (III_fl_3, abjad.Duration(1)),
        #----------------Bar 29
        (fifth_fl_trem_III),
        (III_fl_2, abjad.Duration(1)),
        (sul_III, abjad.Duration(1), rill.tie(), rill.default_on()),
        (sul_III, abjad.Duration(1), rill.tie()),
        #----------------Bar 33
        (sul_III, abjad.Duration(1), rill.tie()),
        (sul_III, abjad.Duration(1), rill.tie()),
        (sul_III, abjad.Duration(1), rill.tie()),
        (sul_III, abjad.Duration(1), rill.tie()),
        #----------------Bar 37
        (sul_III, abjad.Duration(1), rill.tie()),
        (sul_III, abjad.Duration(1), rill.tie()),
        (sul_III, abjad.Duration(1), rill.tie()),
        (sul_III, abjad.Duration(1)),
        #----------------Bar 41
        (empty_58_measure),
        ("r4"),
        (sul_II, abjad.Duration(3, 8), rill.staccato()),
        ("r4"),
        (III_fl_2, abjad.Duration(3, 8), rill.staccato(), 
                rill.harmonic_mixed_on()),
        ("r4"),
        (II_fl_3, abjad.Duration(3, 8), rill.staccato()),
        #----------------Bar 45
        ("r4"),
        (sul_III, abjad.Duration(3, 8), rill.staccato(), rill.default_on()),
        ("r4"),
        (II_fl_3, abjad.Duration(3, 8), rill.staccato(), 
                rill.harmonic_mixed_on()),
        ("r4"),
        (III_fl_2, abjad.Duration(3, 8), rill.staccato()),
        ("r4"),
        (II_fl_4, abjad.Duration(3, 8), rill.staccato()),
        #----------------Bar 50
        ("r4"),
        (sul_II, abjad.Duration(3, 8), rill.staccato(), rill.default_on()),
        ("r4"),
        (III_fl_3, abjad.Duration(3, 8), rill.staccato(), 
                rill.harmonic_mixed_on()),
        ("r4"),
        (III_fl_4, abjad.Duration(3, 8), rill.staccato(),
                rill.barline("||")),
            ]


rhythm_definition.dynamics = [
        (0, abjad.Dynamic("niente")),
        (1, "<"),
        (2, abjad.Dynamic("pp")),
        ]

rhythm_definition.markup = [
        (0, rill.markup.flaut(), 1.5),
        (3, rill.markup.sul_I(), 5.5),
        (22, rill.markup.flaut(), 1.5),
        (25, rill.markup.sul_III(), 2.5),
        (50, rill.markup.sul_II(), 2.5),
        (52, rill.markup.sul_III(), 2.5),
        (54, rill.markup.sul_II(), 5.5),
        (56, rill.markup.sul_III(), 2.5),
        (58, rill.markup.sul_II(), 4.5),
        (60, rill.markup.sul_III(), 2.5),
        (62, rill.markup.sul_II(), 6.5),
        (66, rill.markup.sul_III(), 3.5),
        ]

#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Monosynth'

diad_one = rill.vln_str_diads['I'].pitch_string
diad_two = rill.vln_str_diads['II'].pitch_string
diad_three = rill.vln_str_diads['III'].pitch_string
diad_four = rill.vln_str_diads['IV'].pitch_string

vln_sul_I_double = sul_I
vln_sul_II_double = sul_II
vln_sul_III_double = sul_III 
vln_sul_IV_double = sul_IV

rhythm_definition.notes = [
        (diad_one, 
            abjad.Duration(1), 
            rill.time_signature("4/4"), 
            rill.tremolo(32), rill.tie()),
        (diad_one, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (diad_one, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (diad_one, abjad.Duration(1, 2), rill.tremolo(32), rill.tie()),
        (vln_sul_I_double, abjad.Duration(1, 2), rill.tremolo(32), rill.tie()),
        #----------------Bar 5
        (vln_sul_I_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_I_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_I_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_I_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        #----------------Bar 9
        (vln_sul_I_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_I_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_I_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_I_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        #----------------Bar 13
        (vln_sul_I_double, abjad.Duration(1, 2), rill.tremolo(32), rill.tie()),
        (diad_one, abjad.Duration(1, 2), rill.tremolo(32), rill.tie()),
        (diad_one, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (diad_one, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (diad_one, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        #----------------Bar 17
        (diad_one, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        ("r1"),
        (diad_three, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (diad_three, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        #----------------Bar 21
        (diad_three, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (diad_three, abjad.Duration(1, 2), rill.tremolo(32), rill.tie()),
        (vln_sul_III_double, abjad.Duration(1, 2), rill.tremolo(32), rill.tie()),
        (vln_sul_III_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_III_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        #----------------Bar 25
        (vln_sul_III_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_III_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_III_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_III_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        #----------------Bar 29
        (vln_sul_III_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_III_double, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        (vln_sul_III_double, abjad.Duration(1, 2), rill.tremolo(32), rill.tie()),
        (diad_three, abjad.Duration(1, 2), rill.tremolo(32), rill.tie()),
        (diad_three, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        #----------------Bar 33
        (diad_three, abjad.Duration(1), rill.tremolo(32), rill.tie()),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 37
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 41
        (empty_58_measure),
        ("r4"),
        ("r4."),
        ("r4"),
        ("r4."),
        ("r4"),
        ("r4."),
        #----------------Bar 45
        ("r4"),
        ("r4."),
        ("r4"),
        ("r4."),
        ("r4"),
        ("r4."),
        ("r4"),
        ("r4."),
        #----------------Bar 50
        ("r4"),
        ("r4."),
        ("r4"),
        ("r4."),
        ("r4"),
        ("r4."),
    ]

rhythm_definition.dynamics = [
        (0, abjad.Dynamic("niente")),
        (1, "<"),
        (2, abjad.Dynamic("p")),
        (3, ">"),
        (5, abjad.Dynamic("niente")),
        (6, "<"),
        (7, abjad.Dynamic("p")),
        (8, ">"),
        (10, "<"),
        (11, abjad.Dynamic("p")),
        (12, ">"),
        (14, "<"),
        (15, ">"),
        (16, "<"),
        (17, ">"),
        (19, abjad.Dynamic("niente")),
        (21, "<"),
        (22, ">"),
        (23, "<"),
        (24, ">"),
        (26, "<"),
        (27, ">"),
        (28, "<"),
        (29, ">"),
        (30, "<"),
        (31, ">"),
        (31, "<"),
        (32, ">"),
        (36, abjad.Dynamic("niente")),
        ]

rhythm_definition.markup = []

#-------------------PolySynth----------------#

#--------------/
# RH_Voice_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'RH_I'

rh_seg_one_auth = auth_one_ein_zw[0].segment
rh_seg_two_auth = auth_one_ein_zw[1].segment
rh_seg_three_auth = auth_one_ein_zw[2].segment
rh_seg_four_auth = auth_one_ein_zw[3].segment

arp_one_a_auth = LegatoArpeggio(rh_seg_one_auth, seq_one)
arp_one_b_auth = LegatoArpeggio(rh_seg_two_auth, seq_two)
arp_one_c_auth = LegatoArpeggio(rh_seg_three_auth, seq_three)
arp_one_d_auth = LegatoArpeggio(rh_seg_four_auth, seq_one)

rh_arp_one_a_auth = arp_one_a_auth.stages 
rh_arp_one_b_auth = arp_one_b_auth.stages 
rh_arp_one_c_auth = arp_one_c_auth.stages 
rh_arp_one_d_auth = arp_one_d_auth.stages 

rhythm_definition.notes = [
        (empty_44_measure),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 5
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 9
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 13
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 17
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 21
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 25
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        # ------------------------------------------ Bar 29
        ("r1"),
        ("r2"),
        (rh_arp_one_a_auth[0], abjad.Duration(1, 2), rill.tie()),
        (rh_arp_one_a_auth[1], abjad.Duration(3, 4), rill.tie()),
        (rh_arp_one_a_auth[2], abjad.Duration(1, 4), rill.tie()),
        (rh_arp_one_a_auth[2], abjad.Duration(2, 4), rill.tie()),
        (rh_arp_one_a_auth[3], abjad.Duration(2, 4), rill.tie()),
        (rh_arp_one_a_auth[3], abjad.Duration(1), rill.tie()), 
        #------------Bar 33
        (rh_arp_one_b_auth[2], abjad.Duration(1), rill.tie()),
        (rh_arp_one_b_auth[2], abjad.Duration(1,2), rill.tie()),
        (rh_arp_one_b_auth[3], abjad.Duration(1,2), rill.tie()),
        (rh_arp_one_b_auth[3], abjad.Duration(1), rill.tie()),
        #----------------Bar 37
        (rh_arp_one_b_auth[3], abjad.Duration(1, 4), rill.tie()),
        (rh_arp_one_b_auth[1], abjad.Duration(3, 4), rill.tie()),
        (rh_arp_one_b_auth[0], abjad.Duration(1), rill.tie()),
        (rh_arp_one_b_auth[0], abjad.Duration(1), rill.tie()),
        (rh_arp_one_b_auth[0], abjad.Duration(1), rill.tie()),
        #----------------Bar 41
        (empty_58_measure),
        ("r4"),
        (rh_arp_one_b_auth[2], abjad.Duration(3, 8), rill.staccato()),
        ("r4"),
        (rh_arp_one_c_auth[0], abjad.Duration(3, 8), rill.staccato()),
        ("r4"),
        (rh_arp_one_d_auth[1], abjad.Duration(3, 8), rill.staccato()),
        #----------------Bar 45
        ("r4"),
        (rh_arp_one_a_auth[2], abjad.Duration(3, 8), rill.staccato()),
        ("r4"),
        (rh_arp_one_b_auth[0], abjad.Duration(3, 8), rill.staccato()),
        ("r4"),
        (rh_arp_one_c_auth[0], abjad.Duration(3, 8), rill.staccato()),
        ("r4"),
        (rh_arp_one_d_auth[1], abjad.Duration(3, 8), rill.staccato()),
        #----------------Bar 50
        ("r4"),
        (rh_arp_one_a_auth[0], abjad.Duration(3, 8), rill.staccato()),
        ("r4"),
        (rh_arp_one_b_auth[1], abjad.Duration(3, 8), rill.staccato()),
        ("r4"),
        (rh_arp_one_c_auth[2], abjad.Duration(3, 8), rill.staccato(),
                rill.barline("||")),
    ]

rhythm_definition.dynamics = [
        (30, abjad.Dynamic("pp")),
        ]

rhythm_definition.markup = []


#--------------/
# LH_Voice_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'LH_I'

segment_one_authentic = auth_one_gr[0].segment
arp_one_auth = LegatoArpeggio(segment_one_authentic, seq_three)
lh_arp_one_auth = arp_one_auth.stages

segment_one_plagal = plag_one_gr[1].segment
arp_one_plag = LegatoArpeggio(segment_one_plagal, seq_one)
lh_arp_one_plag = arp_one_plag.stages

segment_two_authentic = auth_one_gr[1].segment
arp_two_auth = LegatoArpeggio(segment_two_authentic, seq_two)
lh_arp_two_auth = arp_two_auth.stages

rhythm_definition.notes = [
        (empty_44_measure),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 5
        ("r1"),
        ("r2"),
        (lh_arp_one_plag[0], abjad.Duration(1, 2), rill.tie()),
        (lh_arp_one_plag[0], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[0], abjad.Duration(1), rill.tie()),
        # -------------- Bar9
        (lh_arp_one_auth[0], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1)), 
        #----------------Bar 13
        (lh_arp_one_plag[0], abjad.Duration(1), rill.tie()),
        (lh_arp_one_plag[0], abjad.Duration(1), rill.tie()),
        (lh_arp_one_plag[0], abjad.Duration(1), rill.tie()),
        (lh_arp_one_plag[0], abjad.Duration(1), rill.tie()),
        #----------------Bar 17
        (lh_arp_one_plag[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_plag[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_plag[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_plag[1], abjad.Duration(1), rill.tie()),
        #----------------Bar 21
        (lh_arp_one_plag[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_plag[1], abjad.Duration(1)),
        (lh_arp_one_auth[0], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[0], abjad.Duration(1), rill.tie()),
        #----------------Bar 25
        (lh_arp_one_auth[0], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[0], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[0], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[0], abjad.Duration(1), rill.tie()),
        #----------------Bar 29
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        #----------------Bar 33
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        #----------------Bar 37
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        (lh_arp_one_auth[1], abjad.Duration(1), rill.tie()),
        #----------------Bar 41
        (empty_58_measure),
        ("r4"),
        (lh_arp_one_auth[1], abjad.Duration(3, 8), rill.tie(), rill.staccato()),
        ("r4"),
        (lh_arp_one_auth[0], abjad.Duration(3, 8), rill.tie(), rill.staccato()),
        ("r4"),
        (lh_arp_two_auth[1], abjad.Duration(3, 8), rill.tie(), rill.staccato()),
        #----------------Bar 45
        ("r4"),
        (lh_arp_one_auth[0], abjad.Duration(3, 8), rill.tie(), rill.staccato()),
        ("r4"),
        (lh_arp_two_auth[0], abjad.Duration(3, 8), rill.tie(), rill.staccato()),
        ("r4"),
        (lh_arp_one_auth[3], abjad.Duration(3, 8), rill.tie(), rill.staccato()),
        ("r4"),
        (lh_arp_two_auth[2], abjad.Duration(3, 8), rill.tie(), rill.staccato()),
        #----------------Bar 50
        ("r4"),
        (lh_arp_one_auth[2], abjad.Duration(3, 8), rill.tie(), rill.staccato()),
        ("r4"),
        (lh_arp_one_auth[1], abjad.Duration(3, 8), rill.tie(), rill.staccato()),
        ("r4"),
        (lh_arp_two_auth[1], abjad.Duration(3, 8), rill.staccato(), 
                rill.barline("||")),
    ]

rhythm_definition.dynamics = [
        (6, abjad.Dynamic("pp")),
        ]

rhythm_definition.markup = []

#-------------------------------------Run segment

lilypond_file = segment_maker.run()
