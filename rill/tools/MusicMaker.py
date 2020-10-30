import copy
import abjadext.rmakers
import abjad


class AttachmentMaker(object):
    """
    An abstract attachment-making class
    """

    def __init__(self, attachment, selector):
        self.attachment = attachment
        self.selector = selector

    def __call__(self, music):
        assert False, "maker must be defined"


class AccentAttachmentMaker(AttachmentMaker):
    """
    Adds an accent to the first note in a logical tie
    """

    def __init__(self, attachment, selector):
        AttachmentMaker.__init__(self, attachment, selector)

    def __call__(self, music):
        for selection in self.selector(music):
            self._attach_to_first_leaf(selection)

    def _attach_to_first_leaf(self, logical_tie):
        first_leaf = logical_tie.head
        if not isinstance(first_leaf, abjad.Rest):
            attachment = copy.copy(self.attachment)
            abjad.attach(attachment, first_leaf)
        elif isinstance(first_leaf, abjad.Rest):
            pass


class MusicMaker(object):
    """
    A music-making machine.
    """

    def __init__(
        self,
        counts,
        denominator,
        pitches,
        attachment_makers=None,
        ):
        self.counts = counts
        self.denominator = denominator
        self.pitches = pitches
        self.attachment_makers = attachment_makers or []

    def __call__(self, time_signature_pairs):
        music = self._make_basic_rhythm(
            time_signature_pairs,
            self.counts,
            self.denominator,
            )
        music = self._clean_up_rhythm(music, time_signature_pairs)
        music = self._add_pitches(music, self.pitches)
        music = self._add_attachments(music)
        return music

    def _make_basic_rhythm(self, time_signature_pairs, counts, denominator):
        """
        Make a basic rhythm using ``time_signature_pairs``, ``counts`` and
        ``denominator``.
        """
        total_duration = sum(
            abjad.Duration(pair) for pair in time_signature_pairs
            )
        talea = abjadext.rmakers.Talea(
            counts=counts,
            denominator=denominator,
            )
        talea_index = 0
        all_leaves = []
        current_duration = abjad.Duration(0)
        while current_duration < total_duration:
            leaf_duration = talea[talea_index]
            if leaf_duration > 0:
                pitch = abjad.NamedPitch("c'")
            else:
                pitch = None
            leaf_duration = abs(leaf_duration)
            if (leaf_duration + current_duration) > total_duration:
                leaf_duration = total_duration - current_duration
            current_leaves = abjad.LeafMaker()([pitch], [leaf_duration])
            all_leaves.extend(current_leaves)
            current_duration += leaf_duration
            talea_index += 1
        music = abjad.Container(all_leaves)
        return music

    def _add_pitches(self, music, pitches):
        """
        Add ``pitches`` to music.
        """
        pitches = abjad.CyclicTuple(pitches)
        logical_ties = abjad.iterate(music).logical_ties(pitched=True)
        for i, logical_tie in enumerate(logical_ties):
            pitch = pitches[i]
            for note in logical_tie:
                note.written_pitch = pitch
        return music

    def _add_attachments(self, music):
        """
        Add attachments to ``music``.
        """

        if not isinstance(self.attachment_makers, list):
            try:
                attachment_maker = self.attachment_makers
                attachment_maker(music)
                return music
            except TypeError:
                print("Expected a selection as input")
        elif isinstance(self.attachment_makers, list):
            for attachment_maker in self.attachment_makers:
                attachment_maker(music)
            return music


def factory(aClass, *pargs, **kargs):
    return aClass(*pargs, **kargs)


class mMakerGenerator(object):
    """Generates the code block for a MusicGenerator"""

    def __init__(
            self,
            counts,
            denominator,
            pitches,
            attachment_makers,
            time_signature_pairs,
    ):
        self.counts = counts
        self.denominator = denominator
        self.pitches = pitches
        self.attachment_makers = attachment_makers
        self.time_signature_pairs = time_signature_pairs

    def __call__(self):
        music_maker_obj = self._make_music_maker_object()
        music = music_maker_obj(self.time_signature_pairs)
        return music

    def _make_music_maker_object(self):
        music_maker_obj = factory(
            MusicMaker,
            self.counts,
            self.denominator,
            self.pitches,
            self.attachment_makers,
        )
        return music_maker_obj


if __name__ == '__main__':
    import abjad
    # THIS IS THE INPUT TO MY MUSICAL IDEA
    time_signature_pairs = [(3, 4), (5, 16), (3, 8), (4, 4)]
    counts = [1, 2, -3, 4]
    denominator = 16

    pitches = abjad.CyclicTuple([0, 3, 7, 12, 7, 3])
    clef = "treble"

    tenuto_attachment_maker = AccentAttachmentMaker(
        selector=abjad.select().logical_ties(),
        attachment=abjad.Articulation("tenuto")
    )
    staccato_attachment_maker = AccentAttachmentMaker(
        selector=abjad.select().logical_ties(),
        attachment=abjad.Staccato()
    )

    attachment_makers = [tenuto_attachment_maker, staccato_attachment_maker]

    my_musicmaker = MusicMaker(
        counts,
        denominator,
        pitches,
        attachment_makers=[
            tenuto_attachment_maker,
            staccato_attachment_maker,
        ],
    )
    music = my_musicmaker(time_signature_pairs)
    abjad.f(music)
