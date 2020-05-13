import abjad 
from abjadext import *

# Talea rhythmMaker test
#
#stack = rmakers.stack(
#        rmakers.talea([1, 2, 3, -4], 16),
#        rmakers.beam(),
#        rmakers.extract_trivial(),
#        )
#divisions = [(3, 8), (4, 8), (3, 8), (4, 8)]
#selection = stack(divisions)
#lilypond_file = abjad.LilyPondFile.rhythm(
#        selection, divisions
#        )
#abjad.show(lilypond_file) # doctest: +SKIP
#
## Note RhythmMaker test
#
#
#stack = rmakers.stack(
#        rmakers.note(),
#        rmakers.force_rest(
#        abjad.select().logical_ties().get([0], 2),
#        ),
#        )
#divisions = [(4, 8), (3, 8), (4, 8), (3, 8)]
#selection = stack(divisions)
#lilypond_file = abjad.LilyPondFile.rhythm(
#        selection, divisions
#        )
#abjad.show(lilypond_file) # doctest: +SKIP


# To set up a simple score: 




staff_1 = abjad.Staff("c'1 d'1 f'1 e'1")
staff_2 = abjad.Staff("e''1 f''1 a''1 g''1")
staves = [staff_2, staff_1]

score = abjad.Score(staves[:]) 
lilypond_file = abjad.LilyPondFile.new(score)
lilypond_file.header_block.title = abjad.Markup('Theme from Jupiter')
lilypond_file.header_block.composer = abjad.Markup('Mozart')
lilypond_file.layout_block.indent = 0
lilypond_file.paper_block.top_margin = 15
lilypond_file.paper_block.left_margin = 15
abjad.show(lilypond_file)
