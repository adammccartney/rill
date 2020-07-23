%#(set-default-paper-size "A4")
#(set-global-staff-size 14)

\include "/home/adam/mccartney/mccartney/lilypond/mccartney.ily"
\include "contexts.ily"
\include "markups.ily"

\paper {
    system-system-spacing = 
        #'((basic-distance . 24) 
           (minimum-distance . 18) 
           (padding . 4))
    score-system-spacing =
        #'((basic-distance . 12)
           (minimum-distance . 12)
           (padding . 1)
           (stretchability . 12))
    system-separator-markup = \slashSeparator
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
        "Adam McCartney (*1987)"
    tagline = \markup \null
    title = \markup \column {
        \center-align {
            \override #'(font-name . "Palatino Italic")
            \fontsize #12
            "rill"
            \vspace #1.25
            \override #'(font-name . "Palatino Italic")
            \fontsize #5
            "for flutes, clarinets, guitar and viola"
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
