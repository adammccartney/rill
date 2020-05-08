C_Global_Rests = {                                                             %! abjad.Path.extern()
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


C_Global_Skips = {                                                             %! abjad.Path.extern()
    \time 4/4
    \override Script.staff-padding = 4
    \override TextScript.staff-padding = 4
    \override TextSpanner.staff-padding = 4.75
    s1 * 1
    - \abjad-dashed-line-with-arrow
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \large
                    \upright
                        accel.
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
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
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
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \stopTextSpan
    - \abjad-invisible-line
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
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
    s1 * 1
    \time 4/4
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
    \time 4/4
    s1 * 1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \abjad-metronome-mark-markup #2 #0 #1 #"27"
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
}                                                                              %! abjad.Path.extern()


C_Viola_I_Markup_Voice = {                                                     %! abjad.Path.extern()
    \clef "alto"
    \override TextScript.staff-padding = 1.5
    \override TextSpanner.staff-padding = 2.25
    s1 * 42/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "sustain until m.130"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
}                                                                              %! abjad.Path.extern()


C_Viola_I_Music_Voice = {                                                      %! abjad.Path.extern()
    d'\longa * 21/2
}                                                                              %! abjad.Path.extern()


C_Viola_I_Dynamics_Voice = {                                                   %! abjad.Path.extern()
    s1 * 42/1
    \!
}                                                                              %! abjad.Path.extern()


C_Viola_I = <<                                                                 %! abjad.Path.extern()
    \context Voice = "Viola_I_Markup_Voice"                                    %! ins_wasser.ScoreTemplate.__call__()
    \C_Viola_I_Markup_Voice                                                    %! abjad.Path.extern()
    \context Voice = "Viola_I_Music_Voice"                                     %! ins_wasser.ScoreTemplate.__call__()
    \C_Viola_I_Music_Voice                                                     %! abjad.Path.extern()
    \context Voice = "Viola_I_Dynamics_Voice"                                  %! ins_wasser.ScoreTemplate.__call__()
    \C_Viola_I_Dynamics_Voice                                                  %! abjad.Path.extern()
>>                                                                             %! abjad.Path.extern()


C_Viola_II_Markup_Voice = {                                                    %! abjad.Path.extern()
    \clef "alto"
    s1 * 2/1
    \override TextScript.staff-padding = 2
    \override TextSpanner.staff-padding = 2.75
    s1 * 4/1
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
    s1 * 4/1
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
    s1 * 3/2
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
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "pT + XFB flaut."
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 3/2
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
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "PO + XFB flaut."
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 3/2
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
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "pP + XFB flaut."
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 3/2
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
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "P + XFB flaut."
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 3/2
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
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "MP + XFB flaut."
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 3/2
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
    \override TextScript.staff-padding = 3
    \override TextSpanner.staff-padding = 3.75
    s1 * 4/1
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
    s1 * 1/4
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "XP + full bow strokes"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    \stopTextSpan
    - \abjad-dashed-line-with-arrow
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    XP
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    1/3OB
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
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
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    2/3OB
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
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
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "OB (no pitch)"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


C_Viola_II_Music_Voice = {                                                     %! abjad.Path.extern()
    \override Score.BarLine.transparent = ##t
    d'\breve
    d'\longa
    d'\longa
    d'1.
    d'1
    d'1.
    d'1
    d'1.
    d'1
    d'1.
    d'1
    d'1.
    d'1
    d'1.
    d'\breve
    d'\longa
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
    d'4
    - \downbow
    d'4
    - \upbow
}                                                                              %! abjad.Path.extern()


C_Viola_II_Dynamics_Voice = {                                                  %! abjad.Path.extern()
    s1 * 2/1
    s1 * 4/1
    s1 * 4/1
    s1 * 3/2
    s1 * 1/1
    s1 * 3/2
    s1 * 1/1
    s1 * 3/2
    s1 * 1/1
    s1 * 3/2
    s1 * 1/1
    s1 * 3/2
    s1 * 1/1
    s1 * 3/2
    s1 * 2/1
    s1 * 4/1
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    s1 * 1/4
    \!
}                                                                              %! abjad.Path.extern()


C_Viola_II = <<                                                                %! abjad.Path.extern()
    \context Voice = "Viola_II_Markup_Voice"                                   %! ins_wasser.ScoreTemplate.__call__()
    \C_Viola_II_Markup_Voice                                                   %! abjad.Path.extern()
    \context Voice = "Viola_II_Music_Voice"                                    %! ins_wasser.ScoreTemplate.__call__()
    \C_Viola_II_Music_Voice                                                    %! abjad.Path.extern()
    \context Voice = "Viola_II_Dynamics_Voice"                                 %! ins_wasser.ScoreTemplate.__call__()
    \C_Viola_II_Dynamics_Voice                                                 %! abjad.Path.extern()
>>                                                                             %! abjad.Path.extern()
