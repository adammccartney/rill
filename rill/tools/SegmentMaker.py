import abjad
import copy
from rill.tools.ScoreTemplate import ScoreTemplate


class SegmentMaker(abjad.SegmentMaker):
    """
    Segment-maker.

    >>> import rill

    .. container:: example

        >>> maker = rill.SegmentMaker()
        >>> abjad.f(maker)
        rill.SegmentMaker(
                metronome_marks=[],
                time_signatures=[],
                )

    """
    
    ### CLASS ATTRIBUTES ###

    __documentation_section__ = None

    __slots__ = (
            "_lilypond_file",
            "_metadata",
            "_score",
            "name",
            )

    ### INITIALIZER ###

    def __init__(
            self, 
            name=None,
        ):
            super(SegmentMaker, self).__init__()
            self.__lilypond_file = None


    ### PRIVATE PROPERTIES ###

    @property 
    def _music_voices(self):
        return(
                self._score["Flute_Music_Voice"],
                self._score["Bb_Clarinet_Music_Voice"],
                self._score["Guitar_Music_Voice"],
                self._score["Viola_Music_Voice"],
                )

    ### PRIVATE METHODS ###
    
    def _make_lilypond_file(self, midi=False):
        return abjad.Staff("c'4 d'4 e'4 f'4").__illustrate__()

    def _make_score(self):
        template = Score.Template()
        score = template()
        self._score = score


    ### PUBLIC METHODS ###

    def run(
        self,
        metadata=None,
        persist=None,
        previous_metadata=None,
        previous_persist=None,
        segment_directory=None,
    ):
        """
        Runs segment-maker

        Returns LilyPond file.
        """
        self._metadata = abjad.OrderedDict(metadata)
        self._persist = abjad.OrderedDict(persist)
        self._segment_directory = segment_directory
        self._make_score()
        self._make_lilypond_file()
        return self._lilypond_file
