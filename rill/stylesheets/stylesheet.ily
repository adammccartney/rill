#(set-default-paper-size "11x17landscape")
#(set-global-staff-size 14)

\include "/Users/trevorbaca/baca/lilypond/baca.ily"
\include "contexts.ily"
\include "markups.ily"

\paper {
    bottom-margin = 7\mm
    evenFooterMarkup = \markup \fill-line {
        " "
        \concat {
            \bold \fontsize #3
            \on-the-fly #print-page-number-check-first
            \fromproperty #'page:page-number-string
            \hspace #15
        }
        " "
    }
    evenHeaderMarkup = \markup \null
    left-margin = 30\mm
    oddFooterMarkup = \markup \fill-line {
        " "
        \concat {
            \bold \fontsize #3
            \on-the-fly #print-page-number-check-first
            \fromproperty #'page:page-number-string
            \hspace #15
        }
        " "
    }
    oddHeaderMarkup = \markup \null
    print-first-page-number = ##f
    print-page-number = ##t
    ragged-bottom = ##t
    ragged-last-bottom = ##t
    right-margin = 30\mm
    top-margin = 12.5\mm
}

\header {
    composer = \markup 
        \override #'(font-name . "Palatino")
        \fontsize #5
        "Trevor Bača (*1975)"
    tagline = \markup \null
    title = \markup \column {
        \center-align {
            \override #'(font-name . "Palatino Italic")
            \fontsize #3
            "to Elizabeth Weisser & John Pickford Richards"
            \vspace #1.5
            \override #'(font-name . "Palatino")
            \fontsize #15 {
                \line { 
                    INS
                    \hspace #3
                    WASSER 
                    \hspace #4.5
                    \concat { EIN \hspace #-1.5 GESCHRIEBEN }
                }
            }
            \vspace #1.25
            \override #'(font-name . "Palatino Italic")
            \fontsize #3
            "for two violas"
        }
    }
}

\layout {
    \accidentalStyle neo-modern
    indent = 0
    ragged-bottom = ##t
    ragged-last = ##t
    ragged-right = ##t
}
