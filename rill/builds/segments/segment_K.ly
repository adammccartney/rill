    \context Score = "Score"                                                   %! rill.ScoreTemplate.__call__()
    \with                                                                      %! rill.ScoreTemplate.__call__()
    {                                                                          %! rill.ScoreTemplate.__call__()
        markFormatter = #format-mark-box-alphabet                              %! rill.ScoreTemplate.__call__()
    }                                                                          %! rill.ScoreTemplate.__call__()
    <<                                                                         %! rill.ScoreTemplate.__call__()
        \context GlobalContext = "Global_Context"                              %! abjad.ScoreTemplate._make_global_context()
        <<                                                                     %! abjad.ScoreTemplate._make_global_context()
            \context GlobalSkips = "Global_Skips"                              %! abjad.ScoreTemplate._make_global_context()
            {                                                                  %! abjad.ScoreTemplate._make_global_context()
                \time 4/4
                s1 * 1
                \time 3/4
                s1 * 3/4
                \time 3/4
                s1 * 3/4
                \time 4/4
                s1 * 1
                \time 3/4
                s1 * 3/4
                \time 3/4
                s1 * 3/4
            }                                                                  %! abjad.ScoreTemplate._make_global_context()
            \context GlobalRests = "Global_Rests"                              %! abjad.ScoreTemplate._make_global_context()
            {                                                                  %! abjad.ScoreTemplate._make_global_context()
                R1 * 1
                R1 * 3/4
                R1 * 3/4
                R1 * 1
                R1 * 3/4
                R1 * 3/4
            }                                                                  %! abjad.ScoreTemplate._make_global_context()
        >>                                                                     %! abjad.ScoreTemplate._make_global_context()
        \context MusicContext = "Music_Context"                                %! rill.ScoreTemplate.__call__()
        <<                                                                     %! rill.ScoreTemplate.__call__()
            \context WoodwindStaffGroup = "Woodwind_Staff_Group"               %! rill.ScoreTemplate.__call__()
            <<                                                                 %! rill.ScoreTemplate.__call__()
                \tag #'fluteOne
                \context FluteOneStaff = "Flute1"                              %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute1_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            r4
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            d'''4
                            r2
                            \once \override NoteHead.style = #'cross
                            e'''2.
                            r2.
                            r2
                            \once \override NoteHead.style = #'cross
                            d'''4
                            ~
                            \once \override NoteHead.style = #'cross
                            d'''4
                            ~
                            \once \override NoteHead.style = #'cross
                            d'''2.
                            ~
                            \once \override NoteHead.style = #'cross
                            d'''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'fluteTwo
                \context FluteTwoStaff = "Flute2"                              %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            r4
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            a''4
                            r2
                            \once \override NoteHead.style = #'cross
                            b''2.
                            r2.
                            r2
                            \once \override NoteHead.style = #'cross
                            a''4
                            ~
                            \once \override NoteHead.style = #'cross
                            a''4
                            ~
                            \once \override NoteHead.style = #'cross
                            a''2.
                            ~
                            \once \override NoteHead.style = #'cross
                            a''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'fluteThree
                \context FluteThreeStaff = "Flute3"                            %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute3_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            r4
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            gs''4
                            r2
                            \once \override NoteHead.style = #'cross
                            a''2.
                            r2.
                            r2
                            \once \override NoteHead.style = #'cross
                            gs''4
                            ~
                            \once \override NoteHead.style = #'cross
                            gs''4
                            ~
                            \once \override NoteHead.style = #'cross
                            gs''2.
                            ~
                            \once \override NoteHead.style = #'cross
                            gs''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'fluteFour
                \context FluteFourStaff = "Flute4"                             %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute4_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            r4
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            a'4
                            r2
                            \once \override NoteHead.style = #'cross
                            gs'2.
                            r2.
                            r2
                            \once \override NoteHead.style = #'cross
                            a'4
                            ~
                            \once \override NoteHead.style = #'cross
                            a'4
                            ~
                            \once \override NoteHead.style = #'cross
                            a'2.
                            ~
                            \once \override NoteHead.style = #'cross
                            a'2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'BbclarinetOne
                \context BbclarinetOneStaff = "Bbclarinet1"                    %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"Bbclarinet"                             %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Music_Voice"                 %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            d'1
                            \f
                            a2.
                            d'2.
                            ~
                            d'2
                            e'4
                            ~
                            e'4
                            ~
                            e'4
                            gs'2
                            fs'2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
            \context PercussionStaffGroup = "Percussion_Staff_Group"           %! rill.ScoreTemplate.__call__()
            <<                                                                 %! rill.ScoreTemplate.__call__()
                \tag #'vibraphone
                \context VibraphoneStaff = "Vibraphone"                        %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"vibraphone"                             %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Vibraphone_Music_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            r8
                            \ppp
                            a'8
                            r4
                            gs'4
                            ~
                            gs'8
                            r8
                            r2
                            a'8
                            ~
                            a'8
                            ~
                            a'2.
                            r8
                            gs'8
                            r4
                            a'4
                            ~
                            a'8
                            r8
                            r2
                            gs'8
                            ~
                            gs'8
                            ~
                            gs'2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
            \context StringStaffGroup = "String_Staff_Group"                   %! rill.ScoreTemplate.__call__()
            <<                                                                 %! rill.ScoreTemplate.__call__()
                \tag #'violinOne
                \context ViolinOneStaff = "Violin1"                            %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin1_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            a'''8
                            \pp
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            b'''8
                            r8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinTwo
                \context ViolinTwoStaff = "Violin2"                            %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            a'''8
                            \pp
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            b'''8
                            r8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                            r8
                            a'''8
                            b'''8
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinThree
                \context ViolinThreeStaff = "Violin3"                          %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin3_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            a''16
                            \pp
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinFour
                \context ViolinFourStaff = "Violin4"                           %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            a''16
                            \pp
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinFive
                \context ViolinFiveStaff = "Violin5"                           %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin5_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            a''16
                            \pp
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                            a''16
                            f''16
                            r16
                            b''16
                            d'''16
                            r16
                            cs'''16
                            fs'''16
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinSix
                \context ViolinSixStaff = "Violin6"                            %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            r4
                            \ppp
                            ^ \markup {
                                \upright
                                    flautando
                                }
                            d'''4
                            r2
                            e'''2.
                            r2.
                            r2
                            d'''4
                            ~
                            d'''4
                            ~
                            d'''2.
                            ~
                            d'''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinSeven
                \context ViolinSevenStaff = "Violin7"                          %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            r4
                            \ppp
                            ^ \markup {
                                \upright
                                    flautando
                                }
                            a'''4
                            r2
                            b'''2.
                            r2.
                            r2
                            a'''4
                            ~
                            a'''4
                            ~
                            a'''2.
                            ~
                            a'''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinEight
                \context ViolinEightStaff = "Violin8"                          %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin8_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "treble"
                            \mark #11
                            r4
                            \ppp
                            ^ \markup {
                                \upright
                                    flautando
                                }
                            gs''4
                            r2
                            a''2.
                            r2.
                            r2
                            gs''4
                            ~
                            gs''4
                            ~
                            gs''2.
                            ~
                            gs''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'viola
                \context ViolaStaff = "Viola"                                  %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"viola"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Viola_Music_Voice"                       %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \clef "alto"
                            \mark #11
                            r4
                            \ppp
                            ^ \markup {
                                \upright
                                    flautando
                                }
                            a4
                            r2
                            gs2.
                            r2.
                            r2
                            a4
                            ~
                            a4
                            ~
                            a2.
                            ~
                            a2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()