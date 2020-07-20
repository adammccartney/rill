import copy
import pathlib

import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony

from rill.tools.barlines import barline as barline
from rill.tools.clef import clef as clef
from rill.tools.FuzzyHarmony import Diad as Diad
from rill.tools.FuzzyHarmony import LegatoArpeggio as LegatoArpeggio
from rill.tools.material_methods import transpose_segment as transpose_segment
from rill.tools.tremolo import tremolo as tremolo

from abjad import NamedPitch as NamedPitch
from typing import List

#####################
# Setting up segment ### [A] ###
#####################

this_current_directory =  pathlib.Path(__file__).parent 
score = rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _phrase_outflows=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=rill.build_path,
                                segment_name='B',
                                rehearsal_mark=2,
                                tempo=((1, 4), 50),
                                time_signatures=[(4, 4)] * 44,
                                )

#-----------------/________________________
# Pitch Material /  Constants for section /
#_______________/------------------------/

emin7 = rill.tetrads['e_i']
emin7_6 = rill.invert_up(emin7, 1)
emin7_64 = rill.invert_up(emin7, 2)
cmin7_42 = rill.invert_up(emin7, 3)

em7 = rill.FuzzyHarmony(e_i, emin7) # emin7
em7_6 = rill.FuzzyHarmony(e_i, emin7_6) 
em7_64 = rill.FuzzyHarmony(e_i, emin7_64)   
em7_42 = rill.FuzzyHarmony(e_i, emin7_42)

# D7(b9, 13)
fsj_65 = rill.tetrads['cs_ii']
fsj_43 = rill.invert_up(fsj_65, 1)
fsj_42 = rill.invert_up(fsj_65, 2)
efmin7 = rill.invert_up(fsj_65, 3)

fs_65 = rill.FuzzyHarmony('cs_ii', fsj_65)
fs_43 = rill.FuzzyHarmony('cs_ii', fsj_43) 
fs_42 = rill.FuzzyHarmony('cs_ii', fsj_42)   
efm7 = rill.FuzzyHarmony('cs_ii', efmin7)

""" 
    Make harmonies and fifth offsets in all octaves
    Note: octave names are in german:
    gross, klein, 
    ein-, zwei-, dreigestr = ein,- zwei-, dreigestrichen
    """

em7_hrmns_ein_zw = [em7, em7_6, em7_64, em7_42]

em7_hrmns_kln_eing = rill.transpose(em7_hrmns_ein_zw, -12)
bm7_hrmns_ein_zw = rill.transpose(em7_hrmns_ein_zw, 7)
bm7_hrmns_zw_dr = rill.transpose(em7_hrmns_ein_zw, 19)



fs7_hrmns_ein_zw = [fs_65, fs_43, fs_42, efm7]

fs7_hrmns_gr_kln = rill.transpose(fs7_hrmns_ein_zw, -24)
fs7_hrmns_kln_eing = rill.transpose(fs7_hrmns_ein_zw, -12)
fs7_hrmns_zw_dr = rill.transpose(fs7_hrmns_ein_zw, 12)

cs7_hrmns_ein_zw = rill.transpose(fs7_hrmns_ein_zw, 7)
cs7_hrmns_zw_dr = rill.transpose(fs7_hrmns_ein_zw, 19)


# ----- Diads

fs7_diads_gr_kln = rill.make_diads(fs7_hrmns_gr_kln, interval_doubling='d5')
fs7_diads_kln_eing = rill.make_diads(fs7_hrmns_kln_eing, interval_doubling='d5')

fs7_fifths_gr_kln = [fs7_diads_gr_kln[0][2], fs7_diads_gr_kln[0][3]]
fs7_fifths_kln_eing = [fs7_diads_kln_eing[0][2], fs7_diads_kln_eing[0][3]]

# -- sequences of notes for arpeggios

seq_one = (1, 0, 3, 2)
seq_two = (3, 2, 0, 1)
seq_three = (2, 0, 1, 3)


#--------------/
#   Violin    /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Monosynth'

#-------------------PolySynth----------------#

#--------------/
# RH_Voice_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'RH_I'

#--------------/
# LH_Voice_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'LH_I'

#--------------------------------------------#mport abjad
