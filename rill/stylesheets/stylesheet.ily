#(set-default-paper-size "letter" 'portrait)
#(set-global-staff-size 14)

\include "./_stylesheets/abjad.ily"
\include "contexts.ily"

\paper {
    system-system-spacing = 
        #'((basic-distance . 24) 
           (minimum-distance . 15) 
           (padding . 15))
    score-system-spacing =
        #'((basic-distance . 14)
           (minimum-distance . 14)
           (padding . 4)
           (stretchability . 6))
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
            "for violin, monosynth and polysynth"
        }
    }
}

\layout {
    \accidentalStyle neo-modern
    indent = 0
    ragged-bottom = ##t
    ragged-last = ##t
    ragged-right = ##t
    \context {
      \Staff
      \name FluteOneStaff
      \alias Staff
      instrumentName = "flute1"
      shortInstrumentName = "fl.1"
    }
    \context {
      \Staff
      \name FluteThreeStaff
      \alias Staff
      instrumentName = "flute2"
      shortInstrumentName = "fl.2"
    }
    \context {
      \Staff
      \name FluteFourStaff
      \alias Staff
      instrumentName = "flute4"
      shortInstrumentName = "fl.4"
    }
    \context {
      \Staff
      \name BbclarinetOneStaff
      \alias Staff
      instrumentName = "Bb Clarinet"
      shortInstrumentName = "cl."
    }
    \context {
      \StaffGroup
      \name WoodwindStaffGroup
      \alias StaffGroup
      \accepts FluteOneStaff
      \accepts FluteTwoStaff
      \accepts FluteThreeStaff
      \accepts FluteFourStaff
      \accepts BbclarinetOneStaff
    }
    \context {
      \Staff
      \name VibraphoneStaff
      \alias Staff
      instrumentName = "vibraphone"
      shortInstrumentName = "vibes."
    }
    \context {
     \StaffGroup
     \name PercussionStaffGroup
     \alias StaffGroup
     \accepts VibraphoneStaff
     }
     \context {
      \Staff
      \name ViolinOneStaff
      \alias Staff
      instrumentName = "Violin1"
      shortInstrumentName = "vn.1"
    }
     \context {
      \Staff
      \name ViolinTwoStaff
      \alias Staff
      instrumentName = "Violin2"
      shortInstrumentName = "vn.2"
    }
     \context {
      \Staff
      \name ViolinThreeStaff
      \alias Staff
      instrumentName = "Violin3"
      shortInstrumentName = "vn.3"
    }
     \context {
      \Staff
      \name ViolinFourStaff
      \alias Staff
      instrumentName = "Violin4"
      shortInstrumentName = "vn.4"
    }
     \context {
      \Staff
      \name ViolinFiveStaff
      \alias Staff
      instrumentName = "Violin5"
      shortInstrumentName = "vn.5"
    }
     \context {
      \Staff
      \name ViolinSixStaff
      \alias Staff
      instrumentName = "Violin6"
      shortInstrumentName = "vn.6"
    }
     \context {
      \Staff
      \name ViolinSevenStaff
      \alias Staff
      instrumentName = "Violin7"
      shortInstrumentName = "vn.7"
    }
     \context {
      \Staff
      \name ViolinEightStaff
      \alias Staff
      instrumentName = "Violin8"
      shortInstrumentName = "vn.8"
    }
     \context {
      \Staff
      \name ViolaStaff
      \alias Staff
      instrumentName = "Viola"
      shortInstrumentName = "va."
    }
    \context {
      \StaffGroup
      \name StringsStaffGroup
      \alias StaffGroup
      \accept ViolinOneStaff
      \accept ViolinTwoStaff
      \accept ViolinThreeStaff
      \accept ViolinFourStaff
      \accept ViolinFiveStaff
      \accept ViolinSixStaff
      \accept ViolinSevenStaff
      \accept ViolinEightStaff
      \accept ViolaStaff
    }
}

