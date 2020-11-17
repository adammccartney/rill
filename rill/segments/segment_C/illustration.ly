\version "2.20.0"                                                              %! abjad.LilyPondFile._get_format_pieces()
\language "english"                                                            %! abjad.LilyPondFile._get_format_pieces()

#(ly:set-option 'relative-includes #t)

\include "../../stylesheets/stylesheet.ily"                                    %! abjad.LilyPondFile._get_formatted_includes()

\header {                                                                      %! abjad.LilyPondFile._get_formatted_blocks()
    title = ##f
    composer = ##f
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()

\score {                                                                       %! abjad.LilyPondFile._get_formatted_blocks()
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
                            \mark #3
                            d''4
                            \p
                            ~
                            d''8
                            e''8
                            d''4
                            ~
                            d''8
                            e''8
                            d''4
                            e''4
                            ~
                            e''8
                            d''8
                            e''4
                            ~
                            e''8
                            d''8
                            e''4
                            d''4
                            ~
                            d''8
                            e''8
                            d''4
                            ~
                            d''8
                            e''8
                            d''4
                            e''4
                            ~
                            e''8
                            d''8
                            e''4
                            ~
                            e''8
                            d''8
                            e''4
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
                            \mark #3
                            d'4
                            \p
                            ~
                            d'8
                            e'8
                            d'4
                            ~
                            d'8
                            e'8
                            d'4
                            e'4
                            ~
                            e'8
                            d'8
                            e'4
                            ~
                            e'8
                            d'8
                            e'4
                            d'4
                            ~
                            d'8
                            e'8
                            d'4
                            ~
                            d'8
                            e'8
                            d'4
                            e'4
                            ~
                            e'8
                            d'8
                            e'4
                            ~
                            e'8
                            d'8
                            e'4
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
                            \mark #3
                            a''8
                            \p
                            b''8
                            ~
                            b''8
                            r8
                            r4
                            a''4
                            ~
                            a''4
                            b''8
                            a''8
                            ~
                            a''8
                            r8
                            r4
                            b''2
                            a''8
                            b''8
                            ~
                            b''8
                            r8
                            r4
                            a''4
                            ~
                            a''4
                            b''8
                            a''8
                            ~
                            a''8
                            r8
                            r4
                            b''2
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
                            \mark #3
                            a'4
                            \p
                            ~
                            a'8
                            b'8
                            a'4
                            ~
                            a'8
                            b'8
                            a'4
                            b'4
                            ~
                            b'8
                            a'8
                            b'4
                            ~
                            b'8
                            a'8
                            b'4
                            a'4
                            ~
                            a'8
                            b'8
                            a'4
                            ~
                            a'8
                            b'8
                            a'4
                            b'4
                            ~
                            b'8
                            a'8
                            b'4
                            ~
                            b'8
                            a'8
                            b'4
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
                            \mark #3
                            a''4
                            \pp
                            ~
                            a''8
                            gs''8
                            ~
                            gs''4
                            ~
                            gs''8
                            f''8
                            ~
                            f''4
                            gs''4
                            ~
                            gs''8
                            a''8
                            ~
                            a''4
                            ~
                            a''8
                            gs''8
                            ~
                            gs''4
                            f''4
                            ~
                            f''8
                            gs''8
                            ~
                            gs''4
                            ~
                            gs''8
                            a''8
                            ~
                            a''4
                            gs''4
                            ~
                            gs''8
                            f''8
                            ~
                            f''4
                            ~
                            f''8
                            gs''8
                            ~
                            gs''4
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
                            \mark #3
                            a''16
                            \pp
                            gs''16
                            r8
                            r4
                            f''16
                            gs''16
                            a''16
                            gs''16
                            r4
                            r8
                            f''16
                            gs''16
                            a''16
                            gs''16
                            r8
                            r8
                            r8
                            f''16
                            gs''16
                            a''16
                            gs''16
                            r4
                            r16
                            r16
                            f''16
                            gs''16
                            a''16
                            gs''16
                            r8
                            r4
                            f''16
                            gs''16
                            a''16
                            gs''16
                            r4
                            r8
                            f''16
                            gs''16
                            a''16
                            gs''16
                            r8
                            r8
                            r8
                            f''16
                            gs''16
                            a''16
                            gs''16
                            r4
                            r16
                            r16
                            f''16
                            gs''16
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
                            \mark #3
                            a''2
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            f''2
                            r2.
                            r2.
                            r1
                            r2
                            b''4
                            ~
                            b''4
                            d'''2
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
                            \mark #3
                            a''2
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            f''2
                            r2.
                            r2.
                            r1
                            r2
                            b''4
                            ~
                            b''4
                            d'''2
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
                            \mark #3
                            a''2
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            f''2
                            r2.
                            r2.
                            r1
                            r2
                            b''4
                            ~
                            b''4
                            d'''2
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
                            \mark #3
                            a'2
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            f'2
                            r2.
                            r2.
                            r1
                            r2
                            b'4
                            ~
                            b'4
                            d''2
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
                            \once \override NoteHead.style = #'cross
                            \clef "treble"
                            \mark #3
                            a'1
                            \ppp
                            ^ \markup {
                                \upright
                                    \center-column
                                        {
                                            flaut.-
                                            pont.
                                        }
                                }
                            ~
                            \once \override NoteHead.style = #'cross
                            a'2.
                            ~
                            \once \override NoteHead.style = #'cross
                            a'2.
                            ~
                            \once \override NoteHead.style = #'cross
                            a'1
                            ~
                            \once \override NoteHead.style = #'cross
                            a'2.
                            ~
                            \once \override NoteHead.style = #'cross
                            a'2.
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
                            \mark #3
                            d'''4
                            \ppp
                            ~
                            d'''8
                            e'''8
                            d'''4
                            ~
                            d'''8
                            e'''8
                            d'''4
                            e'''4
                            ~
                            e'''8
                            d'''8
                            e'''4
                            ~
                            e'''8
                            d'''8
                            e'''4
                            d'''4
                            ~
                            d'''8
                            e'''8
                            d'''4
                            ~
                            d'''8
                            e'''8
                            d'''4
                            e'''4
                            ~
                            e'''8
                            d'''8
                            e'''4
                            ~
                            e'''8
                            d'''8
                            e'''4
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
                            \mark #3
                            a''4
                            \ppp
                            ~
                            a''8
                            b''8
                            a''4
                            ~
                            a''8
                            b''8
                            a''4
                            b''4
                            ~
                            b''8
                            a''8
                            b''4
                            ~
                            b''8
                            a''8
                            b''4
                            a''4
                            ~
                            a''8
                            b''8
                            a''4
                            ~
                            a''8
                            b''8
                            a''4
                            b''4
                            ~
                            b''8
                            a''8
                            b''4
                            ~
                            b''8
                            a''8
                            b''4
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
                            \mark #3
                            a'4
                            \ppp
                            ~
                            a'8
                            gs'8
                            a'4
                            ~
                            a'8
                            gs'8
                            a'4
                            gs'4
                            ~
                            gs'8
                            a'8
                            gs'4
                            ~
                            gs'8
                            a'8
                            gs'4
                            a'4
                            ~
                            a'8
                            gs'8
                            a'4
                            ~
                            a'8
                            gs'8
                            a'4
                            gs'4
                            ~
                            gs'8
                            a'8
                            gs'4
                            ~
                            gs'8
                            a'8
                            gs'4
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
                            \mark #3
                            a4
                            \ppp
                            ~
                            a8
                            gs8
                            a4
                            ~
                            a8
                            gs8
                            a4
                            gs4
                            ~
                            gs8
                            a8
                            gs4
                            ~
                            gs8
                            a8
                            gs4
                            a4
                            ~
                            a8
                            gs8
                            a4
                            ~
                            a8
                            gs8
                            a4
                            gs4
                            ~
                            gs8
                            a8
                            gs4
                            ~
                            gs8
                            a8
                            gs4
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()