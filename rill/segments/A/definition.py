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

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _phrase_outflows=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=test_build_path,
                                markup_leaves=False,
                                segment_name='A',
                                tempo=((1, 4), 50),
                                time_signatures=([(4, 4)] * 24),
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

cm7_hrmns_eingestr = [cm7_6, cm7_64, cm7_42, cm7]

empty_list: List[any] = []

cm7_hrmns_klein = rill.transpose(cm7_hrmns_eingestr, empty_list, -12)
gm7_hrmns_zweigestr = rill.transpose(cm7_hrmns_eingestr, empty_list, 19)


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
        (0, abjad.Dynamic('ppp'), 2.5),
        (0, '-|'),
        (3, abjad.Dynamic('mf')),
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

gmin7_6_zwgstrn = gm7_hrmns_zweigestr[0].segment
rh_arp_one = LegatoArpeggio(gmin7_6_zwgstrn, seq_one)
gmin7_6_stages = rh_arp_one.stages

gmin7_64 = gm7_hrmns_zweigestr[1].segment

rhythm_definition.notes = [
        ("r1"),
        ("r2"),
        (gmin7_6_stages[0], abjad.Duration(1, 2), rill.tie()),
        (gmin7_6_stages[1], abjad.Duration(3, 4), rill.tie()),
        (gmin7_6_stages[2], abjad.Duration(1, 4), rill.tie()),
        (gmin7_6_stages[2], abjad.Duration(2, 4), rill.tie()),
        (gmin7_6_stages[3], abjad.Duration(2, 4), rill.tie()),
        (gmin7_6_stages[3], abjad.Duration(1)), 
        # ------------------------------------------ Bar 6
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


#--------------/
# LH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'LH_I'

cmin7_6_kln = cm7_hrmns_klein[0].segment
lh_arp_one = LegatoArpeggio(cmin7_6_kln, seq_one)
cmin7_6_stages = lh_arp_one.stages

rhythm_definition.notes = [
        (cmin7_6_stages[0], abjad.Duration(1, 2), rill.tie()),
        (cmin7_6_stages[1], abjad.Duration(1, 2), rill.tie()),
        (cmin7_6_stages[1], abjad.Duration(1, 4), rill.tie()),
        (cmin7_6_stages[2], abjad.Duration(3, 4), rill.tie()),
        (cmin7_6_stages[3], abjad.Duration(1), rill.tie()),
        (cmin7_6_stages[3], abjad.Duration(1, 2)), 
        ("r2"),
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
