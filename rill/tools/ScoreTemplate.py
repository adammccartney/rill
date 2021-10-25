import abjad
import rill


class ScoreTemplate(abjad.ScoreTemplate):
    """
    Makes a simple score template for ensemble
    """

    # CLASS VARIABLES #

    __documentation_section__ = None

    _always_make_global_rests = False

    _global_rests_in_topmost_staff = False

    def __init__(self):
        super(ScoreTemplate, self).__init__()
        self.voice_abbreviations.update(
            {"fl1": "Flute1_Music_Voice",
             "fl2": "Flute2_Music_Voice",
             "fl3": "Flute3_Music_Voice",
             "fl4": "Flute4_Music_Voice",
             "Bbcl1": "Bbclarinet1_Music_Voice",
             "vb": "vibraphone_Music_Voice",
             "vn1": "Violin1_Music_Voice",
             "vn2": "Violin2_Music_Voice",
             "vn3": "Violin3_Music_Voice",
             "vn4": "Violin4_Music_Voice",
             "vn5": "Violin5_Music_Voice",
             "vn6": "Violin6_Music_Voice",
             "vn7": "Violin7_Music_Voice",
             "vn8": "Violin8_Music_Voice",
             "va": "Viola_Music_Voice",
             "vlc": "Cello_Music_Voice",
             }
            )

    # SPECIAL METHODS #

    def __call__(self) -> abjad.Score:
        """
        Calls score template.
        """
        site = "rill.ScoreTemplate.__call__()"
        tag = abjad.Tag(site)

        # GLOBAL CONTEXT
        global_context = self._make_global_context()

        # Woodwind
        # Flute 1
        markup_voice = abjad.Voice(name="Flute1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Flute1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Flute1_Dynamics_Voice", tag=tag)
        fluteOne_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Flute1",
            lilypond_type="FluteOneStaff",
            tag=tag,
        )
        abjad.annotate(
            fluteOne_staff,
            "default_instrument",
            rill.instruments["Flute1"],
        )
        abjad.annotate(fluteOne_staff, "default_clef", abjad.Clef("treble"))
        fluteOne_tag = abjad.LilyPondLiteral(
            r"\tag #'fluteOne", format_slot='before')
        abjad.attach(fluteOne_tag, fluteOne_staff)
        abjad.setting(fluteOne_staff).midi_instrument = abjad.scheme.Scheme(
                'flute', force_quotes=True)

        # Flute1
        markup_voice = abjad.Voice(name="Flute2_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Flute2_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Flute2_Dynamics_Voice", tag=tag)
        fluteTwo_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Flute2",
            lilypond_type="FluteTwoStaff",
            tag=tag,
        )
        abjad.annotate(
            fluteTwo_staff,
            "default_instrument",
            rill.instruments["Flute2"],
        )
        abjad.annotate(fluteTwo_staff, "default_clef", abjad.Clef("treble"))
        fluteTwo_tag = abjad.LilyPondLiteral(
            r"\tag #'fluteTwo", format_slot='before')
        abjad.attach(fluteTwo_tag, fluteTwo_staff)
        abjad.setting(fluteTwo_staff).midi_instrument = abjad.scheme.Scheme(
                'flute', force_quotes=True)

        # Flute Three
        markup_voice = abjad.Voice(name="Flute3_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Flute3_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Flute3_Dynamics_Voice", tag=tag)
        fluteThree_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Flute3",
            lilypond_type="FluteThreeStaff",
            tag=tag,
        )
        abjad.annotate(
            fluteThree_staff,
            "default_instrument",
            rill.instruments["Flute3"],
        )
        abjad.annotate(fluteThree_staff, "default_clef", abjad.Clef("treble"))
        fluteThree_tag = abjad.LilyPondLiteral(
            r"\tag #'fluteThree", format_slot='before')
        abjad.attach(fluteThree_tag, fluteThree_staff)
        abjad.setting(fluteThree_staff).midi_instrument = abjad.scheme.Scheme(
                'flute', force_quotes=True)

        # Flute Four
        markup_voice = abjad.Voice(name="Flute4_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Flute4_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Flute4_Dynamics_Voice", tag=tag)
        fluteFour_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Flute4",
            lilypond_type="FluteFourStaff",
            tag=tag,
        )
        abjad.annotate(
            fluteFour_staff,
            "default_instrument",
            rill.instruments["Flute4"],
        )
        abjad.annotate(fluteFour_staff, "default_clef", abjad.Clef("treble"))
        fluteFour_tag = abjad.LilyPondLiteral(
            r"\tag #'fluteFour", format_slot='before')
        abjad.attach(fluteFour_tag, fluteFour_staff)
        abjad.setting(fluteFour_staff).midi_instrument = abjad.scheme.Scheme(
                'flute', force_quotes=True)

        # Bb Clarinet
        markup_voice = abjad.Voice(name="Bbclarinet1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Bbclarinet1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(
            name="Bbclarinet1_Dynamics_Voice", tag=tag)
        Bbclarinet_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Bbclarinet1",
            lilypond_type="BbclarinetOneStaff",
            tag=tag,
        )
        abjad.annotate(
            Bbclarinet_staff,
            "default_instrument",
            rill.instruments["Bbclarinet1"],
        )
        abjad.annotate(Bbclarinet_staff, "default_clef", abjad.Clef("treble"))
        BbclarinetOne_tag = abjad.LilyPondLiteral(
            r"\tag #'BbclarinetOne", format_slot='before')
        abjad.attach(BbclarinetOne_tag, Bbclarinet_staff)
        abjad.setting(Bbclarinet_staff).midi_instrument = abjad.scheme.Scheme(
                'Bbclarinet', force_quotes=True)

        # Vibraphone
        markup_voice = abjad.Voice(name="Vibraphone_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Vibraphone_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Vibraphone_Dynamics_Voice", tag=tag)
        vibraphone_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Vibraphone",
            lilypond_type="VibraphoneStaff",
            tag=tag,
        )
        abjad.annotate(
            vibraphone_staff,
            "default_instrument",
            rill.instruments["Vibraphone"],
        )
        abjad.annotate(vibraphone_staff, "default_clef", abjad.Clef("treble"))
        vibraphone_tag = abjad.LilyPondLiteral(
            r"\tag #'vibraphone", format_slot='before')
        abjad.attach(vibraphone_tag, vibraphone_staff)
        abjad.setting(vibraphone_staff).midi_instrument = abjad.scheme.Scheme(
                'vibraphone', force_quotes=True)

        # Strings
        # Violin1
        markup_voice = abjad.Voice(name="Violin1_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Violin1_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Violin1_Dynamics_Voice", tag=tag)
        violinOne_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Violin1",
            lilypond_type="ViolinOneStaff",
            tag=tag,
        )
        abjad.annotate(
            violinOne_staff,
            "default_instrument",
            rill.instruments["Violin1"],
        )
        abjad.annotate(violinOne_staff, "default_clef", abjad.Clef("treble"))
        violinOne_tag = abjad.LilyPondLiteral(
            r"\tag #'violinOne", format_slot='before')
        abjad.attach(violinOne_tag, violinOne_staff)
        abjad.setting(violinOne_staff).midi_instrument = abjad.scheme.Scheme(
                'violin', force_quotes=True)

        # Violin2
        markup_voice = abjad.Voice(name="Violin2_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Violin2_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Violin2_Dynamics_Voice", tag=tag)
        violinTwo_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Violin2",
            lilypond_type="ViolinTwoStaff",
            tag=tag,
        )
        abjad.annotate(
            violinTwo_staff,
            "default_instrument",
            rill.instruments["Violin2"],
        )
        abjad.annotate(violinTwo_staff, "default_clef", abjad.Clef("treble"))
        violinTwo_tag = abjad.LilyPondLiteral(
            r"\tag #'violinTwo", format_slot='before')
        abjad.attach(violinTwo_tag, violinTwo_staff)
        abjad.setting(violinTwo_staff).midi_instrument = abjad.scheme.Scheme(
                'violin', force_quotes=True)

        # Violin3
        markup_voice = abjad.Voice(name="Violin3_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Violin3_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Violin3_Dynamics_Voice", tag=tag)
        violinThree_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Violin3",
            lilypond_type="ViolinThreeStaff",
            tag=tag,
        )
        abjad.annotate(
            violinThree_staff,
            "default_instrument",
            rill.instruments["Violin3"],
        )
        abjad.annotate(violinThree_staff, "default_clef", abjad.Clef("treble"))
        violinThree_tag = abjad.LilyPondLiteral(
            r"\tag #'violinThree", format_slot='before')
        abjad.attach(violinThree_tag, violinThree_staff)
        abjad.setting(violinThree_staff).midi_instrument = abjad.scheme.Scheme(
                'violin', force_quotes=True)

        # Violin4
        markup_voice = abjad.Voice(name="Violin4_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Violin4_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Violin4_Dynamics_Voice", tag=tag)
        violinFour_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Violin4",
            lilypond_type="ViolinFourStaff",
            tag=tag,
        )
        abjad.annotate(
            violinFour_staff,
            "default_instrument",
            rill.instruments["Violin4"],
        )
        abjad.annotate(violinFour_staff, "default_clef", abjad.Clef("treble"))
        violinFour_tag = abjad.LilyPondLiteral(
            r"\tag #'violinFour", format_slot='before')
        abjad.attach(violinFour_tag, violinFour_staff)
        abjad.setting(violinFour_staff).midi_instrument = abjad.scheme.Scheme(
                'violin', force_quotes=True)

        # Violin5
        markup_voice = abjad.Voice(name="Violin5_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Violin5_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Violin5_Dynamics_Voice", tag=tag)
        violinFive_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Violin5",
            lilypond_type="ViolinFiveStaff",
            tag=tag,
        )
        abjad.annotate(
            violinFive_staff,
            "default_instrument",
            rill.instruments["Violin5"],
        )
        abjad.annotate(violinFive_staff, "default_clef", abjad.Clef("treble"))
        violinFive_tag = abjad.LilyPondLiteral(
            r"\tag #'violinFive", format_slot='before')
        abjad.attach(violinFive_tag, violinFive_staff)
        abjad.setting(violinFive_staff).midi_instrument = abjad.scheme.Scheme(
                'violin', force_quotes=True)

        # Violin6
        markup_voice = abjad.Voice(name="Violin6_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Violin6_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Violin6_Dynamics_Voice", tag=tag)
        violinSix_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Violin6",
            lilypond_type="ViolinSixStaff",
            tag=tag,
        )
        abjad.annotate(
            violinSix_staff,
            "default_instrument",
            rill.instruments["Violin6"],
        )
        abjad.annotate(violinSix_staff, "default_clef", abjad.Clef("treble"))
        violinSix_tag = abjad.LilyPondLiteral(
            r"\tag #'violinSix", format_slot='before')
        abjad.attach(violinSix_tag, violinSix_staff)
        abjad.setting(violinSix_staff).midi_instrument = abjad.scheme.Scheme(
                'violin', force_quotes=True)

        # Violin7
        markup_voice = abjad.Voice(name="Violin7_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Violin7_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Violin7_Dynamics_Voice", tag=tag)
        violinSeven_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Violin7",
            lilypond_type="ViolinSevenStaff",
            tag=tag,
        )
        abjad.annotate(
            violinSeven_staff,
            "default_instrument",
            rill.instruments["Violin7"],
        )
        abjad.annotate(violinSeven_staff, "default_clef", abjad.Clef("treble"))
        violinSeven_tag = abjad.LilyPondLiteral(
            r"\tag #'violinSeven", format_slot='before'
        )
        abjad.attach(violinSeven_tag, violinSeven_staff)
        abjad.setting(violinSeven_staff).midi_instrument = abjad.scheme.Scheme(
                'violin', force_quotes=True)

        # Violin8
        markup_voice = abjad.Voice(name="Violin8_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Violin8_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Violin8_Dynamics_Voice", tag=tag)
        violinEight_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Violin8",
            lilypond_type="ViolinEightStaff",
            tag=tag,
        )
        abjad.annotate(
            violinEight_staff,
            "default_instrument",
            rill.instruments["Violin8"],
        )
        abjad.annotate(violinEight_staff, "default_clef", abjad.Clef("treble"))
        violinEight_tag = abjad.LilyPondLiteral(
            r"\tag #'violinEight", format_slot='before'
        )
        abjad.attach(violinEight_tag, violinEight_staff)
        abjad.setting(violinEight_staff).midi_instrument = abjad.scheme.Scheme(
                'violin', force_quotes=True)


        # Viola
        markup_voice = abjad.Voice(name="Viola_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Viola_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Viola_Dynamics_Voice", tag=tag)
        viola_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Viola",
            lilypond_type="ViolaStaff",
            tag=tag,
        )
        abjad.annotate(
            viola_staff,
            "default_instrument",
            rill.instruments["Viola"],
        )
        abjad.annotate(viola_staff, "default_clef", abjad.Clef("alto"))
        viola_tag = abjad.LilyPondLiteral(
            r"\tag #'viola", format_slot='before')
        abjad.attach(viola_tag, viola_staff)
        abjad.setting(viola_staff).midi_instrument = abjad.scheme.Scheme(
                'viola', force_quotes=True)

        # Cello
        markup_voice = abjad.Voice(name="Cello_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Cello_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Cello_Dynamics_Voice", tag=tag)
        cello_staff = abjad.Staff(
            [music_voice],
            simultaneous=True,
            name="Cello",
            lilypond_type="CelloStaff",
            tag=tag,
        )
        abjad.annotate(
            cello_staff,
            "default_instrument",
            rill.instruments["Cello"],
        )
        abjad.annotate(cello_staff, "default_clef", abjad.Clef("bass"))
        cello_tag = abjad.LilyPondLiteral(
            r"\tag #'cello", format_slot='before')
        abjad.attach(cello_tag, cello_staff)
        abjad.setting(cello_staff).midi_instrument = abjad.scheme.Scheme(
                'cello', force_quotes=True)


        # Define staff groups
        # Woodwind Staff Group
        woodwind_staff_group = abjad.StaffGroup(
                [
                    fluteOne_staff,
                    fluteTwo_staff,
                    fluteThree_staff,
                    fluteFour_staff,
                    Bbclarinet_staff
                ],
                simultaneous=True,
                lilypond_type="WoodwindStaffGroup",
                name="Woodwind_Staff_Group",
                tag=tag,
                )

        # Percussion Staff Group
        percussion_staff_group = abjad.StaffGroup(
                [vibraphone_staff],
                simultaneous=True,
                lilypond_type="PercussionStaffGroup",
                name="Percussion_Staff_Group",
                tag=tag,
                )

        # String Staff Group
        string_staff_group = abjad.StaffGroup(
                [
                    violinOne_staff,
                    violinTwo_staff,
                    violinThree_staff,
                    violinFour_staff,
                    violinFive_staff,
                    violinSix_staff,
                    violinSeven_staff,
                    violinEight_staff,
                    viola_staff
                    cello_staff
                ],
                simultaneous=True,
                lilypond_type="StringStaffGroup",
                name="String_Staff_Group",
                tag=tag,
                )

        # Music Context
        music_context = abjad.Context(
                [
                    woodwind_staff_group,
                    percussion_staff_group,
                    string_staff_group,
                ],
                lilypond_type="MusicContext",
                simultaneous=True,
                name="Music_Context",
                tag=tag,
                )

        # Score
        score = abjad.Score(
                [global_context, music_context], name="Score", tag=tag
                )
        #self._assert_lilypond_identifiers(score)
        #self._assert_unique_context_names(score)
        #self._assert_matching_custom_context_names(score)
        return score

    # PRIVATE METHODS #
    def _make_global_context(self):
        site = "abjad.ScoreTemplate._make_global_context()"
        tag = abjad.Tag(site)
        global_rests = abjad.Context(
            lilypond_type="GlobalRests", name="Global_Rests", tag=tag,
        )
        global_skips = abjad.Context(
            lilypond_type="GlobalSkips", name="Global_Skips", tag=tag,
        )
        global_context = abjad.Context(
            [global_skips, global_rests],
            lilypond_type="GlobalContext",
            simultaneous=True,
            name="Global_Context",
            tag=tag,
        )
        return global_context

    # PUBLIC PROPERTIES #
    @property
    def voice_abbreviations(self):
        """Gets voice abbreviations"""
        return super(ScoreTemplate, self).voice_abbreviations


if __name__ == '__main__':
    score = ScoreTemplate()
    score_template = score()
    abjad.f(score_template)
