import abjad

class MarkupLibrary(object):
    """
    Markup library
    """

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### PUBLIC METHODS ###
    @staticmethod
    def aeolian():
        return abjad.Markup("aeolian", direction=abjad.Up).upright()

    @staticmethod
    def con_sord():
        return abjad.Markup("con sord.", direction=abjad.Up).upright()

    @staticmethod
    def legato():
        return abjad.Markup("legato", direction=abjad.Up).upright()

    @staticmethod
    def ordinario():
        return abjad.Markup("ord.", direction=abjad.Up).upright()

    @staticmethod
    def mx():
        return abjad.Markup("\\bold MX.", direction=abjad.Up).upright()

    @staticmethod
    def pizz():
        return abjad.Markup("pizz.", direction=abjad.Up).upright()

    @staticmethod
    def pont():
        return abjad.Markup("sul pont.", direction=abjad.Up).upright()

    @staticmethod
    def mark(num):
        string = f"\\mark #{num}"
        return abjad.Markup(string, direction=abjad.Up).upright()

    @staticmethod
    def rhythmically():
        return abjad.Markup("rhythmically", direction=abjad.Up).upright()

    @staticmethod
    def sul_I():
        return abjad.Markup("sul I", direction=abjad.Up).upright()

    @staticmethod
    def sul_II():
        return abjad.Markup("sul II", direction=abjad.Up).upright()

    @staticmethod
    def sul_III():
        return abjad.Markup("sul III", direction=abjad.Up).upright()

    @staticmethod
    def sul_IV():
        return abjad.Markup("sul IV", direction=abjad.Up).upright()

    @staticmethod
    def tasto():
        return abjad.Markup("sul tasto", direction=abjad.Up).upright()

    @staticmethod
    def flaut():
        return abjad.Markup("flautando", direction=abjad.Up).upright()

    @staticmethod
    def flaut_pont():
        return abjad.Markup(
                "\\center-column {flaut.-  pont.}",
                direction=abjad.Up).upright()

    @staticmethod
    def via_sord():
        return abjad.Markup("via sord.", direction=abjad.Up).upright()
