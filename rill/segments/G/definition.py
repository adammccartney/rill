import abjad
import rill


###########
### [G] ###
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
                                      segment_name='G',
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
