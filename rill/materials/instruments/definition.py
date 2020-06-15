import abjad
import mccartney

instruments = abjad.OrderedDict(
    [
        (
            "Violin",
            abjad.Violin(
                markup=mccartney.markups.instrument("Violin"),
                short_markup=mccartney.markups.short_instrument("vln"),
            ),
        ),
        (
            "MonoSynth",
            abjad.ClarinetInBFlat(
                markup=mccartney.markups.instrument("MonoSynth"),
                short_markup=mccartney.markups.short_instrument("msy"),
            ),
        ),
        (
            "PolySynth",
            abjad.Piano(
                markup=mccartney.markups.instrument("PolySynth"),
                short_markup=mccartney.markups.short_instrument("psy"),
            ),
        ),
        ]
)

if __name__ == '__main__':
    for key, item in instruments.items():
        print(key, item)


