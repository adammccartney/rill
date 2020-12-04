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
        #fused_music = self._fuse_logical_ties(rcleaned_music,
        #                                      time_signature_pairs)
        bchecked_music = self._add_bar_number_checks(rcleaned_music)
        pitched_music = self._add_pitches(bchecked_music, self.pitches)
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

    def _add_bar_number_checks(self, music):
        abjad.attach(abjad.LilyPondLiteral(
            r"\barNumberCheck #2"), music[1])
        abjad.attach(abjad.LilyPondLiteral(
            r"\barNumberCheck #4"), music[3])
        abjad.attach(abjad.LilyPondLiteral(
            r"\barNumberCheck #6"), music[5])
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
    from rill.tools.AttachmentMaker import (AccentAttachmentMaker,
                                            MarkupAttachmentMaker,
                                            DynamicAttachmentMaker)
    from rill.tools.OverrideMaker import NoteHeadOverrideMaker
    from rill.tools.MarkupLibrary import MarkupLibrary as markup
    #from rill.materials.overrides.definition import cross_note_head_override

    # THIS IS THE INPUT TO MY MUSICAL IDEA
    time_signature_pairs = [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4)]
    counts = [4, 3, 5, 3, 2, 3]
    denominator = 4

    pitches = abjad.CyclicTuple(["e''", "c''", "g''", "bf''", "a''", "d'''"])
    clef = "treble"

    tenuto_attachment_maker = AccentAttachmentMaker(
        selector=abjad.select().logical_ties(),
        attachment=abjad.Articulation("tenuto")
    )
    staccato_attachment_maker = AccentAttachmentMaker(
        selector=abjad.select().logical_ties(),
        attachment=abjad.Staccato()
    )

    pont_attachment_maker = MarkupAttachmentMaker(
        selector=abjad.select(),
        attachment=markup.pont()
    )

    forte_attachment_maker = DynamicAttachmentMaker(
        selector=abjad.select(),
        attachment=abjad.Dynamic("f")
    )

  #  harmonic_override_maker = NoteHeadOverrideMaker('harmonic')
    attachment_makers = [tenuto_attachment_maker, staccato_attachment_maker]

    my_musicmaker = MusicMaker(
        counts,
        denominator,
        pitches,
        attachment_makers=[
            tenuto_attachment_maker,
            staccato_attachment_maker,
            pont_attachment_maker,
            forte_attachment_maker,
        ],
        override_makers=[],
    )
    music = my_musicmaker(time_signature_pairs)
    staff = abjad.Staff([music])
    for i in range(len(time_signature_pairs)):
        print(abjad.TimeSignature(time_signature_pairs[i]))

    abjad.f(staff)
    #abjad.show(staff)
