import pathlib

import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmonyi

from rill.tools.FuzzyHarmony import LegatoArpeggio as LegatoArpeggio
from rill.tools.PhraseMaker import PhraseOutflow as PhraseOutflow
from rill.tools.PhraseMaker import PhraseStream as PhraseStream

from abjad import NamedPitch as NamedPitch
from typing import List
# call to segment maker contains:
    # Set instruments
    # Set voice names
    # set score_template
    # set time signatures
    # Set path for output
    # set tempo
    # set midi
    # 

#####################
# Setting up segment ### [A] ###
#####################

this_current_directory =  pathlib.Path(__file__).parent 
test_build_path = rill.build_path 
score = rill.ScoreTemplate()
score_template = score()

seg_t_signatures = (
                    [((4, 4)) * 10] + 
                    [(3, 4) * 4] +
                    [(5, 4) * 8] +
                    [(4, 4) * 9] +
                    [(3, 4) * 5] +
                    [(5, 4) * 8]
                    )

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _phrase_outflows=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=test_build_path,
                                markup_leaves=False,
                                segment_name='A',
                                tempo=((1, 4), 50),
                                time_signatures=(seg_t_signatures),
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


# ----- Diads

#cm7_diads = rill.make_diads(cm7_hrmns_gross, interval_doubling='d5')
#gm7_diads_zweigestr= rill.make_diads(gm7_hrmns_zweigestr, interval_doubling='d3')


# -- sequences of notes for arpeggios

seq_one = (1, 0, 3, 2)


#--------------/
#   Violin    /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'


gmin7_6_eingstrn = gm7_hrmns_ein_zw[0].segment
rh_arp_one = LegatoArpeggio(gmin7_6_eingstrn, seq_one)
gmin7_6_pitches = rh_arp_one.pitches

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
        (gmin7_6_pitches[2], abjad.Duration(1)),
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
        ("r1"),
        ("r1"),
        ("r1"),
        ]

rhythm_definition.dynamics = [
        (2, abjad.Dynamic('ppp'), 2.5),
        (3, '<'),
        (5, abjad.Dynamic('p'), 2.5),
        (6, '>'),
        (13, abjad.Dynamic('ppp')),
       ]

rhythm_definition.markup = [
        (0, rill.markup.tasto(), 1.5),
        ]


#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Monosynth'

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
        ("r1"),
        ("r1"),
        ("r1"),
        ]

rhythm_definition.dynamics = [
       ]

rhythm_definition.markup = [
        ]


#-------------------PolySynth----------------#


## Set up material for segment 

# Stream material into containers
#--------------/
# RH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'RH_I'

gmin7_6_zwgstrn = gm7_hrmns_zw_dr[0].segment
rh_arp_one = LegatoArpeggio(gmin7_6_zwgstrn, seq_one)
gmin7_6_stages = rh_arp_one.stages

seq_two = (3, 2, 0, 1)
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
        (gmin7_64_stages[0], abjad.Duration(1)),
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
lh_arp_one = LegatoArpeggio(cmin7_6_kln, seq_one)
cmin7_6_stages = lh_arp_one.stages

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
        ("r1"),
        ("r1"),
        ("r1"),
        ]


rhythm_definition.dynamics = []

rhythm_definition.markup = []

# ---------------------------------------RUN SEGMENT

lilypond_file = segment_maker.run()
