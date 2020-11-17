\version "2.20.0"
\language "english"

#(ly:set-option 'relative-includes #t)
\include "../../stylesheets/stylesheet.ily"

#(set-default-paper-size "a3" 'portrait)
#(set-global-staff-size 21)

\layout {
}

\paper {
}

\score {
    \header {piece = "Largo"}
    \include "../segments.ily"
}
