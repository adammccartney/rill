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

        \context Score = "Score"                              %! rill.ScoreTemplate.__call__()
<<                                                            %! rill.ScoreTemplate.__call__()
    \context GlobalContext = "Global_Context"                 %! abjad.ScoreTemplate._make_global_context()
    <<                                                        %! abjad.ScoreTemplate._make_global_context()
        \context GlobalRests = "Global_Rests"                 %! abjad.ScoreTemplate._make_global_context()
        {                                                     %! abjad.ScoreTemplate._make_global_context()
        }                                                     %! abjad.ScoreTemplate._make_global_context()
        \context GlobalSkips = "Global_Skips"                 %! abjad.ScoreTemplate._make_global_context()
        {                                                     %! abjad.ScoreTemplate._make_global_context()
        }                                                     %! abjad.ScoreTemplate._make_global_context()
    >>                                                        %! abjad.ScoreTemplate._make_global_context()
    \context MusicContext = "Music_Context"                   %! rill.ScoreTemplate.__call__()
    {                                                         %! rill.ScoreTemplate.__call__()
        \context Quartet_Staff = "Quartet_Staff"              %! rill.ScoreTemplate.__call__()
        <<                                                    %! rill.ScoreTemplate.__call__()
            \context Staff = "Flute"                          %! rill.ScoreTemplate.__call__()
            <<                                                %! rill.ScoreTemplate.__call__()
                \context Voice = "Flute_Markup_Voice"         %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
                \context Voice = "Flute_Music_Voice"          %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
                \context Voice = "Flute_Dynamics_Voice"       %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
            >>                                                %! rill.ScoreTemplate.__call__()
            \context Staff = "Bb_Clarinet"                    %! rill.ScoreTemplate.__call__()
            <<                                                %! rill.ScoreTemplate.__call__()
                \context Voice = "Bb_Clarinet_Markup_Voice"   %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
                \context Voice = "Bb_Clarinet_Music_Voice"    %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
                \context Voice = "Bb_Clarinet_Dynamics_Voice" %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
            >>                                                %! rill.ScoreTemplate.__call__()
            \context Staff = "Guitar"                         %! rill.ScoreTemplate.__call__()
            <<                                                %! rill.ScoreTemplate.__call__()
                \context Voice = "Guitar_Markup_Voice"        %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
                \context Voice = "Guitar_Music_Voice"         %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
                \context Voice = "Guitar_Dynamics_Voice"      %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
            >>                                                %! rill.ScoreTemplate.__call__()
            \context Staff = "Viola"                          %! rill.ScoreTemplate.__call__()
            <<                                                %! rill.ScoreTemplate.__call__()
                \context Voice = "Viola_Markup_Voice"         %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
                \context Voice = "Viola_Music_Voice"          %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
                \context Voice = "Viola_Dynamics_Voice"       %! rill.ScoreTemplate.__call__()
                {                                             %! rill.ScoreTemplate.__call__()
                }                                             %! rill.ScoreTemplate.__call__()
            >>                                                %! rill.ScoreTemplate.__call__()
        >>                                                    %! rill.ScoreTemplate.__call__()
    }                                                         %! rill.ScoreTemplate.__call__()
>>                                                            %! rill.ScoreTemplate.__call__()

    """
    ### CLASS VARIABLES ###

    __documentation_section__ = None

    _always_make_global_rests = True

    _global_rests_in_topmost_staff = True

    def __init__(self):
        super(ScoreTemplate, self).__init__()
        self.voice_abbreviations.update(
            {"Fl.": "Flute_Music_Voice", "BbCl." : "Bb_Clarinet_Music_Voice",
                "Guit.": "Guitar_Voice", "Vla.": "Viola_Voice"
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
        abjad.annotate(viola_staff, "default_clef", abjad.Clef("alto"))

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
