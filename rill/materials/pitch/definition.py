import abjad

#--------------------------------
#   bf_ii |  bf_ii7             |
#   g_v   |  g_V7b913           |
#   e_i   |  e_i9               |
#   cs_ii |  cs_ii7             |
#   bf_v  |  bf_V7b9            |
#   g_i   |  g_iAlt/7           |
#   e_ii  |  e_ii7              |
#   cs_v  |  cs_V7b913          |
#   bf_i  |  bf_I9              |
#   g_ii  |  g_ii7              |
#   e_v   |  e_V7b913           |
#   cs_i  |  cs_I9              |
#-------------------------------


bass_pitches = abjad.PitchSegment("c d e ds f fs fs gs bf a b cs")

#A container holding all harmonies used in the piece 
tetrads = abjad.OrderedDict([ 
            ('bf_ii', abjad.PitchSegment("ef' g' bf' c''")),       # cmin7 
            ('g_v', abjad.PitchSegment("ef' fs' a' d''")),     # D7(b9,13)
            ('e_i', abjad.PitchSegment("e' g' b' d''")),           # emin9
            ('cs_ii', abjad.PitchSegment("fs' as' cs'' ds''")),   # dsmin9
            ('bf_v', abjad.PitchSegment("fs' a' c' ef''")),      # F7(b9)
            ('g_i', abjad.PitchSegment("fs' gs' as' cs'")),   # gminb9+/+7 
            ('e_ii', abjad.PitchSegment("e' fs' a' cs''")),       # fsmin7
            ('cs_v', abjad.PitchSegment("ds' fs' a' d''")),   # gsb913
            ('bf_i', abjad.PitchSegment("c' f' a' d''")),         # bfM9
            ('g_ii', abjad.PitchSegment("c' e' g' a'")),           # amin7
            ('e_v', abjad.PitchSegment("d' ef' fs' a'")),      # b7b913
            ('cs_i', abjad.PitchSegment("ds' f' gs' bs'")),
            ])


