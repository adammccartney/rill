import abjad

from rill.materials.instruments import markups as markups

instruments = abjad.OrderedDict(
    [
        (
            "Flute1",
            abjad.Flute(
                markup=markups.instrument("Flute1"),
                short_markup=markups.short_instrument("fl.1"),
                ),
            ),
        (
            "Flute2",
            abjad.Flute(
                markup=markups.instrument("Flute2"),
                short_markup=markups.short_instrument("fl.2"),
                ),
            ),
        (
            "Flute3",
            abjad.Flute(
                markup=markups.instrument("Flute3"),
                short_markup=markups.short_instrument("fl.3"),
                ),
            ),
        (
            "Flute4",
            abjad.Flute(
                markup=markups.instrument("Flute4"),
                short_markup=markups.short_instrument("fl.4"),
                ),
            ),
        (
            "Bbclarinet1",
            abjad.ClarinetInBFlat(
                markup=markups.instrument("Bb Clarinet1"),
                short_markup=markups.short_instrument("Bbcl.1"),
                ),
            ),
        (
            "Vibraphone",
            abjad.Percussion(
                markup=markups.instrument("Vibraphone"),
                short_markup=markups.short_instrument("vibes"),
                ),
            ),
        (
            "Violin1",
            abjad.Violin(
                markup=markups.instrument("Violin1"),
                short_markup=markups.short_instrument("vn.1"),
            ),
        ),
        (
            "Violin2",
            abjad.Violin(
                markup=markups.instrument("Violin2"),
                short_markup=markups.short_instrument("vn.2"),
            ),
        ),
        (
            "Violin3",
            abjad.Violin(
                markup=markups.instrument("Violin3"),
                short_markup=markups.short_instrument("vn.3"),
            ),
        ),
        (
            "Violin4",
            abjad.Violin(
                markup=markups.instrument("Violin4"),
                short_markup=markups.short_instrument("vn.4"),
            ),
        ),
        (
            "Violin5",
            abjad.Violin(
                markup=markups.instrument("Violin5"),
                short_markup=markups.short_instrument("vn.5"),
            ),
        ),
        (
            "Violin6",
            abjad.Violin(
                markup=markups.instrument("Violin6"),
                short_markup=markups.short_instrument("vn.6"),
            ),
        ),
        (
            "Violin7",
            abjad.Violin(
                markup=markups.instrument("Violin7"),
                short_markup=markups.short_instrument("vn.7"),
            ),
        ),
        (
            "Violin8",
            abjad.Violin(
                markup=markups.instrument("Violin8"),
                short_markup=markups.short_instrument("vn.8"),
            ),
        ),
        (
            "Viola",
            abjad.Viola(
                markup=markups.instrument("Viola"),
                short_markup=markups.short_instrument("va"),
            ),
        ),
        (
            "Cello",
            abjad.Viola(
                markup=markups.instrument("Cello"),
                short_markup=markups.short_instrument("vc"),
            ),
        ),
    ]
)

if __name__ == '__main__':

    print(f"number of instruments = {len(instruments)}")
    for key, item in instruments.items():
        print(key, item)
