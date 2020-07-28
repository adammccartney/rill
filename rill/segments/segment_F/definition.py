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
                                segment_name='F',
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
