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
                            \context Voice = "z"
                            {
                                \clef "treble"
                                r1
                                r2
                            }
                            \context Voice = "a"
                            {
                                <g' bf'>2
                                <fs' d''>2.
                                <f'' gf''>2.
                                <af' g''>1.
                                r2
                            }
                            \context Voice = "b"
                            {
                                <fs' d''>2
                                <f'' gf''>2.
                                <af' g''>2.
                                <g'' bf''>1.
                                r2
                            }
                            \context Voice = "c"
                            {
                                <f'' gf''>2
                                <af' g''>2.
                                <g'' bf''>2.
                                <fs'' d'''>1.
                                r2
                            }
                            \context Voice = "y"
                            {
                                r2
                                r1
                                r1
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
                                <af, ef>1
                                <af, g>1.
                                <g bf>1.
                                <g c'>\breve.
                                r1
                            }
                            \context Voice = "b"
                            {
                                <af, g>1
                                <g bf>1.
                                <g c'>1.
                                <af ef'>\breve.
                                r1
                            }
                            \context Voice = "c"
                            {
                                <g bf>1
                                <g c'>1.
                                <af ef'>1.
                                <af g'>\breve.
                                r1
                            }
                            \context Voice = "d"
                            {
                                <g c'>1
                                <af ef'>1.
                                <af g'>1.
                                <g' bf'>\breve.
                                r1
                            }
                        }                                                      %! rill.ScoreTemplate.__call__()
                    >>                                                         %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            }                                                                  %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
