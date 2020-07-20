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
    \with                                                                      %! rill.ScoreTemplate.__call__()
    {                                                                          %! rill.ScoreTemplate.__call__()
        markFormatter = #format-mark-box-alphabet                              %! rill.ScoreTemplate.__call__()
    }                                                                          %! rill.ScoreTemplate.__call__()
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
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/1
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/1
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/4
                    \override TextScript.staff-padding = 1.5
                    \override TextSpanner.staff-padding = 2.25
                    s1 * 3/4
                    \stopTextSpan
                    - \abjad-invisible-line
                    - \tweak bound-details.left.text \markup {
                        \concat
                            {
                                \upright
                                    ord.
                                \hspace
                                    #0.5
                            }
                        }
                    \startTextSpan
                    s1 * 1/8
                    s1 * 1/8
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 1/1
                    \override TextScript.staff-padding = 3.5
                    \override TextSpanner.staff-padding = 4.25
                    s1 * 3/4
                    \stopTextSpan
                    - \abjad-invisible-line
                    - \tweak bound-details.left.text \markup {
                        \concat
                            {
                                \upright
                                    \center-column
                                        {
                                            flaut.-
                                            pont.
                                        }
                                \hspace
                                    #0.5
                            }
                        }
                    \startTextSpan
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/1
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/1
                    \override TextScript.staff-padding = 3.5
                    \override TextSpanner.staff-padding = 4.25
                    s1 * 1/2
                    \stopTextSpan
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
                    s1 * 1/2
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/1
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/4
                    \override TextScript.staff-padding = 3.5
                    \override TextSpanner.staff-padding = 4.25
                    s1 * 1/4
                    \stopTextSpan
                    - \abjad-invisible-line
                    - \tweak bound-details.left.text \markup {
                        \concat
                            {
                                \upright
                                    rhythmically
                                \hspace
                                    #0.5
                            }
                        }
                    \startTextSpan
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/4
                    \override TextScript.staff-padding = 1.5
                    \override TextSpanner.staff-padding = 2.25
                    s1 * 1/2
                    \stopTextSpan
                    - \abjad-invisible-line
                    - \tweak bound-details.left.text \markup {
                        \concat
                            {
                                \upright
                                    flautando
                                \hspace
                                    #0.5
                            }
                        }
                    \startTextSpan
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    \stopTextSpan
                }                                                              %! rill.ScoreTemplate.__call__()
                \context Voice = "Violin_Music_Voice"                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    \clef "treble"
                    \mark #1
                    r1
                    r2
                    d''2
                    ~
                    d''1
                    ~
                    d''2
                    bf'2
                    ~
                    bf'1
                    ~
                    bf'1
                    ~
                    bf'2
                    ~
                    f''2
                    ~
                    f''1
                    ~
                    f''4
                    g''2.
                    ~
                    g''1
                    r1
                    r4
                    g'2.
                    ~
                    g'8
                    r8
                    g''2
                    bf'4
                    b'1
                    ef'1
                    c''2
                    ~
                    bf'2
                    ~
                    bf'4
                    ~
                    g''2.
                    ~
                    ef''1
                    ~
                    ef''2.
                    :32
                    r4
                    ef''2
                    ~
                    c''2
                    ~
                    c''1
                    r2
                    a''2
                    ~
                    a''1
                    ~
                    a''2
                    ef''2
                    ~
                    ef''1
                    ~
                    ef''1
                    ~
                    ef''2
                    ~
                    d'''2
                    ~
                    d'''1
                    ~
                    d'''4
                    fs''2.
                    ~
                    fs''1
                    r1
                    r1
                    r1
                    r4
                    a'4
                    a'2
                    bf'4
                    bf'4
                    bf'2
                    a'4
                    a'2
                    bf'4
                    bf'4
                    bf'2
                    ef''4
                    ef''2
                    d''4
                    d''4
                    d''2
                    ef''4
                    ef''2
                    bf'4
                    bf'4
                    bf'4
                    ~
                    bf'4
                    ef''4
                    ef''2
                    ~
                    ef''1
                    ~
                    ef''1
                    ~
                    ef''1
                    \bar "||"
                }                                                              %! rill.ScoreTemplate.__call__()
                \context Voice = "Violin_Dynamics_Voice"                       %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    s1 * 1/1
                    s1 * 1/2
                    \override DynamicLineSpanner.staff-padding = 2.5
                    s1 * 1/2
                    \ppp
                    s1 * 1/1
                    \<
                    s1 * 1/2
                    \override DynamicLineSpanner.staff-padding = 2.5
                    s1 * 1/2
                    \p
                    s1 * 1/1
                    \>
                    s1 * 1/1
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/1
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 1/1
                    \ppp
                    s1 * 1/1
                    s1 * 1/4
                    s1 * 3/4
                    \pp
                    s1 * 1/8
                    s1 * 1/8
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/1
                    s1 * 1/1
                    \mp
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    \>
                    s1 * 3/4
                    s1 * 1/1
                    s1 * 3/4
                    \ppp
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/1
                    \override DynamicLineSpanner.staff-padding = 2.5
                    s1 * 1/2
                    \ppp
                    s1 * 1/2
                    \<
                    s1 * 1/1
                    s1 * 1/2
                    \p
                    s1 * 1/2
                    \>
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/1
                    s1 * 1/4
                    s1 * 3/4
                    \ppp
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/4
                    s1 * 1/4
                    \pp
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/4
                    s1 * 1/2
                    \>
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    _ #(make-dynamic-script (markup #:whiteout #:normal-text #:italic "niente"))
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
                    \override TextScript.staff-padding = 1.5
                    \override TextSpanner.staff-padding = 2.25
                    s1 * 1/1
                    - \abjad-invisible-line
                    - \tweak bound-details.left.text \markup {
                        \concat
                            {
                                \upright
                                    \bold
                                        MX.
                                \hspace
                                    #0.5
                            }
                        }
                    \startTextSpan
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 1/8
                    s1 * 1/8
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 1/1
                    s1 * 3/4
                    s1 * 1/4
                    s1 * 1/2
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 1/1
                    s1 * 3/4
                    s1 * 1/4
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
                    \mark #1
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
                    r4
                    \clef "bass"
                    g2.
                    ~
                    g8
                    r8
                    g'2
                    bf4
                    b1
                    \clef "treble"
                    ef'1
                    :32
                    c'2
                    :32
                    ~
                    <bf c'>2
                    :32
                    ~
                    <bf c'>4
                    :32
                    ~
                    <bf c' g'>2.
                    :32
                    ~
                    <bf c' ef' g'>1
                    :32
                    ~
                    <bf c' ef' g'>2.
                    :32
                    r4
                    ef'2
                    :32
                    ~
                    <c' ef'>2
                    :32
                    ~
                    <c' ef'>4
                    :32
                    ~
                    <c' ef' bf'>2.
                    :32
                    ~
                    <c' ef' g' bf'>1
                    :32
                    ~
                    <c' ef' g' bf'>2.
                    :32
                    r4
                    r1
                    r1
                    r1
                    r1
                    r1
                    r1
                    \clef "bass"
                    <d a>1
                    :32
                    ~
                    <d a>1
                    :32
                    ~
                    <d a>1
                    :32
                    ~
                    <d a>1
                    :32
                    ~
                    <d a>1
                    :32
                    r1
                    r1
                    <a e'>1
                    :32
                    ~
                    <a e'>1
                    :32
                    ~
                    <a e'>1
                    :32
                    ~
                    <a e'>1
                    :32
                    ~
                    <a e'>1
                    :32
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
                    s1 * 1/4
                    s1 * 3/4
                    \ppp
                    s1 * 1/8
                    s1 * 1/8
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 1/1
                    s1 * 1/1
                    \>
                    s1 * 1/2
                    s1 * 1/2
                    \<
                    s1 * 1/4
                    s1 * 3/4
                    s1 * 1/1
                    \>
                    s1 * 3/4
                    \ppp
                    s1 * 1/4
                    s1 * 1/2
                    \<
                    s1 * 1/2
                    s1 * 1/4
                    s1 * 3/4
                    \>
                    s1 * 1/1
                    s1 * 3/4
                    _ #(make-dynamic-script (markup #:whiteout #:normal-text #:italic "niente"))
                    s1 * 1/4
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    s1 * 1/1
                    _ #(make-dynamic-script (markup #:whiteout #:normal-text #:italic "niente"))
                    s1 * 1/1
                    \<
                    s1 * 1/1
                    s1 * 1/1
                    \>
                    s1 * 1/1
                    s1 * 1/1
                    _ #(make-dynamic-script (markup #:whiteout #:normal-text #:italic "niente"))
                    s1 * 1/1
                    s1 * 1/1
                    _ #(make-dynamic-script (markup #:whiteout #:normal-text #:italic "niente"))
                    s1 * 1/1
                    \<
                    s1 * 1/1
                    \override DynamicLineSpanner.staff-padding = 3.5
                    s1 * 1/1
                    \>
                    s1 * 1/1
                    s1 * 1/1
                    _ #(make-dynamic-script (markup #:whiteout #:normal-text #:italic "niente"))
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
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/4
                            s1 * 3/4
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
                            \mark #1
                            r1
                            r2
                            d'''2
                            ~
                            <bf'' d'''>2.
                            ~
                            <bf'' d''' g'''>4
                            ~
                            <bf'' d''' g'''>2
                            ~
                            <bf'' d''' f''' g'''>2
                            ~
                            <bf'' d''' f''' g'''>1
                            ~
                            <d''' g''' bf'''>1
                            ~
                            <d''' g''' bf'''>2
                            ~
                            <d''' f''' g''' bf'''>2
                            ~
                            <d''' f''' g''' bf'''>1
                            ~
                            <d''' f''' g''' bf'''>4
                            ~
                            <g''' bf'''>2.
                            ~
                            bf'''1
                            ~
                            bf'''1
                            ~
                            bf'''1
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
                            \override DynamicLineSpanner.staff-padding = 2.5
                            s1 * 1/1
                            \ppp
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 3/4
                            s1 * 1/4
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/4
                            s1 * 3/4
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
                            s1 * 3/4
                            s1 * 1/4
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
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 3/4
                            s1 * 1/4
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/4
                            s1 * 3/4
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
                            \mark #1
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
                            <ef g bf c'>2.
                            r4
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
                            r2
                            a,2
                            ~
                            <ef, a,>2.
                            ~
                            <ef, fs, a,>4
                            ~
                            <ef, fs, a,>2
                            ~
                            <ef, fs, a, d>2
                            ~
                            <ef, fs, a, d>1
                            ~
                            <fs, a, d ef>1
                            ~
                            <fs, a, d ef>2
                            ~
                            <fs, a, d>2
                            ~
                            <fs, a, d>1
                            ~
                            <fs, a, d>4
                            ~
                            <fs, d>2.
                            ~
                            d1
                            r1
                            r1
                            <d a>1
                            ~
                            <d a>1
                            ~
                            <d a>1
                            ~
                            <d a>1
                            ~
                            <d a>1
                            r1
                            r1
                            <a e'>1
                            ~
                            <a e'>1
                            ~
                            <a e'>1
                            ~
                            <a e'>1
                            ~
                            <a e'>1
                            \bar "||"
                        }                                                      %! rill.ScoreTemplate.__call__()
                        \context Voice = "LH_I_Dynamics_Voice"                 %! rill.ScoreTemplate.__call__()
                        {                                                      %! rill.ScoreTemplate.__call__()
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/4
                            s1 * 3/4
                            s1 * 1/1
                            s1 * 3/4
                            s1 * 1/4
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
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 3/4
                            s1 * 1/4
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/2
                            s1 * 1/2
                            s1 * 1/1
                            s1 * 1/4
                            s1 * 3/4
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
                            \pp
                            s1 * 1/1
                            \>
                            s1 * 1/1
                            s1 * 1/1
                            s1 * 1/1
                            _ #(make-dynamic-script (markup #:whiteout #:normal-text #:italic "niente"))
                        }                                                      %! rill.ScoreTemplate.__call__()
                    >>                                                         %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            }                                                                  %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()