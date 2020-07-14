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
    def pont():
        return abjad.Markup("sul pont.", direction=abjad.Up).upright()

    @staticmethod
    def tasto():
        return abjad.Markup("sul tasto", direction=abjad.Up).upright()
    
    @staticmethod
    def flaut():
        return abjad.Markup("flautando", direction=abjad.Up).upright()

    @staticmethod
    def flaut_pont():
        return abjad.Markup("flaut. + pont.", direction=abjad.Up).upright()
