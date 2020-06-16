import abjad
import rill 

"""
Defines scoretemplate, subclass of abjad.ScoreTemplate. Segments appended later. 
"""



class ScoreTemplate(abjad.ScoreTemplate):
    r"""rill Score template.
    
    ::

        >>> import rill
        >>> template = rill.tools.ScoreTemplate()
        >>> score = template()
        >>> print(format(score))
        abjad.f(score)
        \context Score = "Score" %! rill.ScoreTemplate.__call__()
        <<                       %! rill.ScoreTemplate.__call__()
    \context GlobalContext = "Global_Context" %! abjad.ScoreTemplate._make_global_context()
    <<                                        %! abjad.ScoreTemplate._make_global_context()
        \context GlobalRests = "Global_Rests" %! abjad.ScoreTemplate._make_global_context()
        {                                     %! abjad.ScoreTemplate._make_global_context()
        } %! abjad.ScoreTemplate._make_global_context()
        \context GlobalSkips = "Global_Skips" %! abjad.ScoreTemplate._make_global_context()
        {                                     %! abjad.ScoreTemplate._make_global_context()
        } %! abjad.ScoreTemplate._make_global_context()
    >> %! abjad.ScoreTemplate._make_global_context()
    \context MusicContext = "Music_Context" %! rill.ScoreTemplate.__call__()
    <<                                      %! rill.ScoreTemplate.__call__()
        \context Staff = "Violin" %! rill.ScoreTemplate.__call__()
        <<                        %! rill.ScoreTemplate.__call__()
            \context Voice = "Violin_Markup_Voice" %! rill.ScoreTemplate.__call__()
            {                                      %! rill.ScoreTemplate.__call__()
            } %! rill.ScoreTemplate.__call__()
            \context Voice = "Violin_Music_Voice" %! rill.ScoreTemplate.__call__()
            {                                     %! rill.ScoreTemplate.__call__()
            } %! rill.ScoreTemplate.__call__()
            \context Voice = "Violin_Dynamics_Voice" %! rill.ScoreTemplate.__call__()
            {                                        %! rill.ScoreTemplate.__call__()
            } %! rill.ScoreTemplate.__call__()
        >> %! rill.ScoreTemplate.__call__()
        \context Staff = "MonoSynth" %! rill.ScoreTemplate.__call__()
        <<                           %! rill.ScoreTemplate.__call__()
            \context Voice = "MonoSynth_Markup_Voice" %! rill.ScoreTemplate.__call__()
            {                                         %! rill.ScoreTemplate.__call__()
            } %! rill.ScoreTemplate.__call__()
            \context Voice = "MonoSynth_Music_Voice" %! rill.ScoreTemplate.__call__()
            {                                        %! rill.ScoreTemplate.__call__()
            } %! rill.ScoreTemplate.__call__()
            \context Voice = "MonoSynth_Dynamics_Voice" %! rill.ScoreTemplate.__call__()
            {                                           %! rill.ScoreTemplate.__call__()
            } %! rill.ScoreTemplate.__call__()
        >> %! rill.ScoreTemplate.__call__()
        \context MusicContext = "PolySynth_Music_Context" %! rill.ScoreTemplate.__call__()
        {                                                 %! rill.ScoreTemplate.__call__()
            \context PolySynthMusicStaffGroup = "PolySynth_Music_Staff_Group" %! rill.ScoreTemplate.__call__()
            <<                                                                %! rill.ScoreTemplate.__call__()
                \context PolySynthRHStaff = "PolySynth_Music_RH_Staff" %! rill.ScoreTemplate.__call__()
                <<                                                     %! rill.ScoreTemplate.__call__()
                    \context RHVoiceI = "RH_Voice_I" %! rill.ScoreTemplate.__call__()
                    {                                %! rill.ScoreTemplate.__call__()
                    } %! rill.ScoreTemplate.__call__()
                    \context RHVoiceII = "RH_Voice_II" %! rill.ScoreTemplate.__call__()
                    {                                  %! rill.ScoreTemplate.__call__()
                    } %! rill.ScoreTemplate.__call__()
                >> %! rill.ScoreTemplate.__call__()
                \context PolySynthLHStaff = "PolySynth_Music_LH_Staff" %! rill.ScoreTemplate.__call__()
                <<                                                     %! rill.ScoreTemplate.__call__()
                    \context LHVoiceI = "LH_Voice_I" %! rill.ScoreTemplate.__call__()
                    {                                %! rill.ScoreTemplate.__call__()
                    } %! rill.ScoreTemplate.__call__()
                    \context LHVoiceII = "LH_Voice_II" %! rill.ScoreTemplate.__call__()
                    {                                  %! rill.ScoreTemplate.__call__()
                    } %! rill.ScoreTemplate.__call__()
                >> %! rill.ScoreTemplate.__call__()
            >> %! rill.ScoreTemplate.__call__()
        } %! rill.ScoreTemplate.__call__()
    >> %! rill.ScoreTemplate.__call__()
  >> %! rill.ScoreTemplate.__call__()

    """
    ### CLASS VARIABLES ###

    __documentation_section__ = None

    _always_make_global_rests = True

    _global_rests_in_topmost_staff = True

    def __init__(self):
        super(ScoreTemplate, self).__init__()
        self.voice_abbreviations.update(
            {
                "vn": "Violin_Music_Voice", 
                "msy" : "MonoSynth_Music_Voice",
                "rh_v1": "RH_I_Music_Voice",
                #"rh_v2": "RH_II_Music_Voice",
                "lh_v1": "LH_I_Music_Voice",
                #"lh_v2": "LH_II_Music_Voice",
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

        # Violin
        markup_voice = abjad.Voice(name="Violin_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Violin_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Violin_Dynamics_Voice", tag=tag)
        violin_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="Violin",
            tag=tag,
        )
        abjad.annotate(
            violin_staff,
            "default_instrument",
            rill.instruments["Violin"],
        )
        abjad.annotate(violin_staff, "default_clef", abjad.Clef("treble"))

        # MonoSynth 
        markup_voice = abjad.Voice(name="MonoSynth_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="MonoSynth_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="MonoSynth_Dynamics_Voice", tag=tag)
        monosynth_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="MonoSynth",
            tag=tag,
        )
        abjad.annotate(
            monosynth_staff,
            "default_instrument",
            rill.instruments["MonoSynth"],
        )
        abjad.annotate(monosynth_staff, "default_clef", abjad.Clef("treble"))


        ### RH PolySynth Voices ###
        markup_voice = abjad.Voice(name="RH_I_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="RH_I_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="RH_I_Dynamics_Voice", tag=tag)

        #        rh_voice_2 = abjad.Voice(
        #            lilypond_type="RHVoiceII", name="RH_II_Music_Voice", tag=tag
        #            )
       
        # RH PolySynth Staff 
        polysynth_music_rh_staff = abjad.Staff(
                [markup_voice, music_voice, dynamics_voice],
                lilypond_type="PolySynthRHStaff",
                simultaneous=True,
                name="PolySynth_Music_RH_Staff",
                tag=tag,
                )
        abjad.annotate(
                polysynth_music_rh_staff, "default_clef", abjad.Clef("treble")
                )
        
        ### LH PolySynth Voices ###
        markup_voice = abjad.Voice(name="LH_I_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="LH_I_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="LH_I_Dynamics_Voice", tag=tag)
        #        lh_voice_2 = abjad.Voice(
        #            lilypond_type="LHVoiceII", name="LH_II_Music_Voice", tag=tag
        #        )
        #
       
        # LH PolySynth Staff
        polysynth_music_lh_staff = abjad.Staff(
                [markup_voice, music_voice, dynamics_voice],
                lilypond_type="PolySynthLHStaff",
                simultaneous=True,
                name="PolySynth_Music_LH_Staff",
                tag=tag,
                )
        abjad.annotate(
                polysynth_music_lh_staff, "default_clef", abjad.Clef("bass")
                )

        # PolySynth Staff Group 
        polysynth_music_staff_group = abjad.StaffGroup(
                [polysynth_music_rh_staff, polysynth_music_lh_staff],
                lilypond_type="PolySynthMusicStaffGroup",
                name="PolySynth_Music_Staff_Group",
                tag=tag,
                )
        polysynth = rill.instruments["PolySynth"]
        abjad.annotate(polysynth_music_staff_group, "default_insrument", polysynth)

        # PolySynth Music Context
        polysynth_music_context = abjad.Context(
                [polysynth_music_staff_group],
                lilypond_type="MusicContext",
                name="PolySynth_Music_Context",
                tag=tag
                )
        
        # Music Context
        music_context = abjad.Context(
                [
                    violin_staff,
                    monosynth_staff,
                    polysynth_music_context,
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
                    ('vl', 'Violin_Music_Voice'),
                    ('msy', 'MonoSynth_Music_Voice'),
                    ('rh_v1', 'RH_I_Music_Voice'),
                    # ('rh_v2', 'RH_II_Music_Voice'),
                    ('lh_v1', 'LH_I_Music_Voice'),
                    #('lh_v2', 'LH_II_Music_Voice'),
                    ]
                )
        """
        return super(ScoreTemplate, self).voice_abbreviations
