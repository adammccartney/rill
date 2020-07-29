import pathlib
import abjad
import rill


###########
### [F] ###
###########


this_current_directory =  pathlib.Path(__file__).parent 
test_build_path = rill.build_path 
score = rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _phrase_outflows=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=test_build_path,
                                segment_name='segment_F',
                                tempo=((1, 4), 50),
                                time_signatures=([(4, 4)] * 20),
                                )


#-----------------/________________________
# Pitch Material /  Constants for section /
#_______________/------------------------/

bD7_x = rill.tetrads['e_v']
bD7_6 = rill.invert_up(bD7_x, 1)
bD7_64 = rill.invert_up(bD7_x, 2)
bD7_42 = rill.invert_up(bD7_x, 3)

b7_x = rill.FuzzyHarmony('e_v', bD7_x) # emin7
b7_6 = rill.FuzzyHarmony('e_v', bD7_6) 
b7_64 = rill.FuzzyHarmony('e_v', bD7_64)   
b7_42 = rill.FuzzyHarmony('e_v', bD7_42)

csj7 = rill.tetrads['cs_i']
csj7_6 = rill.invert_up(csj7, 1)
csj7_64 = rill.invert_up(csj7, 2)
csj7_42 = rill.invert_up(csj7, 3)

cs7 = rill.FuzzyHarmony('cs_i', csj7)
cs7_6 = rill.FuzzyHarmony('cs_i', csj7_6) 
cs7_64 = rill.FuzzyHarmony('cs_i', csj7_64)   
cs7_42 = rill.FuzzyHarmony('cs_i', csj7_42)

""" 
    Make harmonies and fifth offsets in all octaves
    Note: octave names are in german:
    gross, klein, 
    ein-, zwei-, dreigestr = ein,- zwei-, dreigestrichen
    """

auth_one_ein_zw = [b7_x, b7_6, b7_64, b7_42]
auth_one_gr = rill.transpose(auth_one_ein_zw, -24)
auth_one_kl_eing = rill.transpose(auth_one_ein_zw, -12)

plag_one_zw_dr = rill.transpose(auth_one_ein_zw, 19)
plag_one_ein_zw = rill.transpose(auth_one_ein_zw, 7)
plag_one_gr = rill.transpose(auth_one_ein_zw, -17)

auth_two_ein_zw = [cs7, cs7_6, cs7_64, csj7_42]

auth_two_gr_kln = rill.transpose(auth_two_ein_zw, -24)
auth_two_kln_eing = rill.transpose(auth_two_ein_zw, -12)
auth_two_zw_dr = rill.transpose(auth_two_ein_zw, 12)

plag_two_ein_zw = rill.transpose(auth_two_ein_zw, 7)
plag_two_zw_dr = rill.transpose(auth_two_ein_zw, 19)

#--------------/
#   Violin    /
#____________/

# Melody One 

mel_one_a = rill.melody_lookup['em'][4]
mel_one_b = rill.melody_lookup['em'][5]

mel_one_a_oct_down = transpose_segment(mel_one_a, -12)
mel_one_a_oct_up = transpose_segment(mel_one_a, 12)

mel_one_a_arp = LegatoArpeggio(mel_one_a, m_seq_a)
mel_one_a_arp_oct_up = LegatoArpeggio(mel_one_a_oct_up, m_seq_a)
mel_one_a_arp_oct_down = LegatoArpeggio(mel_one_a_oct_down, m_seq_a)

melody_one_a = mel_one_a_arp.pitches
melody_one_a_oct_up = mel_one_a_arp_oct_up.pitches
melody_one_a_oct_down = mel_one_a_arp_oct_down.pitches

# Violin Arpeggio One

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

plag_two_a = gm7_hrmns_ein_zw[0].segment
vln_arp_one = LegatoArpeggio(plag_two_a, seq_one)
violin_arp_one = vln_arp_one.pitches

m_seq_a = (0, 1, 2, 3)

# Violin Arpeggio Two

auth_one_c = cm7_hrmns_ein_zw[2].segment
tr_arp_one = LegatoArpeggio(auth_one_c, seq_one)
violin_arp_two = tr_arp_one.pitches 

auth_one_d = cm7_hrmns_ein_zw[3].segment
tr_arp_two = LegatoArpeggio(auth_one_d, seq_one)
violin_arp_three = tr_arp_two.pitches

plag_two_a = d7_hrmns_zw_dr[0].segment
vln_arp_two = LegatoArpeggio(plag_two_a, seq_three)
violin_arp_four = vln_arp_two.pitches

# Melody Two 

