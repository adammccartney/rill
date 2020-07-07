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



