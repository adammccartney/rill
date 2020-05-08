D_Global_Rests = {                                                             %! abjad.Path.extern()
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
    R1 * 1/4
}                                                                              %! abjad.Path.extern()


D_Global_Skips = {                                                             %! abjad.Path.extern()
    \time 4/4
    \override Script.staff-padding = 6
    \override TextScript.staff-padding = 6
    \override TextSpanner.staff-padding = 6.75
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
    \override Script.staff-padding = 4
    \override TextScript.staff-padding = 4
    \override TextSpanner.staff-padding = 4.75
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


D_Viola_I_Markup_Voice = {                                                     %! abjad.Path.extern()
    \clef "alto"
    \override TextScript.staff-padding = 2
    \override TextSpanner.staff-padding = 2.75
    s1 * 3/2
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
    s1 * 3/2
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "PO + FB flaut."
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
    s1 * 3/2
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "PO + NBS"
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
    s1 * 3/2
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "PO + slow bow"
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
    s1 * 3/2
    s1 * 1/1
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "PO + scratch"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 4/1
    s1 * 6/1
    s1 * 1/4
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


D_Viola_I_Music_Voice = {                                                      %! abjad.Path.extern()
    d'1.
    \glissando
    cqs'1
    \parenthesize
    dtqf'1.
    \glissando
    c'1
    \parenthesize
    c'1.
    \glissando
    bqs1
    \parenthesize
    cqf'1.
    \glissando
    b1
    \parenthesize
    b1.
    \glissando
    bqf1
    \parenthesize
    atqs1.
    \glissando
    as1
    \parenthesize
    bf1.
    \glissando
    aqs1
    \parenthesize
    btqf1.
    \glissando
    a1
    a\longa
    a\longa.
    r4
}                                                                              %! abjad.Path.extern()


D_Viola_I_Dynamics_Voice = {                                                   %! abjad.Path.extern()
    \override DynamicLineSpanner.staff-padding = 2
    s1 * 3/2
    \pp
    \<
    s1 * 1/1
    \p
    s1 * 3/2
    \p
    \<
    s1 * 1/1
    \mp
    s1 * 3/2
    \mp
    \<
    s1 * 1/1
    \mf
    \override DynamicLineSpanner.staff-padding = 2.5
    s1 * 3/2
    \mf
    \<
    s1 * 1/1
    \f
    s1 * 3/2
    \f
    \<
    s1 * 1/1
    s1 * 3/2
    s1 * 1/1
    \ff
    s1 * 3/2
    \ff
    \<
    s1 * 1/1
    s1 * 3/2
    s1 * 1/1
    \fff
    s1 * 4/1
    s1 * 6/1
    s1 * 1/4
    \!
}                                                                              %! abjad.Path.extern()


D_Viola_I = <<                                                                 %! abjad.Path.extern()
    \context Voice = "Viola_I_Markup_Voice"                                    %! ins_wasser.ScoreTemplate.__call__()
    \D_Viola_I_Markup_Voice                                                    %! abjad.Path.extern()
    \context Voice = "Viola_I_Music_Voice"                                     %! ins_wasser.ScoreTemplate.__call__()
    \D_Viola_I_Music_Voice                                                     %! abjad.Path.extern()
    \context Voice = "Viola_I_Dynamics_Voice"                                  %! ins_wasser.ScoreTemplate.__call__()
    \D_Viola_I_Dynamics_Voice                                                  %! abjad.Path.extern()
>>                                                                             %! abjad.Path.extern()


D_Viola_II_Markup_Voice = {                                                    %! abjad.Path.extern()
    \clef "alto"
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
    \override TextScript.staff-padding = 1.5
    \override TextSpanner.staff-padding = 2.25
    s1 * 1/1
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
    s1 * 3/2
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
    s1 * 3/2
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
    s1 * 3/2
    \stopTextSpan
    - \abjad-dashed-line-with-arrow
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "tasto + scratch"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 3/2
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \upright
                    "clicks (1-2/sec.)"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
    s1 * 1/4
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


D_Viola_II_Music_Voice = {                                                     %! abjad.Path.extern()
    \override Score.BarLine.transparent = ##t
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
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as4
    - \downbow
    as4
    - \upbow
    as1
    as\longa
    as1.
    as1.
    as1.
    as1.
    \override Score.BarLine.transparent = ##f
    r4
}                                                                              %! abjad.Path.extern()


D_Viola_II_Dynamics_Voice = {                                                  %! abjad.Path.extern()
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
    \override DynamicLineSpanner.staff-padding = 2.5
    s1 * 1/1
    \mf
    \>
    s1 * 4/1
    s1 * 3/2
    \p
    \<
    s1 * 3/2
    s1 * 3/2
    \mf
    s1 * 3/2
    s1 * 1/4
    \!
}                                                                              %! abjad.Path.extern()


D_Viola_II = <<                                                                %! abjad.Path.extern()
    \context Voice = "Viola_II_Markup_Voice"                                   %! ins_wasser.ScoreTemplate.__call__()
    \D_Viola_II_Markup_Voice                                                   %! abjad.Path.extern()
    \context Voice = "Viola_II_Music_Voice"                                    %! ins_wasser.ScoreTemplate.__call__()
    \D_Viola_II_Music_Voice                                                    %! abjad.Path.extern()
    \context Voice = "Viola_II_Dynamics_Voice"                                 %! ins_wasser.ScoreTemplate.__call__()
    \D_Viola_II_Dynamics_Voice                                                 %! abjad.Path.extern()
>>                                                                             %! abjad.Path.extern()
