import abjad

"""
Defines scoretemplate, subclass of abjad.ScoreTemplate. Segments appended later. 
"""



class ScoreTemplate(abjad.ScoreTemplate):
    """
    Score template.
    """
    ### CLASS VARIABLES ###

    __documentation_section__ = None

    _always_make_global_rests = True

    _global_rests_in_topmost_staff = True

    def __init__(self):
        super(ScoreTemplate, self).__init__()
        self.voice_abbreviations.update(
            {"Fl.": "Flute_Music_Voice", "ClBb." : "ClarinetBb_Music_Voice",
                "Guit.": "Guitar", "Vla.": "Viola"
                }
        )

    ### SPECIAL METHODS ###

    def __call__(self) -> abjad.Score:
        """
        Calls score template.
        """
        site = "rill.ScoreTemplate.__call__()"
        tag = abjad.Tag(site)

        # GLOBAL CONTEXT
        global_context = self._make_global_context()

        # Flute
        markup_voice = abjad.Voice(name="Flute_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Flute_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Flute_Dynamics_Voice", tag=tag)
        flute_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="Flute",
            tag=tag,
        )
        abjad.annotate(
            flute_staff,
            "default_instrument",
            rill.instruments["Flute"],
        )
        abjad.annotate(flute_staff, "default_clef", abjad.Clef("treble"))

        # Bb_Clarinet
        markup_voice = abjad.Voice(name="Bb_Clarinet_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Bb_Clarinet_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Bb_Clarinet_Dynamics_Voice", tag=tag)
        bb_clarinet_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="Bb_Clarinet",
            tag=tag,
        )
        abjad.annotate(
            bb_clarinet_staff,
            "default_instrument",
            rill.instruments["Bb_Clarinet"],
        )
        abjad.annotate(bb_clarinet_staff, "default_clef", abjad.Clef("treble"))

        # Guitar 
        markup_voice = abjad.Voice(name="Guitar_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Guitar_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Guitar_Dynamics_Voice", tag=tag)
        guitar_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="Guitar",
            tag=tag,
        )
        abjad.annotate(
            guitar_staff,
            "default_instrument",
            rill.instruments["Guitar"],
        )
        abjad.annotate(guitar_staff, "default_clef", abjad.Clef("treble"))

        # VIOLA  
        markup_voice = abjad.Voice(name="Viola_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Viola_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Viola_Dynamics_Voice", tag=tag)
        viola_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="Viola",
            tag=tag,
        )
        abjad.annotate(
            viola_staff,
            "default_instrument",
            rill.instruments["Viola"],
        )
        abjad.annotate(viola_2_staff, "default_clef", abjad.Clef("alto"))

        # SCORE
        quartet_staff = abjad.StaffGroup(
            [flute_staff, bb_clarinet_staff, guitar_staff, viola_staff],
            lilypond_type="Quartet_Staff",
            name="Quartet_Staff",
            tag=tag,
        )
        music_context = abjad.Context(
            [quartet_staff],
            lilypond_type="MusicContext",
            name="Music_Context",
            tag=tag,
        )
        score = abjad.Score(
            [global_context, music_context], name="Score", tag=tag
        )
        self._assert_lilypond_identifiers(score)
        self._assert_unique_context_names(score)
        self._assert_matching_custom_context_names(score)
        return score

    ### PUBLIC PROPERTIES ###

    @property
    def voice_abbreviations(self):
        """
        Gets voice abbreviations.
        ..  container:: example
            >>> score_template = rill.ScoreTemplate()
            >>> abjad.f(score_template.voice_abbreviations)
            abjad.OrderedDict(
                [
                    ('fl', 'Flute_Music_Voice'),
                    ('bbcl', 'Bb_Clarinet_Music_Voice'),
                    ('guit', 'Guitar_Music_Voice'),
                    ('vla', 'Viola_Music_Voice'),
                    ]
                )
        """
        return super(ScoreTemplate, self).voice_abbreviations
