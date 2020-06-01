import abjad 
from abjadext import rmakers

# Talea rhythmMaker test

stack = rmakers.stack(
        rmakers.talea([1, 2, 3, -4], 16),
        rmakers.beam(),
        rmakers.extract_trivial(),
        )
divisions = [(3, 8), (4, 8), (3, 8), (4, 8)]
selection = stack(divisions)
lilypond_file = abjad.LilyPondFile.rhythm(
        selection, divisions
        )
abjad.show(lilypond_file) # doctest: +SKIP

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


# Sanity check in order to see some notes

#staff_1 = abjad.Staff("c'1 d'1 f'1 e'1")
#staff_2 = abjad.Staff("e''1 f''1 a''1 g''1")
#staves = [staff_2, staff_1]
#
#score = abjad.Score(staves[:]) 
#lilypond_file = abjad.LilyPondFile.new(score)
#lilypond_file.header_block.title = abjad.Markup('Theme from Jupiter')
#lilypond_file.header_block.composer = abjad.Markup('Mozart')
#lilypond_file.layout_block.indent = 0
#lilypond_file.paper_block.top_margin = 15
#lilypond_file.paper_block.left_margin = 15
#abjad.show(lilypond_file)

# Another examples of constructing rmakers

#stack = rmakers.stack(
#    rmakers.note(),
#    rmakers.force_rest(
#        abjad.select().logical_ties().get([0], 2),
#    ),
#)
#divisions = [(4, 4), (4, 4), (4, 4), (4, 4)]
#selection = stack(divisions)
#lilypond_file = abjad.LilyPondFile.rhythm(
#        selection, divisions
#)
#abjad.show(lilypond_file)
#abjad.f(lilypond_file[abjad.Score])


# Construct rmakers and use with measures in a voice
#
#
#maker1 = rmakers.TaleaRhythmMaker(
#  extra_counts_per_division=[0],
#    talea=rmakers.Talea(
#        counts=[3, 3, 4, 3, 3],
#        denominator=16,
#        ),
#    tuplet_specifier= rmakers.TupletSpecifier(
#        extract_trivial=True
#    )
#)
#divisions=[4 * (4, 4)]
#
#
#stack = rmakers.stack(
#        rmakers.talea([3, 3, 4, 3, 3], 16),
#        rmakers.beam(),
#        rmakers.extract_trivial(),
#        )
#divisions = [4 * (4, 4)]
#selection = stack(divisions)
#
#
#
#measures = abjad.Voice()
#
## Fill measures with Rests and attach TimeSignatures
#for pair in divisions:
#    multimeasure_rest = abjad.MultimeasureRest(1, multiplier=pair)
#    measures.append(abjad.Container([multimeasure_rest]))
#shards = abjad.mutate(measures[:]).split(divisions)
#for i, shard in enumerate(shards):
#    abjad.attach(abjad.TimeSignature(divisions[i]), shard[0][0])
#   
#
#selections = maker1(divisions)
#
## # Replace contents of measures with the RhythmMaker's contents
#
#for i, measure in enumerate(measures):
#    assert isinstance(selections[i], abjad.Selection), repr(selection)
#    assert isinstance(measure, abjad.Container), repr(measure)
#    abjad.mutate(measure[:]).replace(selections[i]) ## <-- here was the problem
#    abjad.attach(abjad.TimeSignature(divisions[i]), measure[0])
#
#   
#staff = abjad.Staff([measures])
#abjad.f(staff)
