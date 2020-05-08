%%% BOW SPEED & POSITION %%%

ins-wasser-clicks-one-two-sec = \markup "clicks (1-2/sec)"

ins-wasser-half-ob = \markup "1/2OB"

ins-wasser-mp-xfb-flaut = \markup "MP + XFB flaut."

ins-wasser-ob-no-pitch = \markup "OB (no pitch)"

ins-wasser-one-third-ob = \markup "1/3OB"

ins-wasser-p-xfb-flaut = \markup "P + XFB flaut."

ins-wasser-po-fb-flaut = \markup "PO + FB flaut."
ins-wasser-po-nbs = \markup "PO + NBS"
ins-wasser-po-scratch = \markup "PO + scratch"
ins-wasser-po-slow-bow = \markup "PO + slow bow"
ins-wasser-po-xfb-flaut = \markup "PO + XFB flaut."

ins-wasser-pp-xfb-flaut = \markup "pP + XFB flaut."

ins-wasser-pt-xfb-flaut = \markup "pT + XFB flaut."

ins-wasser-tasto-fb-flaut = \markup "tasto + FB flaut."
ins-wasser-tasto-nbs = \markup "tasto + NBS"
ins-wasser-tasto-scratch = \markup "tasto + scratch"
ins-wasser-tasto-slow-bow = \markup "tasto + slow bow"
ins-wasser-tasto-xfb-flaut = \markup "tasto + XFB flaut."

ins-wasser-trans = \markup "trans."

ins-wasser-two-thirds-ob = \markup "2/3OB"

ins-wasser-xp = \markup "XP"
ins-wasser-xp-full-bow-strokes = \markup "XP + full bow strokes"
ins-wasser-xp-xfb-flaut = \markup "XP + XFB flaut."

%%% COLOPHON %%%

ins-wasser-colophon-markup = \markup {
    \override #'(font-name . "Palatino")
    \with-color #black
    \override #'(baseline-skip . 4)
    \right-column {
        \line { Cambridge, Mass. }
        \line { Nov. \hspace #0.75 – \hspace #0.75 Dec. 2014. }
        }
    }

%%% MARGIN MARKUP %%%

ins-wasser-viola-i-markup = \markup \hcenter-in #12 "Viola I"
ins-wasser-va-i-markup = \markup \hcenter-in #10 "Va. I"

ins-wasser-viola-ii-markup = \markup \hcenter-in #12 "Viola II"
ins-wasser-va-ii-markup = \markup \hcenter-in #10 "Va. II"

%%% MISCELLANEOUS %%%

ins-wasser-repeat-eight = \markup
    \with-dimensions-from \null
    \override #'(box-padding . 0.5)
    \box
    \fontsize #6
    \bold
    \sans
    x8
