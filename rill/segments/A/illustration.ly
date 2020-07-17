\version "2.18.2"                                                              %! abjad.LilyPondFile._get_format_pieces()
\language "english"                                                            %! abjad.LilyPondFile._get_format_pieces()

#(ly:set-option 'relative-includes #t)

\include "../../stylesheets/stylesheet.ily"                                    %! abjad.LilyPondFile._get_formatted_includes()

\header {                                                                      %! abjad.LilyPondFile._get_formatted_blocks()
    title = ##f
    composer = ##f
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()

\score {                                                                       %! abjad.LilyPondFile._get_formatted_blocks()
    \context Score = "Score"                                                   %! rill.ScoreTemplate.__call__()
    <<                                                                         %! rill.ScoreTemplate.__call__()
        \context MusicContext = "Music_Context"                                %! rill.ScoreTemplate.__call__()
        <<                                                                     %! rill.ScoreTemplate.__call__()
            \context Staff = "Violin"                                          %! rill.ScoreTemplate.__call__()
            <<                                                                 %! rill.ScoreTemplate.__call__()
                \context Voice = "Violin_Markup_Voice"                         %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    \override TextScript.staff-padding = 1.5
                    \override TextSpanner.staff-padding = 2.25
                    s1 * 1/1
                    - \abjad-invisible-line
                    - \tweak bound-details.left.text \markup {
                        \concat
                            {
                                \upright
                                    "sul tasto"
                                \hspace
                                    #0.5
                            }
                        }
                    \startTextSpan
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    \stopTextSpan
                }                                                              %! rill.ScoreTemplate.__call__()
                \context Voice = "Violin_Music_Voice"                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    \clef "treble"
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                }                                                              %! rill.ScoreTemplate.__call__()
                \context Voice = "Violin_Dynamics_Voice"                       %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    \once \override Hairpin.stencil = #constante-hairpin
                    \override DynamicLineSpanner.staff-padding = 2.5
                    s1 * 1/1
                    \ppp
                    \<
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    \mf
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    \!
                }                                                              %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
            \context Staff = "Monosynth"                                       %! rill.ScoreTemplate.__call__()
            <<                                                                 %! rill.ScoreTemplate.__call__()
                \context Voice = "Monosynth_Markup_Voice"                      %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    \stopTextSpan
                }                                                              %! rill.ScoreTemplate.__call__()
                \context Voice = "Monosynth_Music_Voice"                       %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    \clef "treble"
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                }                                                              %! rill.ScoreTemplate.__call__()
                \context Voice = "Monosynth_Dynamics_Voice"                    %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    \!
                }                                                              %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
            \context MusicContext = "Polysynth_Music_Context"                  %! rill.ScoreTemplate.__call__()
            {                                                                  %! rill.ScoreTemplate.__call__()
                \context PolySynthMusicStaffGroup = "PolySynth_Music_Staff_Group" %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Staff = "RH_Polysynth"                            %! rill.ScoreTemplate.__call__()
                    <<                                                         %! rill.ScoreTemplate.__call__()
                        \context Voice = "RH_I_Markup_Voice"                   %! rill.ScoreTemplate.__call__()
                        {                                                      %! rill.ScoreTemplate.__call__()
                            s1 * 1/1
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 3/4
                            s1 * 1/4
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            \stopTextSpan
                        }                                                      %! rill.ScoreTemplate.__call__()
                        \context Voice = "RH_I_Music_Voice"                    %! rill.ScoreTemplate.__call__()
                        {                                                      %! rill.ScoreTemplate.__call__()
                            \clef "treble"
                            r1
                            r2
                            g2
                            ~
                            <ef g>2.
                            ~
                            <ef g c'>4
                            ~
                            <ef g c'>2
                            ~
                            <ef g bf c'>2
                            ~
                            <ef g bf c'>1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                        }                                                      %! rill.ScoreTemplate.__call__()
                        \context Voice = "RH_I_Dynamics_Voice"                 %! rill.ScoreTemplate.__call__()
                        {                                                      %! rill.ScoreTemplate.__call__()
                            s1 * 1/1
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 3/4
                            s1 * 1/4
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            \!
                        }                                                      %! rill.ScoreTemplate.__call__()
                    >>                                                         %! rill.ScoreTemplate.__call__()
                    \context Staff = "LH_Polysynth"                            %! rill.ScoreTemplate.__call__()
                    <<                                                         %! rill.ScoreTemplate.__call__()
                        \context Voice = "LH_I_Markup_Voice"                   %! rill.ScoreTemplate.__call__()
                        {                                                      %! rill.ScoreTemplate.__call__()
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 1/1
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            \stopTextSpan
                        }                                                      %! rill.ScoreTemplate.__call__()
                        \context Voice = "LH_I_Music_Voice"                    %! rill.ScoreTemplate.__call__()
                        {                                                      %! rill.ScoreTemplate.__call__()
                            \clef "bass"
                            g2
                            ~
                            <ef g>2
                            ~
                            <ef g>4
                            ~
                            <ef g c'>2.
                            ~
                            <ef g bf c'>1
                            ~
                            <ef g bf c'>2
                            r2
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                            r1
                        }                                                      %! rill.ScoreTemplate.__call__()
                        \context Voice = "LH_I_Dynamics_Voice"                 %! rill.ScoreTemplate.__call__()
                        {                                                      %! rill.ScoreTemplate.__call__()
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 1/1
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            \!
                        }                                                      %! rill.ScoreTemplate.__call__()
                    >>                                                         %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            }                                                                  %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()