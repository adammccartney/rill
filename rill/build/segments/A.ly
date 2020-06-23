\version "2.20.0"   %! abjad.LilyPondFile._get_format_pieces()
\language "english" %! abjad.LilyPondFile._get_format_pieces()

#(ly:set-option 'relative-includes #t)

\include "../../stylesheets/stylesheet.ily" %! abjad.LilyPondFile._get_formatted_includes()

\header { %! abjad.LilyPondFile._get_formatted_blocks()
    title = ##f
    composer = ##f
} %! abjad.LilyPondFile._get_formatted_blocks()

\score { %! abjad.LilyPondFile._get_formatted_blocks()
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
                    {
                        ef'2
                        g'2
                        ~
                        g'4
                        bf'2.
                        c''1.
                        r2
                    }
                    {
                        g'2
                        bf'2
                        ~
                        bf'4
                        c''2.
                        ef''1.
                        r2
                    }
                    {
                        bf'2
                        c''2
                        ~
                        c''4
                        ef''2.
                        g''1.
                        r2
                    }
                    {
                        c''2
                        ef''2
                        ~
                        ef''4
                        g''2.
                        bf''1.
                        r2
                    }
                    {
                        ef'2
                        g'2
                        ~
                        g'4
                        bf'2.
                        c''1.
                        r2
                    }
                    {
                        g'2
                        bf'2
                        ~
                        bf'4
                        c''2.
                        ef''1.
                        r2
                    }
                    {
                        bf'2
                        c''2
                        ~
                        c''4
                        ef''2.
                        g''1.
                        r2
                    }
                    {
                        c''2
                        ef''2
                        ~
                        ef''4
                        g''2.
                        bf''1.
                        r2
                    }
                } %! rill.ScoreTemplate.__call__()
                \context Voice = "Violin_Dynamics_Voice" %! rill.ScoreTemplate.__call__()
                {                                        %! rill.ScoreTemplate.__call__()
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    \!
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    \!
                } %! rill.ScoreTemplate.__call__()
            >> %! rill.ScoreTemplate.__call__()
            \context Staff = "MonoSynth" %! rill.ScoreTemplate.__call__()
            <<                           %! rill.ScoreTemplate.__call__()
                \context Voice = "MonoSynth_Markup_Voice" %! rill.ScoreTemplate.__call__()
                {                                         %! rill.ScoreTemplate.__call__()
                } %! rill.ScoreTemplate.__call__()
                \context Voice = "MonoSynth_Music_Voice" %! rill.ScoreTemplate.__call__()
                {                                        %! rill.ScoreTemplate.__call__()
                    {
                        ef'2
                        g'2
                        ~
                        g'4
                        bf'2.
                        c''1.
                        r2
                    }
                    {
                        ef'2
                        g'2
                        ~
                        g'4
                        bf'2.
                        c''1.
                        r2
                    }
                } %! rill.ScoreTemplate.__call__()
                \context Voice = "MonoSynth_Dynamics_Voice" %! rill.ScoreTemplate.__call__()
                {                                           %! rill.ScoreTemplate.__call__()
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    \!
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 3/2
                    s1 * 1/2
                    \!
                } %! rill.ScoreTemplate.__call__()
            >> %! rill.ScoreTemplate.__call__()
            \context MusicContext = "PolySynth_Music_Context" %! rill.ScoreTemplate.__call__()
            {                                                 %! rill.ScoreTemplate.__call__()
                \context PolySynthMusicStaffGroup = "PolySynth_Music_Staff_Group" %! rill.ScoreTemplate.__call__()
                <<                                                                %! rill.ScoreTemplate.__call__()
                    \context PolySynthRHStaff = "PolySynth_Music_RH_Staff" %! rill.ScoreTemplate.__call__()
                    <<                                                     %! rill.ScoreTemplate.__call__()
                        \context Voice = "RH_I_Markup_Voice" %! rill.ScoreTemplate.__call__()
                        {                                    %! rill.ScoreTemplate.__call__()
                        } %! rill.ScoreTemplate.__call__()
                        \context Voice = "RH_I_Music_Voice" %! rill.ScoreTemplate.__call__()
                        {                                   %! rill.ScoreTemplate.__call__()
                            {
                                ef'2
                                g'2
                                ~
                                g'4
                                bf'2.
                                c''1.
                                r2
                            }
                            {
                                ef'2
                                g'2
                                ~
                                g'4
                                bf'2.
                                c''1.
                                r2
                            }
                        } %! rill.ScoreTemplate.__call__()
                        \context Voice = "RH_I_Dynamics_Voice" %! rill.ScoreTemplate.__call__()
                        {                                      %! rill.ScoreTemplate.__call__()
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            \!
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            \!
                        } %! rill.ScoreTemplate.__call__()
                    >> %! rill.ScoreTemplate.__call__()
                    \context PolySynthLHStaff = "PolySynth_Music_LH_Staff" %! rill.ScoreTemplate.__call__()
                    <<                                                     %! rill.ScoreTemplate.__call__()
                        \context Voice = "LH_I_Markup_Voice" %! rill.ScoreTemplate.__call__()
                        {                                    %! rill.ScoreTemplate.__call__()
                        } %! rill.ScoreTemplate.__call__()
                        \context Voice = "LH_I_Music_Voice" %! rill.ScoreTemplate.__call__()
                        {                                   %! rill.ScoreTemplate.__call__()
                            {
                                ef'2
                                g'2
                                ~
                                g'4
                                bf'2.
                                c''1.
                                r2
                            }
                            {
                                g'2
                                bf'2
                                ~
                                bf'4
                                c''2.
                                ef''1.
                                r2
                            }
                            {
                                bf'2
                                c''2
                                ~
                                c''4
                                ef''2.
                                g''1.
                                r2
                            }
                            {
                                c''2
                                ef''2
                                ~
                                ef''4
                                g''2.
                                bf''1.
                                r2
                            }
                            {
                                ef'2
                                g'2
                                ~
                                g'4
                                bf'2.
                                c''1.
                                r2
                            }
                            {
                                g'2
                                bf'2
                                ~
                                bf'4
                                c''2.
                                ef''1.
                                r2
                            }
                            {
                                bf'2
                                c''2
                                ~
                                c''4
                                ef''2.
                                g''1.
                                r2
                            }
                            {
                                c''2
                                ef''2
                                ~
                                ef''4
                                g''2.
                                bf''1.
                                r2
                            }
                        } %! rill.ScoreTemplate.__call__()
                        \context Voice = "LH_I_Dynamics_Voice" %! rill.ScoreTemplate.__call__()
                        {                                      %! rill.ScoreTemplate.__call__()
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            \!
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 3/2
                            s1 * 1/2
                            \!
                        } %! rill.ScoreTemplate.__call__()
                    >> %! rill.ScoreTemplate.__call__()
                >> %! rill.ScoreTemplate.__call__()
            } %! rill.ScoreTemplate.__call__()
        >> %! rill.ScoreTemplate.__call__()
    >> %! rill.ScoreTemplate.__call__()
} %! abjad.LilyPondFile._get_formatted_blocks()