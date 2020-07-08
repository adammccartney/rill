import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.PhraseMaker import PhraseOutflow as PhraseOutflow
from rill.tools.PhraseMaker import PhraseStream as PhraseStream


#####################
# Setting up segment ### [B] ###
#####################

score_template = rill.ScoreTemplate()
score = score_template()

test_current_directory = rill.current_directory
test_build_path = rill.build_path 
score = rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                      _lilypond_file=None,
                                      _phrase_outflows=None,
                                      _score=score_template,
                                      current_directory=test_current_directory,
                                      build_path=test_build_path,
                                      segment_name='B',
                                      tempo=((1, 4), 50),
                                      time_signatures=([(4, 4)] * 20),
                                    )


#--------------/
#   Violin    /
#____________/


#-----------------/
#   MonoSynth    /
#_______________/


#-------------------PolySynth----------------#

#--------------/
# RH_Voice_I  /
#____________/

#---------------/
# RH_Voice_II  /
#_____________/

#--------------/
# LH_Voice_I  /
#____________/

#---------------/
# LH_Voice_II  /
#_____________/

#--------------------------------------------#mport abjad
