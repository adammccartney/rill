import copy
import pathlib

import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony

from rill.tools.barlines import barline as barline
from rill.tools.clef import clef as clef
from rill.tools.FuzzyHarmony import Diad as Diad
from rill.tools.FuzzyHarmony import LegatoArpeggio as LegatoArpeggio
from rill.tools.PhraseMaker import PhraseOutflow as PhraseOutflow
from rill.tools.PhraseMaker import PhraseStream as PhraseStream
from rill.tools.material_methods import transpose_segment as transpose_segment
from rill.tools.tremolo import tremolo as tremolo

from abjad import NamedPitch as NamedPitch
from typing import List

#####################
# Setting up segment ### [A] ###
#####################

this_current_directory =  pathlib.Path(__file__).parent 
test_build_path = rill.build_path 
score = rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=test_build_path,
                                markup_leaves=False,
                                segment_name='A',
                                rehearsal_mark=1,
                                tempo=((1, 4), 50),
                                time_signatures=([(4, 4) * 46]),
                                )

segment_maker.metronome_marks = [
        (0, rill.metronome_marks['50'], 5),
        ]

#-----------------/________________________
# Pitch Material /  Constants for section /
#_______________/------------------------/

cmin7_6 = rill.tetrads['bf_ii']
cmin7_64 = rill.invert_up(cmin7_6, 1)
cmin7_42 = rill.invert_up(cmin7_6, 2)
cmin7 = rill.invert_up(cmin7_6, 3)

cm7_6 = rill.FuzzyHarmony('bf_ii', cmin7_6) # cmin7/e
cm7_64 = rill.FuzzyHarmony('bf_ii', cmin7_64) 
cm7_42 = rill.FuzzyHarmony('bf_ii', cmin7_42)   
cm7 = rill.FuzzyHarmony('bf_ii', cmin7)

# D7(b9, 13)
d7_9 = rill.tetrads['g_v']
d7_6 = rill.invert_up(d7_9, 1)
d7_64 = rill.invert_up(d7_9, 2)
d7 = rill.invert_up(d7_9, 3)

d7_9 = rill.FuzzyHarmony('g_v', d7_9)
d7_6 = rill.FuzzyHarmony('g_v', d7_6) 
d7_64 = rill.FuzzyHarmony('g_v', d7_64)   
d7 = rill.FuzzyHarmony('g_v', d7)

""" 
    Make harmonies and fifth offsets in all octaves
    Note: octave names are in german:
    gross, klein, 
    ein-, zwei-, dreigestr = ein,- zwei-, dreigestrichen
    """

cm7_hrmns_ein_zw = [cm7_6, cm7_64, cm7_42, cm7]

cm7_hrmns_kln_eing = rill.transpose(cm7_hrmns_ein_zw, -12)
gm7_hrmns_ein_zw = rill.transpose(cm7_hrmns_ein_zw, 7)
gm7_hrmns_zw_dr = rill.transpose(cm7_hrmns_ein_zw, 19)



d7_hrmns_ein_zw = [d7_9, d7_6, d7_64, d7]

d7_hrmns_gr_kln = rill.transpose(d7_hrmns_ein_zw, -24)
d7_hrmns_kln_eing = rill.transpose(d7_hrmns_ein_zw, -12)
d7_hrmns_zw_dr = rill.transpose(d7_hrmns_ein_zw, 12)

a7_hrmns_ein_zw = rill.transpose(d7_hrmns_ein_zw, 7)
a7_hrmns_zw_dr = rill.transpose(d7_hrmns_ein_zw, 19)


# ----- Diads

d7_diads_gr_kln = rill.make_diads(d7_hrmns_gr_kln, interval_doubling='d5')
d7_diads_kln_eing = rill.make_diads(d7_hrmns_kln_eing, interval_doubling='d5')

d7_fifths_gr_kln = [d7_diads_gr_kln[0][2], d7_diads_gr_kln[0][3]]
d7_fifths_kln_eing = [d7_diads_kln_eing[0][2], d7_diads_kln_eing[0][3]]

# -- sequences of notes for arpeggios

seq_one = (1, 0, 3, 2)
seq_two = (3, 2, 0, 1)
seq_three = (2, 0, 1, 3)

#--------------/
#   Violin    /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'


gmin7_6_eingstrn = gm7_hrmns_ein_zw[0].segment
vln_arp_one = LegatoArpeggio(gmin7_6_eingstrn, seq_one)
gmin7_6_pitches = vln_arp_one.pitches

m_seq_a = (0, 1, 2, 3)
m_frag_a = rill.melody_lookup['bfm'][1]
m_frag_b = rill.melody_lookup['bfm'][2]

