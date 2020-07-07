import abjad
import rill

template = rill.ScoreTemplate()
path = abjad.Path('rill', 'stylesheets', 'contexts.ily')
lilypond_file = template.__illustrate__(
                                        global_staff_size=14,
                                        includes=[path],
                                        )
score = template()
#print(format(score))
#abjad.show(lilypond_file) # doctest: +SKIP
print(template.voice_abbreviations)
abjad.f(lilypond_file[abjad.Score], strict=89)
