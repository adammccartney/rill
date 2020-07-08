import abjad 
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.PhraseMaker import PhraseOutflow as PhraseOutflow
from rill.tools.PhraseMaker import PhraseStream as PhraseStream


durations = [
        abjad.Duration(1, 2), 
        abjad.Duration(3, 4), 
        abjad.Duration(3, 4), 
        abjad.Duration(3, 2),
        abjad.Duration(1, 2),
        ]


harmony_one = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
harmony_two = FuzzyHarmony('bf_ii', abjad.PitchSegment("g' bf' c'' ef''"), 2) 

progression = [
      harmony_one,
      harmony_two,
      ]

harmonized_progression = rill.make_diads(progression)

dry_phrase_stream = PhraseStream()
wet_phrase_stream = rill.order_material(
                                  harmonized_progression,
                                  durations,
                                  dry_phrase_stream,
                                  )
containers = wet_phrase_stream.containers
print("containers from make_diads test: ", containers)


harmonies = [
      FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1),       # cmin7 
      FuzzyHarmony('g_v', abjad.PitchSegment("ef' fs' a' d''"), 1),     # D7(b9,13)
      FuzzyHarmony('e_i', abjad.PitchSegment("e' g' b' d''"), 0),           # emin9
      FuzzyHarmony('cs_ii', abjad.PitchSegment("fs' as' cs'' ds''"), 1),   # dsmin9
      FuzzyHarmony('bf_v', abjad.PitchSegment("fs' a' c' ef''"), 2),      # F7(b9)
      FuzzyHarmony('g_i', abjad.PitchSegment("fs' gs' as' cs'"), 3),   # gminb9+/+7 
      FuzzyHarmony('e_ii', abjad.PitchSegment("e' fs' a' cs''"), 0),       # fsmin7
      FuzzyHarmony('cs_v', abjad.PitchSegment("ds' fs' a' d''"), 0),   # gsb913
      FuzzyHarmony('bf_i', abjad.PitchSegment("c' f' a' d''"), 4),         # bfM9
      FuzzyHarmony('g_ii', abjad.PitchSegment("c' e' g' a'"), 1),           # amin7
      FuzzyHarmony('e_v', abjad.PitchSegment("d' ef' fs' a'"), 3),      # b7b913
      FuzzyHarmony('cs_i', abjad.PitchSegment("ds' f' gs' bs'"), 0),
      ]

transposed_harmonies = []
transposed = rill.transpose_up_fifth(harmonies, transposed_harmonies)
print("transposed: ", transposed)
