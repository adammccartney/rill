import abjad

from rill.materials.instruments.markups import instrument as instrument
from rill.materials.instruments.markups import short_instrument as short_instrument

instruments = abjad.OrderedDict(
    [
        (
            "Violin",
            abjad.Violin(
                markup=instrument("Violin"),
                short_markup=short_instrument("vln"),
            ),
        ),
        (
            "Monosynth",
            abjad.ClarinetInBFlat(
                markup=instrument("MonoSynth"),
                short_markup=short_instrument("msy"),
            ),
        ),
        (
            "Polysynth",
            abjad.Piano(
                markup=instrument("PolySynth"),
                short_markup=short_instrument("psy"),
            ),
        ),
        ]
)

if __name__ == '__main__':
    for key, item in instruments.items():
        print(key, item)


