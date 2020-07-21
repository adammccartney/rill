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
                                segment_name='C',
                                rehearsal_mark=3,
                                tempo=((1, 4), 50),
                                time_signatures=([(4, 4)] * 20),
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

# D7(b9, 13)
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


# ---- Diads 



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

fl_trem_I = abjad.TremoloContainer(16, "{0}32 {1}".format(I_fl_5, I_fl_4))
fl_trem_II = abjad.TremoloContainer(16, "{0}32 {1}".format(II_fl_5, II_fl_4))
fl_trem_III = abjad.TremoloContainer(16, "{0}32 {1}".format(III_fl_5, III_fl_4))
fl_trem_IV = abjad.TremoloContainer(16, "{0}32 {1}".format(IV_fl_5, IV_fl_4))

rhythm_definition.notes = [
        (sul_I, abjad.Duration(1), rill.tie()),
        (sul_I, abjad.Duration(1), rill.tie()),
        (sul_I, abjad.Duration(1), rill.tie()),
        (sul_I, abjad.Duration(1)),
        #----------------Bar 5
        (fl_trem_I, abjad.Duration(1), rill.harmonic_mixed_on()),
        (I_fl_2, abjad.Duration(1)),
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
        #----------------Bar 29
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 33
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 37
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 41
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
    ]


rhythm_definition.dynamics = []

rhythm_definition.markup = []

#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Monosynth'

diad_one = rill.vln_str_diads['I'].pitch_string
diad_two = rill.vln_str_diads['II'].pitch_string
diad_three = rill.vln_str_diads['III'].pitch_string
diad_four = rill.vln_str_diads['IV'].pitch_string

rhythm_definition.notes = [
        (diad_one, abjad.Duration(1), rill.tremolo(32)),
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
        #----------------Bar 29
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 33
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 37
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 41
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
    ]

rhythm_definition.dynamics = []

rhythm_definition.markup = []

#-------------------PolySynth----------------#

#--------------/
# RH_Voice_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'RH_I'

rhythm_definition.notes = [
        ("r1"),
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
        #----------------Bar 29
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 33
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 37
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 41
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
    ]

rhythm_definition.dynamics = []

rhythm_definition.markup = []


#--------------/
# LH_Voice_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'LH_I'

rhythm_definition.notes = [
        ("r1"),
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
        #----------------Bar 29
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 33
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 37
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #----------------Bar 41
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
    ]

rhythm_definition.dynamics = []

rhythm_definition.markup = []

#-------------------------------------Run segment

lilypond_file = segment_maker.run()
