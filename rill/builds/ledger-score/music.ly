% rill (2020) for flute, clarinet, guitar and viola

\version "2.20.0"
\language "english"

#(ly:set-option 'relative-includes #t)
\include "../stylesheets/stylesheet.ily"

\score {
    {
   \include "segment-a.ly"
   \include "segment-b.ly"
   \include "segment-b2.ly"
   \include "segment-b3.ly"
   \include "segment-c.ly"
   \include "segment-d.ly"
   \include "semgent-e.ly"
    }
}
