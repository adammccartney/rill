B_Global_Rests = {                                                             %! abjad.Path.extern()
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


B_Global_Skips = {                                                             %! abjad.Path.extern()
    \time 4/4
    \override Script.staff-padding = 8
    \override TextScript.staff-padding = 8
    \override TextSpanner.staff-padding = 8.75
    s1 * 1
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \abjad-metronome-mark-markup #2 #0 #1 #"72"
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
                \abjad-metronome-mark-markup #2 #0 #1 #"18"
                \hspace
                    #0.5
            }
        }
    \startTextSpan
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
    \stopTextSpan
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
    \stopTextSpan
    - \abjad-invisible-line
    - \tweak bound-details.left.text \markup {
        \concat
            {
                \abjad-metronome-mark-markup #2 #0 #1 #"72"
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
}                                                                              %! abjad.Path.extern()


B_Viola_I_Markup_Voice = {                                                     %! abjad.Path.extern()
    \clef "alto"
    \override TextScript.staff-padding = 2.5
    \override TextSpanner.staff-padding = 3.25
    s1 * 2/1
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
    s1 * 1/1
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
    s1 * 3/2
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
    s1 * 1/2
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
    s1 * 3/2
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
    s1 * 1/1
    s1 * 3/2
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
    s1 * 1/2
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
    s1 * 3/2
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
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


B_Viola_I_Music_Voice = {                                                      %! abjad.Path.extern()
    <fs' a'>\breve
    <e' g'>1
    <d' fs'>1
    <fs' a'>\breve
    <fs' a'>\breve
    <fs' a'>1
    <fs' a'>1.
    <fs' a'>1.
    <fs' a'>1.
    <fs' a'>2
    <fs' a'>1.
    a'1.
    a'1
    a'1.
    a'1.
    a'2
    a'1.
    a'1.
    a'1.
    <fs' a'>\breve
    <fs' a'>1
    <e' g'>1
    <d' fs'>\breve
}                                                                              %! abjad.Path.extern()


B_Viola_I_Dynamics_Voice = {                                                   %! abjad.Path.extern()
    \override DynamicLineSpanner.staff-padding = 2
    s1 * 2/1
    \mp
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    \p
    s1 * 2/1
    s1 * 1/1
    s1 * 3/2
    \p
    \<
    s1 * 3/2
    \mp
    s1 * 3/2
    \mp
    \<
    s1 * 1/2
    \mf
    s1 * 3/2
    \mf
    \<
    s1 * 3/2
    \f
    s1 * 1/1
    \ff
    s1 * 3/2
    s1 * 3/2
    \f
    \>
    s1 * 1/2
    \mf
    s1 * 3/2
    \mf
    \>
    s1 * 3/2
    \mp
    s1 * 3/2
    \mp
    \>
    s1 * 2/1
    \p
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    \!
}                                                                              %! abjad.Path.extern()


B_Viola_I = <<                                                                 %! abjad.Path.extern()
    \context Voice = "Viola_I_Markup_Voice"                                    %! ins_wasser.ScoreTemplate.__call__()
    \B_Viola_I_Markup_Voice                                                    %! abjad.Path.extern()
    \context Voice = "Viola_I_Music_Voice"                                     %! ins_wasser.ScoreTemplate.__call__()
    \B_Viola_I_Music_Voice                                                     %! abjad.Path.extern()
    \context Voice = "Viola_I_Dynamics_Voice"                                  %! ins_wasser.ScoreTemplate.__call__()
    \B_Viola_I_Dynamics_Voice                                                  %! abjad.Path.extern()
>>                                                                             %! abjad.Path.extern()


B_Viola_II_Markup_Voice = {                                                    %! abjad.Path.extern()
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
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
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
    s1 * 3/2
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
    s1 * 1/2
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
    s1 * 3/2
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
    s1 * 1/1
    s1 * 3/2
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
    s1 * 1/2
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
    s1 * 3/2
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
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    \stopTextSpan
}                                                                              %! abjad.Path.extern()


B_Viola_II_Music_Voice = {                                                     %! abjad.Path.extern()
    \override Score.BarLine.transparent = ##t
    d'1
    cs'1
    a1
    d'1
    d'1
    cs'1
    <b ds'>\breve
    <b ds'>1.
    <b ds'>1.
    <b ds'>1.
    <b ds'>2
    <b ds'>1.
    b1.
    b1
    b1.
    b1.
    b2
    b1.
    b1.
    b1.
    b1
    <b ds'>\breve
    cs'1
    <a cs'>1
    d'\breve
}                                                                              %! abjad.Path.extern()


B_Viola_II_Dynamics_Voice = {                                                  %! abjad.Path.extern()
    \override DynamicLineSpanner.staff-padding = 2
    s1 * 1/1
    \mp
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    s1 * 1/1
    \p
    s1 * 1/1
    s1 * 2/1
    \override DynamicLineSpanner.staff-padding = 3
    s1 * 3/2
    \p
    \<
    s1 * 3/2
    \mp
    s1 * 3/2
    \mp
    \<
    s1 * 1/2
    \mf
    s1 * 3/2
    \mf
    \<
    s1 * 3/2
    \f
    s1 * 1/1
    \ff
    s1 * 3/2
    s1 * 3/2
    \f
    \>
    s1 * 1/2
    \mf
    s1 * 3/2
    \mf
    \>
    s1 * 3/2
    \mp
    s1 * 3/2
    \mp
    \>
    s1 * 1/1
    \p
    s1 * 2/1
    s1 * 1/1
    s1 * 1/1
    s1 * 2/1
    \!
}                                                                              %! abjad.Path.extern()


B_Viola_II = <<                                                                %! abjad.Path.extern()
    \context Voice = "Viola_II_Markup_Voice"                                   %! ins_wasser.ScoreTemplate.__call__()
    \B_Viola_II_Markup_Voice                                                   %! abjad.Path.extern()
    \context Voice = "Viola_II_Music_Voice"                                    %! ins_wasser.ScoreTemplate.__call__()
    \B_Viola_II_Music_Voice                                                    %! abjad.Path.extern()
    \context Voice = "Viola_II_Dynamics_Voice"                                 %! ins_wasser.ScoreTemplate.__call__()
    \B_Viola_II_Dynamics_Voice                                                 %! abjad.Path.extern()
>>                                                                             %! abjad.Path.extern()
