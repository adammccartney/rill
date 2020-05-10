import abjad
import mccartney


instruments = abjad.OrderedDict(
    [
        (
            "Flute",
            abjad.Flute(
                markup=mccartney.markups.instrument("Flute"),
                short_markup=mccartney.markups.short_instrument("Fl."),
            ),
        ),
        (
            "Bb_Clarinet",
            abjad.ClarinetInBFlat(
                markup=mccartney.markups.instrument("Bb_Clarinet"),
                short_markup=mccartney.markups.short_instrument("BbCl."),
            ),
        ),
        (
            "Guitar",
            abjad.Guitar(
                markup=mccartney.markups.instrument("Guitar"),
                short_markup=mccartney.markups.short_instrument("Guit."),
            ),
        ),
        (
            "Viola",
            abjad.Viola(
                markup=mccartney.markups.instrument("Viola"),
                short_markup=mccartney.markups.short_instrument("Vla."),
            ),
        ),
    ]
)
