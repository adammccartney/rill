import copy
import abjadext.rmakers
import abjad


s = abjad.Staff("c'4 c'4 c'4 c'4")
pitches = [0, 1, [2, 3], 4]


class PolyMusicMaker(object):
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
        #fused_music = self._fuse_logical_ties(rcleaned_music,
        #                                      time_signature_pairs)
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
        shards = abjad.mutate(music[:]).split(time_signature_pairs)
        for i, shard in enumerate(shards):
            time_signature = time_signature_pairs[i]
            meter = abjad.Meter(time_signature)
            shard_duration = abjad.inspect(shard).duration()
            time_sig_duration = abjad.Duration(time_signature)
            assert shard_duration == time_sig_duration
            abjad.mutate(shard).rewrite_meter(meter, boundary_depth=1)
            abjad.mutate(shard).split([meter.duration], cyclic=True)
            #abjad.mutate(shard).fuse()
        return music

    def _fuse_logical_ties(self, music, time_signature_pairs):
        shards = abjad.mutate(music[:]).split(time_signature_pairs)
        for i, shard in enumerate(shards):
            time_signature = time_signature_pairs[i]
            selection = abjad.select(shard).logical_ties()
            for logical_tie in selection:
                abjad.mutate(logical_tie).fuse()
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
        logical_ties = abjad.select(music).logical_ties(pitches=True)
        print(pitches, logical_ties)
        #for logical_tie, pitch in zip(logical_ties, pitches):
        #    if isinstance(pitch, list):
        #        new_leaf = abjad.Chord()
        #        new_leaf.written_duration = logical_tie.written_duration
        #        new_leaf.written_pitches = pitch
        #    else:
        #        new_leaf = abjad.Note()
        #        new_leaf.written_duration = logical_tie.written_duration
        #        new_leaf.written_pitch = pitch
        #    abjad.mutate(logical_tie).replace(new_leaf)
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


if __name__ == '__main__':
    import abjad
    # THIS IS THE INPUT TO MY MUSICAL IDEA
    time_signature_pairs = [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4)]
    counts = [4, 3, 5, 3, 2, 3]
    denominator = 4

    pitches = abjad.CyclicTuple(["e''", "c''", ["g''", "bf''"], "a''", "d'''"])
    clef = "treble"

    my_musicmaker = PolyMusicMaker(
        counts,
        denominator,
        pitches=[1, [2, 3], 4],
        attachment_makers=[],
        override_makers=[],
    )
    music = my_musicmaker(time_signature_pairs)
    staff = abjad.Staff([music])

    abjad.f(staff)
