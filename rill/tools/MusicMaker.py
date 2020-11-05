import copy
import abjadext.rmakers
import abjad

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
        override_makers=None,
    ):
        self.counts = counts
        self.denominator = denominator
        self.pitches = pitches
        self.attachment_makers = attachment_makers or []
        self.override_makers = override_makers or []

    def __call__(self, time_signature_pairs):
        music = self._make_basic_rhythm(
            time_signature_pairs,
            self.counts,
            self.denominator,
        )
        rcleaned_music = self._clean_up_rhythm(music, time_signature_pairs)
        pitched_music = self._add_pitches(rcleaned_music, self.pitches)
        articulate_music = self._add_attachments(pitched_music)
        music_with_overrides = self._add_overrides(articulate_music)
        return music_with_overrides

    def _clean_up_rhythm(self, music, time_signature_pairs):
        """
        Clean up rhythms in ``music`` via ``time_signature_pairs``.
        """
        for i in range(len(time_signature_pairs)):
            time_signature = time_signature_pairs[i]
            print("time_signature: ", time_signature)
        shards = abjad.mutate(music[:]).split(time_signature_pairs)
        for i, shard in enumerate(shards):
            print(shard)
            time_signature = time_signature_pairs[i]
            meter = abjad.Meter(time_signature)
            shard_duration = abjad.inspect(shard).duration()
            time_sig_duration = abjad.Duration(time_signature)
            assert shard_duration == time_sig_duration
            abjad.mutate(shard).split([meter.duration], cyclic=True)
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
        print("music after mutation: ", music)
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
                print(attachment_maker, " is not an attachment maker")
        elif isinstance(self.attachment_makers, list):
            for attachment_maker in self.attachment_makers:
                attachment_maker(music)
            return music

    def _add_overrides(self, music):
        if not isinstance(self.attachment_makers, list):
            try:
                override_maker = self.override_makers
                override_maker(music)
                return music
            except TypeError:
                print(override_maker, " is not an override maker")
        elif isinstance(self.attachment_makers, list):
            for override_maker in self.override_makers:
                override_maker(music)
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
    from rill.tools.AttachmentMaker import AccentAttachmentMaker

    # THIS IS THE INPUT TO MY MUSICAL IDEA
    time_signature_pairs = [(3, 4), (5, 16), (3, 8), (4, 4)]
    counts = [1, 2, -3, 4]
    denominator = 8

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
    staff = abjad.Staff([music])
    for i in range(len(time_signature_pairs)):
        print(abjad.TimeSignature(time_signature_pairs[i]))

    abjad.f(staff)