mel_two_a = rill.melody_lookup['gm'][3]
mel_two_b = rill.melody_lookup['gm'][4]
mel_two_c = rill.melody_lookup['gm'][5]

mel_two_a_arp = LegatoArpeggio(mel_two_a, m_seq_a)  
mel_two_b_arp = LegatoArpeggio(mel_two_b, m_seq_a)
mel_two_c_arp = LegatoArpeggio(mel_two_c, m_seq_a)

melody_two_a = mel_two_a_arp.pitches
melody_two_b = mel_two_b_arp.pitches
melody_two_c = mel_two_c_arp.pitches

#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Monosynth'

auth_one_c = cm7_hrmns_kln_eing[2].segment
tr_arp_one = LegatoArpeggio(auth_one_c, seq_one)
monosynth_arp_one = tr_arp_one.stages 

cmin7_kln = cm7_hrmns_kln_eing[3].segment
tr_arp_two = LegatoArpeggio(cmin7_kln, seq_one)
monosynth_arp_two = tr_arp_two.stages 

diad_DA = Diad(d7_fifths_gr_kln[1])
diad_one = diad_DA.pitch_string

diad_AE = Diad(d7_fifths_kln_eing[0])
diad_two = diad_AE.pitch_string

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
        (melody_one_a_oct_down[0], abjad.Duration(3, 4), rill.tie(), clef('bass')),
        #------------Bar 13
        (melody_one_a_oct_down[0], abjad.Duration(1, 8)),
        ("r8"),
        (melody_one_a[0], abjad.Duration(2, 4)), 
        (melody_one_a_oct_down[1], abjad.Duration(1,4)), 
        (melody_one_a_oct_down[3], abjad.Duration(1)), 
        (melody_one_a_oct_down[2], abjad.Duration(1), tremolo(32), clef('treble')), 
        (monosynth_arp_one[0], abjad.Duration(1, 2), tremolo(32), rill.tie()),
        (monosynth_arp_one[1], abjad.Duration(1, 2), tremolo(32), rill.tie()),
        #------------Bar 17
        (monosynth_arp_one[1], abjad.Duration(1, 4), tremolo(32), rill.tie()),
        (monosynth_arp_one[2], abjad.Duration(3, 4), tremolo(32), rill.tie()),
        (monosynth_arp_one[3], abjad.Duration(1), tremolo(32), rill.tie()),
        (monosynth_arp_one[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        (monosynth_arp_two[0], abjad.Duration(1, 2), tremolo(32), rill.tie()),
        (monosynth_arp_two[1], abjad.Duration(1, 2), tremolo(32), rill.tie()),
        #------------Bar 21
        (monosynth_arp_two[1], abjad.Duration(1, 4), tremolo(32), rill.tie()),
        (monosynth_arp_two[2], abjad.Duration(3, 4), tremolo(32), rill.tie()),
        (monosynth_arp_two[3], abjad.Duration(1), tremolo(32), rill.tie()),
        (monosynth_arp_two[3], abjad.Duration(3, 4), tremolo(32)), 
        ("r4"),
        ("r1"),
        #-----------Bar 25
        ("r1"),
        ("r1"),
        ("r1"),
        ("r1"),
        #-----------Bar 29
        ("r1"),
        (diad_one, abjad.Duration(1), tremolo(32), rill.tie(), clef('bass')),
        (diad_one, abjad.Duration(1), tremolo(32), rill.tie()),
        (diad_one, abjad.Duration(1), tremolo(32), rill.tie()),
        #-----------Bar 33
        (diad_one, abjad.Duration(1), tremolo(32), rill.tie()),
        (diad_one, abjad.Duration(1), tremolo(32)),
        ("r1"),
        ("r1"),
        #-----------Bar 37
        (diad_two, abjad.Duration(1), tremolo(32), rill.tie()),
        (diad_two, abjad.Duration(1), tremolo(32), rill.tie()),
        (diad_two, abjad.Duration(1), tremolo(32), rill.tie()),
        (diad_two, abjad.Duration(1), tremolo(32), rill.tie()),
        #-----------Bar 41
        (diad_two, abjad.Duration(1), tremolo(32)),
        ("r1"),
        ("r1"),
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
        (18, rill.markup.mx(), 1.5),
        ]


#-------------------PolySynth----------------#

#--------------/
# RH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'RH_I'

gmin7_6_zwgstrn = gm7_hrmns_zw_dr[0].segment
gmin7_6_arp = LegatoArpeggio(gmin7_6_zwgstrn, seq_one)
rh_arp_one = gmin7_6_arp.stages

gmin7_64 = gm7_hrmns_zw_dr[1].segment
gmin7_64_arp = LegatoArpeggio(gmin7_64, seq_two)
rh_arp_two = gmin7_64_arp.stages

rhythm_definition.notes = [
        ("r1"),
        ("r2"),
        (rh_arp_one[0], abjad.Duration(1, 2), rill.tie()),
        (rh_arp_one[1], abjad.Duration(3, 4), rill.tie()),
        (rh_arp_one[2], abjad.Duration(1, 4), rill.tie()),
        (rh_arp_one[2], abjad.Duration(2, 4), rill.tie()),
        (rh_arp_one[3], abjad.Duration(2, 4), rill.tie()),
        (rh_arp_one[3], abjad.Duration(1), rill.tie()), 
        # ------------------------------------------ Bar 6
        (rh_arp_two[2], abjad.Duration(1), rill.tie()),
        (rh_arp_two[2], abjad.Duration(1,2), rill.tie()),
        (rh_arp_two[3], abjad.Duration(1,2), rill.tie()),
        (rh_arp_two[3], abjad.Duration(1), rill.tie()),
        #------------Bar 9
        (rh_arp_two[3], abjad.Duration(1, 4), rill.tie()),
        (rh_arp_two[1], abjad.Duration(3, 4), rill.tie()),
        (rh_arp_two[0], abjad.Duration(1), rill.tie()),
        (rh_arp_two[0], abjad.Duration(1), rill.tie()),
        (rh_arp_two[0], abjad.Duration(1)),
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
cmin7_6_arp= LegatoArpeggio(cmin7_6_kln, seq_one)
lh_arp_one = cmin7_6_arp.stages

d7_9 = d7_hrmns_gr_kln[0].segment
d7_9_arp = LegatoArpeggio(d7_9, seq_three)
lh_arp_two = d7_9_arp.stages

d7_6 = d7_hrmns_gr_kln[1].segment
d7_6_arp = LegatoArpeggio(d7_6, seq_three)
lh_arp_three = d7_6_arp.stages


rhythm_definition.notes = [
        (lh_arp_one[0], abjad.Duration(1, 2), rill.tie()),
        (lh_arp_one[1], abjad.Duration(1, 2), rill.tie()),
        (lh_arp_one[1], abjad.Duration(1, 4), rill.tie()),
        (lh_arp_one[2], abjad.Duration(3, 4), rill.tie()),
        (lh_arp_one[3], abjad.Duration(1), rill.tie()),
        (lh_arp_one[3], abjad.Duration(3, 4)), 
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
        (lh_arp_two[0], abjad.Duration(1, 2), rill.tie()),
        (lh_arp_two[1], abjad.Duration(3, 4), rill.tie()),
        (lh_arp_two[2], abjad.Duration(1, 4), rill.tie()),
        (lh_arp_two[2], abjad.Duration(2, 4), rill.tie()),
        (lh_arp_two[3], abjad.Duration(2, 4), rill.tie()),
        #------------ Bar 25
        (lh_arp_two[3], abjad.Duration(1), rill.tie()), 
        (lh_arp_three[3], abjad.Duration(1), rill.tie()),
        (lh_arp_three[3], abjad.Duration(1,2), rill.tie()),
        (lh_arp_three[2], abjad.Duration(1,2), rill.tie()),
        (lh_arp_three[2], abjad.Duration(1), rill.tie()),
        #------------Bar 29
        (lh_arp_three[2], abjad.Duration(1, 4), rill.tie()),
        (lh_arp_three[1], abjad.Duration(3, 4), rill.tie()),
        (lh_arp_three[0], abjad.Duration(1)),
        ("r1"),  
        ("r1"),
        #-----------Bar 33
        (diad_one, abjad.Duration(1), rill.tie()),
        (diad_one, abjad.Duration(1), rill.tie()),
        (diad_one, abjad.Duration(1), rill.tie()),
        (diad_one, abjad.Duration(1), rill.tie()),
        #-----------Bar 37
        (diad_one, abjad.Duration(1)),
        ("r1"),
        ("r1"),
        (diad_two, abjad.Duration(1), rill.tie()),
        #-----------Bar 41
        (diad_two, abjad.Duration(1), rill.tie()),
        (diad_two, abjad.Duration(1), rill.tie()), 
        (diad_two, abjad.Duration(1), rill.tie()),
        (diad_two, abjad.Duration(1), barline("||")),
        ]


rhythm_definition.dynamics = [
        (47, abjad.Dynamic('pp')),
        (48, '>'),
        (51, abjad.Dynamic('niente')),
        ]

rhythm_definition.markup = []

# ------------ run and build segment
lilypond_file = segment_maker.run()
