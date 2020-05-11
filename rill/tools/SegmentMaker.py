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
    def _make_lilypond_file(self, midi=False):
        return abjad.Staff("c'4 d'4 e'4 f'4").__illustrate__()

   
