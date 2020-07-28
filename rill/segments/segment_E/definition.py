import pathlib
import abjad
import rill


###########
### [E] ###
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
                                segment_name='segment_E',
                                tempo=((1, 4), 50),
                                time_signatures=([(4, 4)] * 20),
                                )


#-----------------/________________________
# Pitch Material /  Constants for section /
#_______________/------------------------/

bfM9_42 = rill.tetrads['bf_i']
bfM9_64 = rill.invert_up(bfM9_42, 1)
bfM9_7 = rill.invert_up(bfM9_42, 2)
bfM9_6 = rill.invert_up(bfM9_42, 3)

bf9_42 = rill.FuzzyHarmony('bf_v', bfM9_42) # emin7
bf9_64 = rill.FuzzyHarmony('bf_v', bfM9_64) 
bf9_7 = rill.FuzzyHarmony('bf_v', bfM9_7)   
bf9_6 = rill.FuzzyHarmony('bf_v', bfM9_6)

amin7_6 = rill.tetrads['g_ii']
amin7_64 = rill.invert_up(amin7_6, 1)
amin7_42 = rill.invert_up(amin7_6, 2)
amin7 = rill.invert_up(amin7_6, 3)

am7_6 = rill.FuzzyHarmony('g_ii', amin7_6)
am7_64 = rill.FuzzyHarmony('g_ii', amin7_64) 
am7_42 = rill.FuzzyHarmony('g_ii', amin7_42)   
am7 = rill.FuzzyHarmony('g_ii', amin7)

""" 
    Make harmonies and fifth offsets in all octaves
    Note: octave names are in german:
    gross, klein, 
    ein-, zwei-, dreigestr = ein,- zwei-, dreigestrichen
    """

auth_one_ein_zw = [bf9_42, bf9_64, bf9_7, bf9_6]
auth_one_gr = rill.transpose(auth_one_ein_zw, -24)
auth_one_kl_eing = rill.transpose(auth_one_ein_zw, -12)

plag_one_zw_dr = rill.transpose(auth_one_ein_zw, 19)
plag_one_ein_zw = rill.transpose(auth_one_ein_zw, 7)
plag_one_gr = rill.transpose(auth_one_ein_zw, -17)

auth_two_ein_zw = [am7_6, am7_64, am7_42, am7]

auth_two_gr_kln = rill.transpose(auth_two_ein_zw, -24)
auth_two_kln_eing = rill.transpose(auth_two_ein_zw, -12)
auth_two_zw_dr = rill.transpose(auth_two_ein_zw, 12)

plag_two_ein_zw = rill.transpose(auth_two_ein_zw, 7)
plag_two_zw_dr = rill.transpose(auth_two_ein_zw, 19)
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
