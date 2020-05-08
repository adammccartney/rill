import baca


distances = (5, 12, 22)

breaks = baca.breaks(
    baca.page(
        baca.system(
            *distances,
            measure=1,
            y_offset=30 - 5 + 0 * sum(distances)
            ),
        baca.system(
            *distances,
            measure=11,
            y_offset=30 + 1 * sum(distances)
            ),
        number=1,
        ),
    )

spacing = baca.scorewide_spacing(
    __file__,
    breaks=breaks,
    fallback_duration=(1, 14),
    )
