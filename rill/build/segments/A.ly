    \context Score = "Score"                                                   %! rill.ScoreTemplate.__call__()
    <<                                                                         %! rill.ScoreTemplate.__call__()
        \context GlobalContext = "Global_Context"                              %! abjad.ScoreTemplate._make_global_context()
        <<                                                                     %! abjad.ScoreTemplate._make_global_context()
            \context GlobalRests = "Global_Rests"                              %! abjad.ScoreTemplate._make_global_context()
            {                                                                  %! abjad.ScoreTemplate._make_global_context()
            }                                                                  %! abjad.ScoreTemplate._make_global_context()
            \context GlobalSkips = "Global_Skips"                              %! abjad.ScoreTemplate._make_global_context()
            {                                                                  %! abjad.ScoreTemplate._make_global_context()
            }                                                                  %! abjad.ScoreTemplate._make_global_context()
        >>                                                                     %! abjad.ScoreTemplate._make_global_context()
        \context MusicContext = "Music_Context"                                %! rill.ScoreTemplate.__call__()
        <<                                                                     %! rill.ScoreTemplate.__call__()
            \context Staff = "Violin"                                          %! rill.ScoreTemplate.__call__()
            <<                                                                 %! rill.ScoreTemplate.__call__()
                \context Voice = "Violin_Music_Voice"                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    \context Voice = "a"
                    {
                        \clef "treble"
                        r\breve
                    }
                    \context Voice = "b"
                    {
                        r\breve
                    }
                    \context Voice = "c"
                    {
                        r\breve
                    }
                    \context Voice = "d"
                    {
                        r\breve
                    }
                    \context Voice = "e"
                    {
                        r\breve
                    }
                    \context Voice = "f"
                    {
                        r\breve
                    }
                    \context Voice = "g"
                    {
                        r\breve
                    }
                    \context Voice = "h"
                    {
                        r\breve
                    }
                    \context Voice = "i"
                    {
                        r\breve
                    }
                    \context Voice = "j"
                    {
                        r\breve
                    }
                }                                                              %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
            \context Staff = "Monosynth"                                       %! rill.ScoreTemplate.__call__()
            <<                                                                 %! rill.ScoreTemplate.__call__()
                \context Voice = "Monosynth_Music_Voice"                       %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    \context Voice = "a"
                    {
                        \clef "treble"
                        r\breve
                    }
                    \context Voice = "b"
                    {
                        r\breve
                    }
                    \context Voice = "c"
                    {
                        r\breve
                    }
                    \context Voice = "d"
                    {
                        r\breve
                    }
                    \context Voice = "e"
                    {
                        r\breve
                    }
                    \context Voice = "f"
                    {
                        r\breve
                    }
                    \context Voice = "g"
                    {
                        r\breve
                    }
                    \context Voice = "h"
                    {
                        r\breve
                    }
                    \context Voice = "i"
                    {
                        r\breve
                    }
                    \context Voice = "j"
                    {
                        r\breve
                    }
                }                                                              %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
            \context MusicContext = "Polysynth_Music_Context"                  %! rill.ScoreTemplate.__call__()
            {                                                                  %! rill.ScoreTemplate.__call__()
                \context PolySynthMusicStaffGroup = "PolySynth_Music_Staff_Group" %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Staff = "RH_Polysynth"                            %! rill.ScoreTemplate.__call__()
                    <<                                                         %! rill.ScoreTemplate.__call__()
                        \context Voice = "RH_I_Music_Voice"                    %! rill.ScoreTemplate.__call__()
                        {                                                      %! rill.ScoreTemplate.__call__()
                            \context Voice = "a"
                            {
                                \clef "treble"
                                g''\breve
                                f''\breve
                                bf'\breve
                                d''\longa
                            }
                        }                                                      %! rill.ScoreTemplate.__call__()
                    >>                                                         %! rill.ScoreTemplate.__call__()
                    \context Staff = "LH_Polysynth"                            %! rill.ScoreTemplate.__call__()
                    <<                                                         %! rill.ScoreTemplate.__call__()
                        \context Voice = "LH_I_Music_Voice"                    %! rill.ScoreTemplate.__call__()
                        {                                                      %! rill.ScoreTemplate.__call__()
                            \context Voice = "a"
                            {
                                \clef "bass"
                                <ef bf>\longa
                                <g d'>\longa
                                <c' g'>\longa
                                <bf f'>\longa
                            }
                            \context Voice = "b"
                            {
                                <g d'>\longa
                                <bf f'>\longa
                                <ef' bf'>\longa
                                <c' g'>\longa
                            }
                            \context Voice = "c"
                            {
                                <bf f'>\longa
                                <c' g'>\longa
                                <g d'>\longa
                                <ef bf>\longa
                            }
                            \context Voice = "d"
                            {
                                <c' g'>\longa
                                <bf f'>\longa
                                <ef bf>\longa
                                <g d'>\longa
                            }
                        }                                                      %! rill.ScoreTemplate.__call__()
                    >>                                                         %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            }                                                                  %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
