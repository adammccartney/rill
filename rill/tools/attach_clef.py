import abjad

def attach_clef(clef):
    """
    Makes a clef before a specific leaf
    """
    if isinstance(clef, abjad.Clef):
        return abjad.LilyPondLiteral(f"{format(clef, 'lilypond')}", "before")


                
if __name__ == '__main__':
    clef = attach_clef(abjad.Clef('bass'))
    abjad.f(clef)
