import abjad


class OverrideMaker(object):
    "An abstract override-making class"

    def __init__(self, style=''):
        self.style = style

    def __call__(self, music):
        assert False, "maker must be defined"




class NoteHeadOverrideMaker(OverrideMaker):
    "Changes the style of notehead"

    def __init__(self, style):
        self.notehead_types = [
            'default',
            'mensural',
            'petrucci',
            'neomensural',
            'mensural',
            'harmonic',
            'harmonic-black',
            'harmonic-mixed',
            'cross',
            'xcircle',
            'slash',
        ]
        OverrideMaker.__init__(self, style)

    def __call__(self, music):
        selection = abjad.select(music[:]).leaves(pitched=True)
        if self.style in self.notehead_types:
            for leaf in selection:
                abjad.override(leaf).note_head.style = self.style
            else:
                ValueError(self.style, "is not a valid note head style")

if __name__ == '__main__':
    staff = abjad.Staff("c'4 d'4 f'2 e'1")

    once_override_maker = NoteHeadOverrideMaker('harmonic')
    harmonic_override = once_override_maker(staff)

    abjad.f(staff)
