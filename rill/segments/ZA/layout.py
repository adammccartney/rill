import baca


distances = (5, 15, 20)

breaks = baca.breaks(
    baca.page(
        baca.system(
            *distances,
            measure=1,
            y_offset=50 - 5 + 0 * sum(distances)
            ),
        baca.system(
            *distances,
            measure=11,
            y_offset=50 + 1 * sum(distances)
            ),
        baca.system(
            *distances,
            measure=21,
            y_offset=50 + 2 * sum(distances)
            ),
        baca.system(
            *distances,
            measure=31,
            y_offset=50 + 3 * sum(distances)
            ),
        number=1,
        ),
    baca.page(
        baca.system(
            *distances,
            measure=41,
            y_offset=10 + 0 * (30 + 16),
            ),
        baca.system(
            *distances,
            measure=51,
            y_offset=10 + 1 * (30 + 16),
            ),
        number=2,
        ),
    )

spacing = baca.scorewide_spacing(
    __file__,
    breaks=breaks,
    fallback_duration=(1, 14),
    )
