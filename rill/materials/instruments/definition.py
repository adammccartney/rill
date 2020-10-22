import abjad

from rill.materials.instruments import markups as markups

instruments = abjad.OrderedDict(
    [
        (
            "Flute 1",
            abjad.Flute(
                markup=markups.instrument("Flute 1"),
                short_markup=markups.short_instrument("fl.1"),
                ),
            ),
        (
            "Flute 2",
            abjad.Flute(
                markup=markups.instrument("Flute 2"),
                short_markup=markups.short_instrument("fl.2"),
                ),
            ),
        (
            "Flute 3",
            abjad.Flute(
                markup=markups.instrument("Flute 3"),
                short_markup=markups.short_instrument("fl.3"),
                ),
            ),

        (
            "Bbclarinet 1",
            abjad.ClarinetInBFlat(
                markup=markups.instrument("Bb Clarinet 1"),
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
            "Violin 1",
            abjad.Violin(
                markup=markups.instrument("Violin 1"),
                short_markup=markups.short_instrument("vn 1"),
            ),
        ),
        (
            "Violin 2",
            abjad.Violin(
                markup=markups.instrument("Violin 2"),
                short_markup=markups.short_instrument("vn 2"),
            ),
        ),
        (
            "Violin 3",
            abjad.Violin(
                markup=markups.instrument("Violin 3"),
                short_markup=markups.short_instrument("vn 3"),
            ),
        ),
        (
            "Violin 4",
            abjad.Violin(
                markup=markups.instrument("Violin 4"),
                short_markup=markups.short_instrument("vn 4"),
            ),
        ),
        (
            "Violin 5",
            abjad.Violin(
                markup=markups.instrument("Violin 5"),
                short_markup=markups.short_instrument("vn 5"),
            ),
        ),
        (
            "Violin 6",
            abjad.Violin(
                markup=markups.instrument("Violin 6"),
                short_markup=markups.short_instrument("vn 6"),
            ),
        ), 
        (
            "Violin 7",
            abjad.Violin(
                markup=markups.instrument("Violin 7"),
                short_markup=markups.short_instrument("vn 7"),
            ),
        ),
        (
            "Viola",
            abjad.Viola(
                markup=markups.instrument("Viola"),
                short_markup=markups.short_instrument("va"),
            ),
        ),
    ]
)

if __name__ == '__main__':
    
    print(f"number of instruments = {len(instruments)}")
    for key, item in instruments.items():
        print(key, item)


