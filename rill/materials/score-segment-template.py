import abjad

"""
Defines scoretemplate, instance of Score class. Segments appended later. 
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
        site = "ins_wasser.ScoreTemplate.__call__()"
        tag = abjad.Tag(site)

        # GLOBAL CONTEXT
        global_context = self._make_global_context()

        # VIOLA 1
        markup_voice = abjad.Voice(name="Viola_I_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Viola_I_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Viola_I_Dynamics_Voice", tag=tag)
        viola_1_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="Viola_I",
            tag=tag,
        )
        abjad.annotate(
            viola_1_staff,
            "default_instrument",
            ins_wasser.instruments["ViolaI"],
        )
        abjad.annotate(viola_1_staff, "default_clef", abjad.Clef("alto"))

        # VIOLA 2
        markup_voice = abjad.Voice(name="Viola_II_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Viola_II_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Viola_II_Dynamics_Voice", tag=tag)
        viola_2_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="Viola_II",
            tag=tag,
        )
        abjad.annotate(
            viola_2_staff,
            "default_instrument",
            ins_wasser.instruments["ViolaII"],
        )
        abjad.annotate(viola_2_staff, "default_clef", abjad.Clef("alto"))

        # SCORE
        piano_staff = abjad.StaffGroup(
            [viola_1_staff, viola_2_staff],
            lilypond_type="PianoStaff",
            name="Piano_Staff",
            tag=tag,
        )
        music_context = abjad.Context(
            [piano_staff],
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
            >>> score_template = ins_wasser.ScoreTemplate()
            >>> abjad.f(score_template.voice_abbreviations)
            abjad.OrderedDict(
                [
                    ('va1', 'Viola_I_Music_Voice'),
                    ('va2', 'Viola_II_Music_Voice'),
                    ]
                )
        """
        return super(ScoreTemplate, self).voice_abbreviations
