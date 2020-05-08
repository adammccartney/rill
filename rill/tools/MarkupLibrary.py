import abjad


class MarkupLibrary(object):
    """
    Markup library.
    """

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### PUBLIC METHODS ###

    @staticmethod
    def clicks_1_2_per_second():
        return abjad.Markup("clicks (1-2/sec.)", direction=abjad.Up).upright()

    @staticmethod
    def clicks_2_3_per_second():
        return abjad.Markup("clicks (2-3/sec.)", direction=abjad.Up).upright()

    @staticmethod
    def MP_XFB_flaut():
        return abjad.Markup("MP + XFB flaut.", direction=abjad.Up).upright()

    @staticmethod
    def null():
        return abjad.Markup().null()

    @staticmethod
    def OB_no_pitch():
        return abjad.Markup("OB (no pitch)", direction=abjad.Up).upright()

    @staticmethod
    def OB_XFB():
        return abjad.Markup("OB + XFB", direction=abjad.Up).upright()

    @staticmethod
    def one_half_OB():
        return abjad.Markup("1/2OB", direction=abjad.Up).upright()

    @staticmethod
    def one_third_OB():
        return abjad.Markup("1/3OB", direction=abjad.Up).upright()

    @staticmethod
    def P_XFB_flaut():
        return abjad.Markup("P + XFB flaut.", direction=abjad.Up).upright()

    @staticmethod
    def PO_FB_flaut():
        return abjad.Markup("PO + FB flaut.", direction=abjad.Up).upright()

    @staticmethod
    def PO_NBS():
        return abjad.Markup("PO + NBS", direction=abjad.Up).upright()

    @staticmethod
    def PO_scratch():
        return abjad.Markup("PO + scratch", direction=abjad.Up).upright()

    @staticmethod
    def PO_slow_bow():
        return abjad.Markup("PO + slow bow", direction=abjad.Up).upright()

    @staticmethod
    def PO_XFB_flaut():
        return abjad.Markup("PO + XFB flaut.", direction=abjad.Up).upright()

    @staticmethod
    def pP_XFB_flaut():
        return abjad.Markup("pP + XFB flaut.", direction=abjad.Up).upright()

    @staticmethod
    def pT_XFB_flaut():
        return abjad.Markup("pT + XFB flaut.", direction=abjad.Up).upright()

    @staticmethod
    def sustain_until_m_130():
        return abjad.Markup(
            "sustain until m.130", direction=abjad.Up
        ).upright()

    @staticmethod
    def sustain_until_m_250():
        return abjad.Markup(
            "sustain until m.250", direction=abjad.Up
        ).upright()

    @staticmethod
    def tasto():
        return abjad.Markup("tasto", direction=abjad.Up).upright()

    @staticmethod
    def tasto_FB_flaut():
        return abjad.Markup("tasto + FB flaut.", direction=abjad.Up).upright()

    @staticmethod
    def tasto_NBS():
        return abjad.Markup("tasto + NBS", direction=abjad.Up).upright()

    @staticmethod
    def tasto_scratch():
        return abjad.Markup("tasto + scratch", direction=abjad.Up).upright()

    @staticmethod
    def tasto_slow_bow():
        return abjad.Markup("tasto + slow bow", direction=abjad.Up).upright()

    @staticmethod
    def tasto_XFB_flaut():
        return abjad.Markup("tasto + XFB flaut.", direction=abjad.Up).upright()

    @staticmethod
    def trans():
        return abjad.Markup("trans.", direction=abjad.Up).upright()

    @staticmethod
    def two_thirds_OB():
        return abjad.Markup("2/3OB", direction=abjad.Up).upright()

    @staticmethod
    def x_8():
        return (
            abjad.Markup("x8", direction=abjad.Up)
            .sans()
            .bold()
            .fontsize(6)
            .upright()
            .box()
            .override(("box-padding", 0.5))
        )

    @staticmethod
    def XP():
        return abjad.Markup("XP", direction=abjad.Up).upright()

    @staticmethod
    def XP_full_bow_strokes():
        return abjad.Markup(
            "XP + full bow strokes", direction=abjad.Up
        ).upright()

    @staticmethod
    def XP_XFB_flaut():
        return abjad.Markup("XP + XFB flaut.", direction=abjad.Up).upright()
