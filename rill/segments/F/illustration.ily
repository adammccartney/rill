F_Global_Rests = {                                                             %! abjad.Path.extern()
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
    R1 * 1
}                                                                              %! abjad.Path.extern()


F_Global_Skips = {                                                             %! abjad.Path.extern()
    \time 4/4
    \override Script.staff-padding = 6
    \override TextScript.staff-padding = 6
    \override TextSpanner.staff-padding = 6.75
    s1 * 1
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \abjad-metronome-mark-markup #2 #0 #1 #"108"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    \override Script.staff-padding = 2
    \override TextScript.staff-padding = 2
    \override TextSpanner.staff-padding = 2.75
    s1 * 1
    \fermata
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    \override Script.staff-padding = 6
    \override TextScript.staff-padding = 6
    \override TextSpanner.staff-padding = 6.75
    s1 * 1
    \stopTextSpan
    - \abjad-dashed-line-with-arrow
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \large
                    \upright
                        rit.
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \stopTextSpan
    - \abjad-dashed-line-with-arrow
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \abjad-metronome-mark-markup #2 #0 #1 #"54"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \abjad-metronome-mark-markup #2 #0 #1 #"108"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    \override Script.staff-padding = 2
    \override TextScript.staff-padding = 2
    \override TextSpanner.staff-padding = 2.75
    s1 * 1
    \fermata
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


F_Viola_I_Markup_Voice = {                                                     %! abjad.Path.extern()
    \clef "alto"
    \override TextScript.staff-padding = 2
    \override TextSpanner.staff-padding = 2.75
    s1 * 1/1
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "tasto + FB flaut."
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    s1 * 2/1
    s1 * 2/1
    s1 * 2/1
    \stopTextSpan
    - \abjad-dashed-line-with-arrow
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    trans.
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 2/1
    \stopTextSpan
    - \abjad-dashed-line-with-arrow
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "tasto + slow bow"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "tasto + XFB flaut."
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    s1 * 2/1
    s1 * 2/1
    s1 * 4/1
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


F_Viola_I_Music_Voice = {                                                      %! abjad.Path.extern()
    \override Score.BarLine.transparent = ##t
    <fs' a'>1
    <e' g'>1
    <d' fs'>1
    <d' fs'>\breve
    <fs' a'>\breve
    <e' g'>\breve
    <d' fs'>\breve
    <d' fs'>\breve
    <fs' a'>1
    <fs' a'>1
    <fs' a'>1
    <fs' a'>1
    <e' g'>1
    <d' fs'>\breve
    <d' fs'>\breve
    <e' g'>\breve
    <d' fs'>\longa
}                                                                              %! abjad.Path.extern()


F_Viola_I_Dynamics_Voice = {                                                   %! abjad.Path.extern()
    \override DynamicLineSpanner.staff-padding = 2
    s1 * 1/1
    \mp
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    s1 * 2/1
    \p
    \>
    s1 * 2/1
    s1 * 2/1
    \ppp
    \<
    s1 * 2/1
    \f
    \>
    s1 * 1/1
    \ppp
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    s1 * 2/1
    \ppppp
    s1 * 2/1
    s1 * 4/1
    \!
}                                                                              %! abjad.Path.extern()


F_Viola_I = <<                                                                 %! abjad.Path.extern()
    \context Voice = "Viola_I_Markup_Voice"                                    %! ins_wasser.ScoreTemplate.__call__()
    \F_Viola_I_Markup_Voice                                                    %! abjad.Path.extern()
    \context Voice = "Viola_I_Music_Voice"                                     %! ins_wasser.ScoreTemplate.__call__()
    \F_Viola_I_Music_Voice                                                     %! abjad.Path.extern()
    \context Voice = "Viola_I_Dynamics_Voice"                                  %! ins_wasser.ScoreTemplate.__call__()
    \F_Viola_I_Dynamics_Voice                                                  %! abjad.Path.extern()
>>                                                                             %! abjad.Path.extern()


F_Viola_II_Markup_Voice = {                                                    %! abjad.Path.extern()
    \clef "alto"
    \override TextScript.staff-padding = 1.5
    \override TextSpanner.staff-padding = 2.25
    s1 * 1/1
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "tasto + FB flaut."
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    s1 * 2/1
    s1 * 2/1
    s1 * 2/1
    \stopTextSpan
    - \abjad-dashed-line-with-arrow
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    trans.
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 2/1
    \stopTextSpan
    - \abjad-dashed-line-with-arrow
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "tasto + slow bow"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "tasto + XFB flaut."
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    s1 * 2/1
    s1 * 2/1
    s1 * 4/1
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


F_Viola_II_Music_Voice = {                                                     %! abjad.Path.extern()
    d'1
    fs'1
    a1
    d'\breve
    d'\breve
    a\breve
    b\breve
    b\breve
    d'1
    fs'1
    <bs fs'>1
    fs'1
    <a fs'>1
    d'\breve
    d'\breve
    a\breve
    b\longa
}                                                                              %! abjad.Path.extern()


F_Viola_II_Dynamics_Voice = {                                                  %! abjad.Path.extern()
    \override DynamicLineSpanner.staff-padding = 2
    s1 * 1/1
    \mp
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    s1 * 2/1
    \p
    \>
    s1 * 2/1
    s1 * 2/1
    \ppp
    \<
    s1 * 2/1
    \f
    \>
    s1 * 1/1
    \ppp
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    s1 * 2/1
    \ppppp
    s1 * 2/1
    s1 * 4/1
    \!
}                                                                              %! abjad.Path.extern()


F_Viola_II = <<                                                                %! abjad.Path.extern()
    \context Voice = "Viola_II_Markup_Voice"                                   %! ins_wasser.ScoreTemplate.__call__()
    \F_Viola_II_Markup_Voice                                                   %! abjad.Path.extern()
    \context Voice = "Viola_II_Music_Voice"                                    %! ins_wasser.ScoreTemplate.__call__()
    \F_Viola_II_Music_Voice                                                    %! abjad.Path.extern()
    \context Voice = "Viola_II_Dynamics_Voice"                                 %! ins_wasser.ScoreTemplate.__call__()
    \F_Viola_II_Dynamics_Voice                                                 %! abjad.Path.extern()
>>                                                                             %! abjad.Path.extern()
