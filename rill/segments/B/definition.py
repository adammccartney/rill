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

em7 = rill.FuzzyHarmony('e_i, emin7) # emin7
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

seq_one = (2, 3, 0, 2)
seq_two = (3, 2, 0, 1)
seq_three = (2, 0, 1, 3)


#--------------/
#   Violin    /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

bmin7_eingstrn = bm7_hrmns_ein_zw[0].segment
vln_arp_one = LegatoArpeggio(bmin7_eingstrn, seq_one)
violin_arp_one = vln_arp_one.pitches

m_seq_a = (0, 1, 2, 3)

# Melody One 

mel_one_a = rill.melody_lookup['bfm'][1]
mel_one_b = rill.melody_lookup['bfm'][2]

mel_one_a_oct_down = transpose_segment(mel_one_a, -12)
mel_one_a_oct_up = transpose_segment(mel_one_a, 12)

mel_one_a_arp = LegatoArpeggio(mel_one_a, m_seq_a)
mel_one_a_arp_oct_up = LegatoArpeggio(mel_one_a_oct_up, m_seq_a)
mel_one_a_arp_oct_down = LegatoArpeggio(mel_one_a_oct_down, m_seq_a)

melody_one_a = mel_one_a_arp.pitches
melody_one_a_oct_up = mel_one_a_arp_oct_up.pitches
melody_one_a_oct_down = mel_one_a_arp_oct_down.pitches

emin7_64_zwei = cm7_hrmns_ein_zw[2].segment
tr_arp_one = LegatoArpeggio(emin7_64_zwei, seq_one)
violin_arp_two = tr_arp_one.pitches 

emin7_42_zwei = cm7_hrmns_ein_zw[3].segment
tr_arp_two = LegatoArpeggio(emin7_42_zwei, seq_one)
violin_arp_three = tr_arp_two.pitches

fs7_eingstrn = d7_hrmns_zw_dr[0].segment
vln_arp_two = LegatoArpeggio(fs7_eingstrn, seq_three)
violin_arp_four = vln_arp_two.pitches


# Melody Two 

mel_two_a = rill.melody_lookup['gm'][2]
mel_two_b = rill.melody_lookup['gm'][3]
mel_two_c = rill.melody_lookup['gm'][4]

mel_two_a_arp = LegatoArpeggio(mel_two_a, m_seq_a)  
mel_two_b_arp = LegatoArpeggio(mel_two_b, m_seq_a)
mel_two_c_arp = LegatoArpeggio(mel_two_c, m_seq_a)

melody_two_a = mel_two_a_arp.pitches
melody_two_b = mel_two_b_arp.pitches
melody_two_c = mel_two_c_arp.pitches


rhythm_definition.notes = [
        ("r1"),
        ("r2"),
        (violin_arp_one[0], abjad.Duration(1, 2), rill.tie()),
        (violin_arp_one[0], abjad.Duration(1), rill.tie()),
        (violin_arp_one[0], abjad.Duration(1, 2)),
        (violin_arp_one[1], abjad.Duration(1, 2), rill.tie()),
        #------------Bar 5
        (violin_arp_one[1], abjad.Duration(1), rill.tie()),
        (violin_arp_one[1], abjad.Duration(1), rill.tie()),
        (violin_arp_one[1], abjad.Duration(1, 2), rill.tie()),
        (violin_arp_one[3], abjad.Duration(1, 2), rill.tie()),
        (violin_arp_one[3], abjad.Duration(1), rill.tie()),
        #------------Bar 9
        (violin_arp_one[3], abjad.Duration(1, 4)),
        (violin_arp_one[2], abjad.Duration(3, 4), rill.tie()),
        (violin_arp_one[2], abjad.Duration(1), ),
        ("r1"),
        ("r4"),
        (melody_one_a[0], abjad.Duration(3, 4), rill.tie()),
        #------------Bar 13
        (melody_one_a[0], abjad.Duration(1, 8)),
        ("r8"),
        (melody_one_a_oct_up[0], abjad.Duration(2, 4)), 
        (melody_one_a[1], abjad.Duration(1,4)), 
        (melody_one_a[3], abjad.Duration(1)), 
        (melody_one_a_oct_down[2], abjad.Duration(1)), 
        (violin_arp_two[0], abjad.Duration(1, 2), rill.tie()),
        (violin_arp_two[1], abjad.Duration(1, 2), rill.tie()),
        #------------Bar 17
        (violin_arp_two[1], abjad.Duration(1, 4), rill.tie()),
        (violin_arp_two[2], abjad.Duration(3, 4), rill.tie()),
        (violin_arp_two[3], abjad.Duration(1), rill.tie()),
        (violin_arp_two[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        (violin_arp_three[0], abjad.Duration(1, 2), rill.tie()),
        (violin_arp_three[1], abjad.Duration(1, 2), rill.tie()),
        #------------Bar 21
        (violin_arp_three[1], abjad.Duration(1)),
        ("r2"),
        (violin_arp_four[0], abjad.Duration(1, 2), rill.tie()),
        (violin_arp_four[0], abjad.Duration(1), rill.tie()),
        (violin_arp_four[0], abjad.Duration(1, 2)),
        (violin_arp_four[1], abjad.Duration(1, 2), rill.tie()),
        #------------Bar 25
        (violin_arp_four[1], abjad.Duration(1), rill.tie()),
        (violin_arp_four[1], abjad.Duration(1), rill.tie()),
        (violin_arp_four[1], abjad.Duration(1, 2), rill.tie()),
        (violin_arp_four[3], abjad.Duration(1, 2), rill.tie()),
        (violin_arp_four[3], abjad.Duration(1), rill.tie()),
        #------------Bar 29
        (violin_arp_four[3], abjad.Duration(1, 4)),
        (violin_arp_four[2], abjad.Duration(3, 4), rill.tie()),
        (violin_arp_four[2], abjad.Duration(1)),
        ("r1"),
        ("r1"),
        #-----------Bar 33
        ("r1"),
        ("r4"),
        (melody_two_a[2], abjad.Duration(1,4)),
        (melody_two_a[2], abjad.Duration(2,4)), 
        (melody_two_b[3], abjad.Duration(1,4)),
        (melody_two_b[3], abjad.Duration(1,4)), 
        (melody_two_b[3], abjad.Duration(2,4)), 
        (melody_two_a[2], abjad.Duration(1,4)),
        (melody_two_a[2], abjad.Duration(2,4)), 
        (melody_two_c[0], abjad.Duration(1,4)),
        #-----------Bar 37
        (melody_two_c[0], abjad.Duration(1,4)), 
        (melody_two_c[0], abjad.Duration(2,4)), 
        (melody_two_a[1], abjad.Duration(1,4)),
        (melody_two_a[1], abjad.Duration(2,4)), 
        (melody_two_b[2], abjad.Duration(1,4)),
        (melody_two_b[2], abjad.Duration(1,4)), 
        (melody_two_b[2], abjad.Duration(2,4)), 
        (melody_two_a[1], abjad.Duration(1,4)),
        (melody_two_a[1], abjad.Duration(2,4)), 
        (melody_two_c[0], abjad.Duration(1,4)),
        (melody_two_c[0], abjad.Duration(1,4)),
        (melody_two_c[0], abjad.Duration(1,4), rill.tie()),
        #-----------Bar 41
        (melody_two_c[0], abjad.Duration(1,4)),
        (melody_two_a[1], abjad.Duration(1,4)),
        (melody_two_a[1], abjad.Duration(2,4), rill.tie()), 
        (melody_two_a[1], abjad.Duration(1), rill.tie()), 
        (melody_two_a[1], abjad.Duration(1), rill.tie()),
        (melody_two_a[1], abjad.Duration(1), barline("||")),
        ]


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
