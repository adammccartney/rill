import baca


distances = (5, 12, 16)

breaks = baca.breaks(
    baca.page(
        baca.system(
            *distances,
            measure=1,
            y_offset=20 - 5 + 0 * sum(distances)
            ),
        baca.system(
            *distances,
            measure=11,
            y_offset=20 + 1 * sum(distances)
            ),
        baca.system(
            *distances,
            measure=21,
            y_offset=20 + 2 * sum(distances)
            ),
        baca.system(
            *distances,
            measure=31,
            y_offset=20 + 3 * sum(distances)
            ),
        baca.system(
            *distances,
            measure=41,
            y_offset=20 + 4 * sum(distances)
            ),
        baca.system(
            *distances,
            measure=51,
            y_offset=20 + 5 * sum(distances)
            ),
        number=1,
        ),
    baca.page(
        baca.system(
            *distances,
            measure=61,
            y_offset=20 + 0 * sum(distances)
            ),
        number=2,
        ),
    )

spacing = baca.scorewide_spacing(
    __file__,
    breaks=breaks,
    fallback_duration=(1, 14),
    )