m_frag_a_oct_down = transpose_segment(m_frag_a, -12)
m_frag_a_oct_up = transpose_segment(m_frag_a, 12)

m_arp_a = LegatoArpeggio(m_frag_a, m_seq_a)
m_arp_a_oct_up = LegatoArpeggio(m_frag_a_oct_up, m_seq_a)
m_arp_a_oct_down = LegatoArpeggio(m_frag_a_oct_down, m_seq_a)

melody_a = m_arp_a.pitches
melody_a_oct_up = m_arp_a_oct_up.pitches
melody_a_oct_down = m_arp_a_oct_down.pitches

cmin7_42_zwei = cm7_hrmns_ein_zw[2].segment
tr_arp_one = LegatoArpeggio(cmin7_42_zwei, seq_one)
cmin7_42_pitches = tr_arp_one.pitches 

cmin7_zwei = cm7_hrmns_ein_zw[3].segment
tr_arp_two = LegatoArpeggio(cmin7_zwei, seq_one)
cmin7_pitches = tr_arp_two.pitches

d7_9_eingstrn = d7_hrmns_zw_dr[0].segment
vln_arp_two = LegatoArpeggio(d7_9_eingstrn, seq_three)
d7_9_pitches = vln_arp_two.pitches

seg_cefaf = rill.melody_lookup['gm'][2]
seg_fadbf = rill.melody_lookup['gm'][3]
seg_bfdgef = rill.melody_lookup['gm'][4]

cefaf_arp = LegatoArpeggio(seg_cefaf, m_seq_a)  
fadbf_arp = LegatoArpeggio(seg_fadbf, m_seq_a)
bfdgef_arp = LegatoArpeggio(seg_bfdgef, m_seq_a)

melody_cefaf = cefaf_arp.pitches
melody_fadbf = fadbf_arp.pitches
melody_bfdgef = bfdgef_arp.pitches

