E_Global_Rests = {                                                             %! abjad.Path.extern()
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
    R1 * 1/4
}                                                                              %! abjad.Path.extern()


E_Global_Skips = {                                                             %! abjad.Path.extern()
    \time 4/4
    \override Script.staff-padding = 11
    \override TextScript.staff-padding = 11
    \override TextSpanner.staff-padding = 11.75
    s1 * 1
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \abjad-metronome-mark-markup #2 #0 #1 #"36"
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
    \time 1/4
    \override Script.staff-padding = 2
    \override TextScript.staff-padding = 2
    \override TextSpanner.staff-padding = 2.75
    s1 * 1/4
    \fermata
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


E_Viola_I_Markup_Voice = {                                                     %! abjad.Path.extern()
    \clef "alto"
    \override TextScript.staff-padding = 2.5
    \override TextSpanner.staff-padding = 3.25
    s1 * 1/4
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "tasto + NBS"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/4
    s1 * 1/2
    s1 * 1/4
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    s1 * 1/4
    s1 * 1/4
    s1 * 1/2
    s1 * 1/4
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    s1 * 1/4
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    \override TextScript.staff-padding = 1.5
    \override TextSpanner.staff-padding = 2.25
    s1 * 2/1
    \stopTextSpan
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
    s1 * 2/1
    s1 * 2/1
    s1 * 1/4
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


E_Viola_I_Music_Voice = {                                                      %! abjad.Path.extern()
    \repeat volta 8
    {
        \override Score.BarLine.transparent = ##f
        <cs' e'>4
        <cs' e'>4
        r2
        \revert Score.BarLine.transparent
    }
    <as d'>4
    <as d'>4
    r2
    r1
    <cs' e'>4
    <cs' e'>4
    r2
    <b d'>4
    <b d'>4
    r2
    r1
    <b d'>4
    <b d'>4
    r2
    r1
    <a es'>\breve
    <g es'>\breve
    <fs d'>\breve
    r4
}                                                                              %! abjad.Path.extern()


E_Viola_I_Dynamics_Voice = {                                                   %! abjad.Path.extern()
    \override DynamicLineSpanner.staff-padding = 4
    s1 * 1/4
    \mf
    s1 * 1/4
    s1 * 1/2
    \override DynamicLineSpanner.staff-padding = 2
    s1 * 1/4
    \mp
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    s1 * 1/4
    \mf
    s1 * 1/4
    s1 * 1/2
    s1 * 1/4
    \mp
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    s1 * 1/4
    \mp
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    \override DynamicLineSpanner.staff-padding = 2
    s1 * 2/1
    \p
    \<
    s1 * 2/1
    \mf
    s1 * 2/1
    \mf
    \>
    s1 * 1/4
    \mp
}                                                                              %! abjad.Path.extern()


E_Viola_I = <<                                                                 %! abjad.Path.extern()
    \context Voice = "Viola_I_Markup_Voice"                                    %! ins_wasser.ScoreTemplate.__call__()
    \E_Viola_I_Markup_Voice                                                    %! abjad.Path.extern()
    \context Voice = "Viola_I_Music_Voice"                                     %! ins_wasser.ScoreTemplate.__call__()
    \E_Viola_I_Music_Voice                                                     %! abjad.Path.extern()
    \context Voice = "Viola_I_Dynamics_Voice"                                  %! ins_wasser.ScoreTemplate.__call__()
    \E_Viola_I_Dynamics_Voice                                                  %! abjad.Path.extern()
>>                                                                             %! abjad.Path.extern()


E_Viola_II_Markup_Voice = {                                                    %! abjad.Path.extern()
    \clef "alto"
    \override TextScript.staff-padding = 2.5
    \override TextSpanner.staff-padding = 3.25
    s1 * 1/4
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "tasto + NBS"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/4
    s1 * 1/2
    s1 * 1/4
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    s1 * 1/4
    s1 * 1/4
    s1 * 1/2
    s1 * 1/4
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    s1 * 1/4
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    \override TextScript.staff-padding = 1.5
    \override TextSpanner.staff-padding = 2.25
    s1 * 3/1
    \stopTextSpan
    - \abjad-dashed-line-with-arrow
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
    s1 * 3/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "XP + XFB flaut."
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/4
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


E_Viola_II_Music_Voice = {                                                     %! abjad.Path.extern()
    \repeat volta 8
    {
        \override Score.BarLine.transparent = ##f
        <e a>4
        <e a>4
        r2
        \revert Score.BarLine.transparent
    }
    <e g>4
    <e g>4
    r2
    r1
    <e a>4
    <e a>4
    r2
    <e gs>4
    <e gs>4
    r2
    r1
    <gs a>4
    <gs a>4
    r2
    r1
    a\breve.
    a\breve.
    r4
}                                                                              %! abjad.Path.extern()


E_Viola_II_Dynamics_Voice = {                                                  %! abjad.Path.extern()
    \override DynamicLineSpanner.staff-padding = 3.5
    s1 * 1/4
    \mf
    s1 * 1/4
    s1 * 1/2
    s1 * 1/4
    \mp
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    s1 * 1/4
    \mf
    s1 * 1/4
    s1 * 1/2
    s1 * 1/4
    \mp
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    \override DynamicLineSpanner.staff-padding = 2.5
    s1 * 1/4
    \mp
    s1 * 1/4
    s1 * 1/2
    s1 * 1/1
    \override DynamicLineSpanner.staff-padding = 2
    s1 * 3/1
    \pp
    \<
    s1 * 3/1
    \mf
    \>
    s1 * 1/4
    \ppp
}                                                                              %! abjad.Path.extern()


E_Viola_II = <<                                                                %! abjad.Path.extern()
    \context Voice = "Viola_II_Markup_Voice"                                   %! ins_wasser.ScoreTemplate.__call__()
    \E_Viola_II_Markup_Voice                                                   %! abjad.Path.extern()
    \context Voice = "Viola_II_Music_Voice"                                    %! ins_wasser.ScoreTemplate.__call__()
    \E_Viola_II_Music_Voice                                                    %! abjad.Path.extern()
    \context Voice = "Viola_II_Dynamics_Voice"                                 %! ins_wasser.ScoreTemplate.__call__()
    \E_Viola_II_Dynamics_Voice                                                 %! abjad.Path.extern()
>>                                                                             %! abjad.Path.extern()
