import abjad
import baca


instruments = abjad.OrderedDict(
    [
        (
            "ViolaI",
            abjad.Viola(
                markup=baca.markups.instrument("Viola I"),
                short_markup=baca.markups.short_instrument("Va. I"),
            ),
        ),
        (
            "ViolaII",
            abjad.Viola(
                markup=baca.markups.instrument("Viola II"),
                short_markup=baca.markups.short_instrument("Va. II"),
            ),
        ),
    ]
)