rhythm_definition.notes = [
        ("r1"),
        ("r2"),
        (gmin7_6_pitches[0], abjad.Duration(1, 2), rill.tie()),
        (gmin7_6_pitches[0], abjad.Duration(1), rill.tie()),
        (gmin7_6_pitches[0], abjad.Duration(1, 2)),
        (gmin7_6_pitches[1], abjad.Duration(1, 2), rill.tie()),
        #------------Bar 5
        (gmin7_6_pitches[1], abjad.Duration(1), rill.tie()),
        (gmin7_6_pitches[1], abjad.Duration(1), rill.tie()),
        (gmin7_6_pitches[1], abjad.Duration(1, 2), rill.tie()),
        (gmin7_6_pitches[3], abjad.Duration(1, 2), rill.tie()),
        (gmin7_6_pitches[3], abjad.Duration(1), rill.tie()),
        #------------Bar 9
        (gmin7_6_pitches[3], abjad.Duration(1, 4)),
        (gmin7_6_pitches[2], abjad.Duration(3, 4), rill.tie()),
        (gmin7_6_pitches[2], abjad.Duration(1), rill.line_break()),
        ("r1"),
        ("r4"),
        (melody_a[0], abjad.Duration(3, 4), rill.tie()),
        #------------Bar 13
        (melody_a[0], abjad.Duration(1, 8)),
        ("r8"),
        (melody_a_oct_up[0], abjad.Duration(2, 4)), 
        (melody_a[1], abjad.Duration(1,4)), 
        (melody_a[3], abjad.Duration(1)), 
        (melody_a_oct_down[2], abjad.Duration(1)), 
        (cmin7_42_pitches[0], abjad.Duration(1, 2), rill.tie()),
        (cmin7_42_pitches[1], abjad.Duration(1, 2), rill.tie()),
        #------------Bar 17
        (cmin7_42_pitches[1], abjad.Duration(1, 4), rill.tie()),
        (cmin7_42_pitches[2], abjad.Duration(3, 4), rill.tie()),
        (cmin7_42_pitches[3], abjad.Duration(1), rill.tie()),
        (cmin7_42_pitches[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        (cmin7_pitches[0], abjad.Duration(1, 2), rill.tie()),
        (cmin7_pitches[1], abjad.Duration(1, 2), rill.tie()),
        #------------Bar 21
        (cmin7_pitches[1], abjad.Duration(1)),
        ("r2"),
        (d7_9_pitches[0], abjad.Duration(1, 2), rill.tie()),
        (d7_9_pitches[0], abjad.Duration(1), rill.tie()),
        (d7_9_pitches[0], abjad.Duration(1, 2)),
        (d7_9_pitches[1], abjad.Duration(1, 2), rill.tie()),
        #------------Bar 25
        (d7_9_pitches[1], abjad.Duration(1), rill.tie()),
        (d7_9_pitches[1], abjad.Duration(1), rill.tie()),
        (d7_9_pitches[1], abjad.Duration(1, 2), rill.tie()),
        (d7_9_pitches[3], abjad.Duration(1, 2), rill.tie()),
        (d7_9_pitches[3], abjad.Duration(1), rill.tie()),
        #------------Bar 29
        (d7_9_pitches[3], abjad.Duration(1, 4)),
        (d7_9_pitches[2], abjad.Duration(3, 4), rill.tie()),
        (d7_9_pitches[2], abjad.Duration(1), ),
        ("r1"),
        ("r1"),
        #-----------Bar 33
        ("r1"),
        ("r4"),
        (melody_fadbf[2], abjad.Duration(1,4)),
        (melody_fadbf[2], abjad.Duration(2,4)), 
        (melody_bfdgef[3], abjad.Duration(1,4)),
        (melody_bfdgef[3], abjad.Duration(1,4)), 
        (melody_bfdgef[3], abjad.Duration(2,4)), 
        (melody_fadbf[2], abjad.Duration(1,4)),
        (melody_fadbf[2], abjad.Duration(2,4)), 
        (melody_cefaf[0], abjad.Duration(1,4)),
        #-----------Bar 37
        (melody_cefaf[0], abjad.Duration(1,4)), 
        (melody_cefaf[0], abjad.Duration(2,4)), 
        (melody_fadbf[1], abjad.Duration(1,4)),
        (melody_fadbf[1], abjad.Duration(2,4)), 
        (melody_bfdgef[2], abjad.Duration(1,4)),
        (melody_bfdgef[2], abjad.Duration(1,4)), 
        (melody_bfdgef[2], abjad.Duration(2,4)), 
        (melody_fadbf[1], abjad.Duration(1,4)),
        (melody_fadbf[1], abjad.Duration(2,4)), 
        (melody_cefaf[0], abjad.Duration(1,4)),
        (melody_cefaf[0], abjad.Duration(1,4)),
        (melody_cefaf[0], abjad.Duration(1,4), rill.tie()),
        #-----------Bar 41
        (melody_cefaf[0], abjad.Duration(1,4)),
        (melody_fadbf[1], abjad.Duration(1,4)),
        (melody_fadbf[1], abjad.Duration(2,4), rill.tie()), 
        (melody_fadbf[1], abjad.Duration(1), barline("||")),
        ]

rhythm_definition.dynamics = [
        (2, abjad.Dynamic('ppp'), 2.5),
        (3, '<'),
        (5, abjad.Dynamic('p'), 2.5),
        (6, '>'),
        (13, abjad.Dynamic('ppp')),
        (16, abjad.Dynamic('pp')),
        (22, abjad.Dynamic('mp')),
        (25, '>'),
        (28, abjad.Dynamic('ppp')),
        (33, abjad.Dynamic('ppp'), 2.5),
        (34, '<'),
        (36, abjad.Dynamic('p')),
        (37, '>'),
        (44, abjad.Dynamic('ppp')),
        (50, abjad.Dynamic('pp')),
       ]

rhythm_definition.markup = [
        (0, rill.markup.tasto(), 1.5),
        (16, rill.markup.ord(), 1.5),
        (28, rill.markup.flaut_pont(), 3.5),
        (36, rill.markup.tasto(), 3.5),
        (50, rill.markup.rhythmically(), 3.5),
        ]


#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Monosynth'

cmin7_42_eing = cm7_hrmns_kln_eing[2].segment
tr_arp_one = LegatoArpeggio(cmin7_42_eing, seq_one)
cmin7_42_stages = tr_arp_one.stages 

cmin7_kln = cm7_hrmns_kln_eing[3].segment
tr_arp_two = LegatoArpeggio(cmin7_kln, seq_one)
cmin7_stages = tr_arp_two.stages 

diad_DA = Diad(d7_fifths_gr_kln[1])
diad_DA_gr_kln = diad_DA.pitch_string

diad_AE = Diad(d7_fifths_kln_eing[0])
diad_AE_kln_eing = diad_AE.pitch_string

rhythm_definition.notes = [
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 5
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 9
        ("r1"),
        ("r1"),
        ("r1"),
        ("r4"),
        (melody_a_oct_down[0], abjad.Duration(3, 4), rill.tie(), clef('bass')),
        #------------Bar 13
        (melody_a_oct_down[0], abjad.Duration(1, 8)),
        ("r8"),
        (melody_a[0], abjad.Duration(2, 4)), 
        (melody_a_oct_down[1], abjad.Duration(1,4)), 
        (melody_a_oct_down[3], abjad.Duration(1)), 
        (melody_a_oct_down[2], abjad.Duration(1), tremolo(32), clef('treble')), 
        (cmin7_42_stages[0], abjad.Duration(1, 2), tremolo(32), rill.tie()),
        (cmin7_42_stages[1], abjad.Duration(1, 2), tremolo(32), rill.tie()),
        #------------Bar 17
        (cmin7_42_stages[1], abjad.Duration(1, 4), tremolo(32), rill.tie()),
        (cmin7_42_stages[2], abjad.Duration(3, 4), tremolo(32), rill.tie()),
        (cmin7_42_stages[3], abjad.Duration(1), tremolo(32), rill.tie()),
        (cmin7_42_stages[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        (cmin7_stages[0], abjad.Duration(1, 2), tremolo(32), rill.tie()),
        (cmin7_stages[1], abjad.Duration(1, 2), tremolo(32), rill.tie()),
        #------------Bar 21
        (cmin7_stages[1], abjad.Duration(1, 4), tremolo(32), rill.tie()),
        (cmin7_stages[2], abjad.Duration(3, 4), tremolo(32), rill.tie()),
        (cmin7_stages[3], abjad.Duration(1), tremolo(32), rill.tie()),
        (cmin7_stages[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        ("r1"),
        #-----------Bar 25
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 29
        ("r1"),
        (diad_DA_gr_kln, abjad.Duration(1), tremolo(32), rill.tie(), clef('bass')),
        (diad_DA_gr_kln, abjad.Duration(1), tremolo(32), rill.tie()),
        (diad_DA_gr_kln, abjad.Duration(1), tremolo(32), rill.tie()),
        #-----------Bar 33
        (diad_DA_gr_kln, abjad.Duration(1), tremolo(32), rill.tie()),
        (diad_DA_gr_kln, abjad.Duration(1), tremolo(32)),
        ("r1"),
        ("r1"),
        #-----------Bar 37
        (diad_AE_kln_eing, abjad.Duration(1), tremolo(32), rill.tie()),
        (diad_AE_kln_eing, abjad.Duration(1), tremolo(32), rill.tie()),
        (diad_AE_kln_eing, abjad.Duration(1), tremolo(32), rill.tie()),
        (diad_AE_kln_eing, abjad.Duration(1), tremolo(32), rill.tie()),
        #-----------Bar 41
        (diad_AE_kln_eing, abjad.Duration(1), tremolo(32)),
        ("r1"),
        ]

rhythm_definition.dynamics = [
        (12, abjad.Dynamic('ppp')),
        (18, '>'),
        (20, '<'),
        (23, '>'),
        (24, abjad.Dynamic('ppp')),
        (26, '<'),
        (29, '>'),
        (31, abjad.Dynamic('niente')),
        (39, abjad.Dynamic('niente')),
        (40, '<'),
        (42, '>'),
        (44, abjad.Dynamic('niente')),
        (46, abjad.Dynamic('niente')),
        (47, '<'),
        (49, '>', 3.5),
        (51, abjad.Dynamic('niente')),
       ]

rhythm_definition.markup = [
        (10, rill.markup.mx(), 1.5),
        ]


#-------------------PolySynth----------------#

#--------------/
# RH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'RH_I'

gmin7_6_zwgstrn = gm7_hrmns_zw_dr[0].segment
rh_arp_one = LegatoArpeggio(gmin7_6_zwgstrn, seq_one)
gmin7_6_stages = rh_arp_one.stages

gmin7_64 = gm7_hrmns_zw_dr[1].segment
rh_arp_two = LegatoArpeggio(gmin7_64, seq_two)
gmin7_64_stages = rh_arp_two.stages

rhythm_definition.notes = [
        ("r1"),
        ("r2"),
        (gmin7_6_stages[0], abjad.Duration(1, 2), rill.tie()),
        (gmin7_6_stages[1], abjad.Duration(3, 4), rill.tie()),
        (gmin7_6_stages[2], abjad.Duration(1, 4), rill.tie()),
        (gmin7_6_stages[2], abjad.Duration(2, 4), rill.tie()),
        (gmin7_6_stages[3], abjad.Duration(2, 4), rill.tie()),
        (gmin7_6_stages[3], abjad.Duration(1), rill.tie()), 
        # ------------------------------------------ Bar 6
        (gmin7_64_stages[2], abjad.Duration(1), rill.tie()),
        (gmin7_64_stages[2], abjad.Duration(1,2), rill.tie()),
        (gmin7_64_stages[3], abjad.Duration(1,2), rill.tie()),
        (gmin7_64_stages[3], abjad.Duration(1), rill.tie()),
        #------------Bar 9
        (gmin7_64_stages[3], abjad.Duration(1, 4), rill.tie()),
        (gmin7_64_stages[1], abjad.Duration(3, 4), rill.tie()),
        (gmin7_64_stages[0], abjad.Duration(1), rill.tie()),
        (gmin7_64_stages[0], abjad.Duration(1), rill.tie()),
        (gmin7_64_stages[0], abjad.Duration(1)),
        #------------Bar 13
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 17
        ("r1"),
        ("r1"),
        ("r1"),       
        ("r1"),
        #------------Bar 21
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 25
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 29
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 33
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 37
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 41
        ("r1"),
        ("r1"),
        ]


rhythm_definition.dynamics = [ 
                    (0, abjad.Dynamic('ppp'), 2.5)
                       ]

rhythm_definition.markup = []


#--------------/
# LH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'LH_I'

cmin7_6_kln = cm7_hrmns_kln_eing[0].segment
lh_arp_one = LegatoArpeggio(cmin7_6_kln, seq_one)
cmin7_6_stages = lh_arp_one.stages


d7_9 = d7_hrmns_gr_kln[0].segment
lh_arp_two = LegatoArpeggio(d7_9, seq_three)
d7_9_stages = lh_arp_two.stages

d7_6 = d7_hrmns_gr_kln[1].segment
lh_arp_three = LegatoArpeggio(d7_6, seq_three)
d7_6_stages = lh_arp_three.stages

rhythm_definition.notes = [
        (cmin7_6_stages[0], abjad.Duration(1, 2), rill.tie()),
        (cmin7_6_stages[1], abjad.Duration(1, 2), rill.tie()),
        (cmin7_6_stages[1], abjad.Duration(1, 4), rill.tie()),
        (cmin7_6_stages[2], abjad.Duration(3, 4), rill.tie()),
        (cmin7_6_stages[3], abjad.Duration(1), rill.tie()),
        (cmin7_6_stages[3], abjad.Duration(3, 4)), 
        ("r4"),
        # ------------------------------------------ Bar 5
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 9
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 13
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #------------Bar 17
        ("r1"),
        ("r1"),
        ("r1"),       
        ("r1"),
        #------------Bar 21
        ("r1"),
        ("r2"),
        (d7_9_stages[0], abjad.Duration(1, 2), rill.tie()),
        (d7_9_stages[1], abjad.Duration(3, 4), rill.tie()),
        (d7_9_stages[2], abjad.Duration(1, 4), rill.tie()),
        (d7_9_stages[2], abjad.Duration(2, 4), rill.tie()),
        (d7_9_stages[3], abjad.Duration(2, 4), rill.tie()),
        #------------ Bar 25
        (d7_9_stages[3], abjad.Duration(1), rill.tie()), 
        (d7_6_stages[3], abjad.Duration(1), rill.tie()),
        (d7_6_stages[3], abjad.Duration(1,2), rill.tie()),
        (d7_6_stages[2], abjad.Duration(1,2), rill.tie()),
        (d7_6_stages[2], abjad.Duration(1), rill.tie()),
        #------------Bar 29
        (d7_6_stages[2], abjad.Duration(1, 4), rill.tie()),
        (d7_6_stages[1], abjad.Duration(3, 4), rill.tie()),
        (d7_6_stages[0], abjad.Duration(1)),
        ("r1"),  
        ("r1"),
        #-----------Bar 33
        (diad_DA_gr_kln, abjad.Duration(1), rill.tie()),
        (diad_DA_gr_kln, abjad.Duration(1), rill.tie()),
        (diad_DA_gr_kln, abjad.Duration(1), rill.tie()),
        (diad_DA_gr_kln, abjad.Duration(1), rill.tie()),
        #-----------Bar 37
        (diad_DA_gr_kln, abjad.Duration(1)),
        ("r1"),
        ("r1"),
        (diad_AE_kln_eing, abjad.Duration(1), rill.tie()),
        #-----------Bar 41
        (diad_AE_kln_eing, abjad.Duration(1), rill.tie()),
        (diad_AE_kln_eing, abjad.Duration(1), barline("||")),
        ]


rhythm_definition.dynamics = []

rhythm_definition.markup = []

# ---------------------------------------RUN SEGMENT

lilypond_file = segment_maker.run()
