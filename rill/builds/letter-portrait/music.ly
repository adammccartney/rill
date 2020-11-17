\version "2.20.0"
\language "english"

#(ly:set-option 'relative-includes #t)
\include "../../stylesheets/stylesheet.ily"

#(set-default-paper-size "letter" 'portrait)
#(set-global-staff-size 15)

\layout {
}

\paper {
}

\score {
    \include "../segments.ily"
}
