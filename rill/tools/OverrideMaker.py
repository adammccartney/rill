import abjad


class OverrideMaker(object):
    "An abstract override-making class"

    def __init__(self, music):
        self.music = music

    def __call__(self, style):
        assert False, "maker must be defined"


class NoteHeadOverrideMaker(OverrideMaker):
    "Changes the style of notehead"

    def __init__(self, music=None):
        OverrideMaker.__init__(self, music)

    def __call__(self, style):
        selection = abjad.select(self.music[:]).leaves(pitched=True)
        for leaf in selection:
            abjad.override(leaf).note_head.style = style

if __name__ == '__main__':
    staff = abjad.Staff("c'4 d'4 f'2 e'1")

    once_override_maker = NoteHeadOverrideMaker(staff)
    harmonic_override = once_override_maker('harmonic')

    abjad.f(staff)