transposition_lookup = {
        """Nested dict that can be used as part
           material_methods.transpose method
           
           Spelling is a bit idiosyncratic and favours diads where possible
           e.g: bf - cs, bf - fs also tries to keep the double flats and sharps
           to a minimum
           """
        0: { # P1 
            "bf_ii": "bf_ii",
            "g_v": "g_v",
            "e_i": "e_i",
            "cs_ii": "cs_ii",
            "bf_v": "bf_v",
            "g_i": "g_i",
            "e_ii": "e_ii",
            "cs_v": "cs_v",
            "bf_i": "bf_i",
            "g_ii": "g_ii",
            "e_v": "e_v",
            "cs_i": "cs_i",
            }, 
        1: { # m2 
            "bf_ii": "b_ii",
            "g_v": "gs_v",
            "e_i": "f_i",
            "cs_ii": "d_ii",
            "bf_v": "b_v",
            "g_i": "gs_i",
            "e_ii": "f_ii",
            "cs_v": "d_v",
            "bf_i": "b_i",
            "g_ii": "gs_ii",
            "e_v": "f_v",
            "cs_i": "d_i",
            },   
        2: { # M2 
            "bf_ii": "c_ii",
            "g_v": "a_v",
            "e_i": "fs_i",
            "cs_ii": "ds_ii",
            "bf_v": "c_v",
            "g_i": "a_i",
            "e_ii": "fs_ii",
            "cs_v": "ds_v",
            "bf_i": "c_i",
            "g_ii": "a_ii",
            "e_v": "fs_v",
            "cs_i": "ds_i",
            },   
       3: { # m3 
            "bf_ii": "cs_ii",
            "g_v": "bf_v",
            "e_i": "g_i",
            "cs_ii": "e_ii",
            "bf_v": "cs_v",
            "g_i": "bf_i",
            "e_ii": "g_ii",
            "cs_v": "e_v",
            "bf_i": "cs_i",
            "g_ii": "bf_ii",
            "e_v": "g_v",
            "cs_i": "e_i",
            },   
        4: { # M3 
            "bf_ii": "d_ii",
            "g_v": "b_v",
            "e_i": "gs_i",
            "cs_ii": "f_ii",
            "bf_v": "d_v",
            "g_i": "b_i",
            "e_ii": "gs_ii",
            "cs_v": "f_v",
            "bf_i": "d_i",
            "g_ii": "b_ii",
            "e_v": "gs_v",
            "cs_i": "f_i",
            },
        5: { # P4 
            "bf_ii": "ef_ii",
            "g_v": "c_v",
            "e_i": "a_i",
            "cs_ii": "fs_ii",
            "bf_v": "ef_v",
            "g_i": "c_i",
            "e_ii": "a_ii",
            "cs_v": "fs_v",
            "bf_i": "ef_i",
            "g_ii": "c_ii",
            "e_v": "a_v",
            "cs_i": "fs_i",
            },
        6: { # tritone
            "bf_ii": "e_ii",
            "g_v": "cs_v",
            "e_i": "bf_i",
            "cs_ii": "g_ii",
            "bf_v": "e_v",
            "g_i": "cs_i",
            "e_ii": "bf_ii",
            "cs_v": "g_v",
            "bf_i": "e_i",
            "g_ii": "cs_ii",
            "e_v": "bf_v",
            "cs_i": "g_i",
            },
        7: { # P5
            "bf_ii": "f_ii",
            "g_v": "d_v",
            "e_i": "b_i",
            "cs_ii": "gs_ii",
            "bf_v": "f_v",
            "g_i": "d_i",
            "e_ii": "b_ii",
            "cs_v": "gs_v",
            "bf_i": "f_i",
            "g_ii": "d_ii",
            "e_v": "b_v",
            "cs_i": "gs_i",
            },
        8: { # m 6
            "bf_ii": "fs_ii",
            "g_v": "ef_v",
            "e_i": "c_i",
            "cs_ii": "a_ii",
            "bf_v": "fs_v",
            "g_i": "ef_i",
            "e_ii": "c_ii",
            "cs_v": "a_v",
            "bf_i": "fs_i",
            "g_ii": "ef_ii",
            "e_v": "c_v",
            "cs_i": "a_i",
            },
        9: { # M6
            "bf_ii": "g_ii",
            "g_v": "e_v",
            "e_i": "cs_i",
            "cs_ii": "bf_ii",
            "bf_v": "g_v",
            "g_i": "e_i",
            "e_ii": "cs_ii",
            "cs_v": "bf_v",
            "bf_i": "g_i",
            "g_ii": "e_ii",
            "e_v": "cs_v",
            "cs_i": "bf_i",
            },
        10: { # m7
            "bf_ii": "af_ii",
            "g_v": "f_v",
            "e_i": "d_i",
            "cs_ii": "b_ii",
            "bf_v": "af_v",
            "g_i": "f_i",
            "e_ii": "d_ii",
            "cs_v": "b_v",
            "bf_i": "af_i",
            "g_ii": "f_ii",
            "e_v": "d_v",
            "cs_i": "b_i",
            },
        11: { # M7
            "bf_ii": "a_ii",
            "g_v": "fs_v",
            "e_i": "ds_i",
            "cs_ii": "c_ii",
            "bf_v": "a_v",
            "g_i": "fs_i",
            "e_ii": "ds_ii",
            "cs_v": "c_v",
            "bf_i": "a_i",
            "g_ii": "fs_ii",
            "e_v": "ds_v",
            "cs_i": "c_i",
            },
        12: { # P8
            "bf_ii": "bf_ii",
            "g_v": "g_v",
            "e_i": "e_i",
            "cs_ii": "cs_ii",
            "bf_v": "bf_v",
            "g_i": "g_i",
            "e_ii": "e_ii",
            "cs_v": "cs_v",
            "bf_i": "bf_i",
            "g_ii": "g_ii",
            "e_v": "e_v",
            "cs_i": "cs_i",
            }
        }



