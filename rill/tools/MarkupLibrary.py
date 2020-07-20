import abjad

class MarkupLibrary(object):
    """
    Markup library
    """

    ### CLASS VARIABLES ###

    __slots__ = ()

    ### PUBLIC METHODS ###

    @staticmethod
    def ord():
        return abjad.Markup("ord.", direction=abjad.Up).upright()

    @staticmethod
    def mx():
        return abjad.Markup("\\bold MX.", direction=abjad.Up).upright()

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
