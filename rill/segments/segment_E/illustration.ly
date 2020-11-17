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
                            \mark #5
                            cs'''8.
                            \mf
                            bf''16
                            ~
                            bf''8.
                            cs'''16
                            ~
                            cs'''8
                            bf''8
                            ~
                            bf''16
                            cs'''8.
                            ~
                            cs'''16
                            bf''8.
                            cs'''8.
                            bf''16
                            ~
                            bf''8.
                            cs'''16
                            ~
                            cs'''8
                            bf''8
                            ~
                            bf''16
                            cs'''8.
                            ~
                            cs'''16
                            bf''8.
                            cs'''8.
                            bf''16
                            ~
                            bf''8.
                            cs'''16
                            ~
                            cs'''8
                            bf''8
                            ~
                            bf''16
                            cs'''8.
                            ~
                            cs'''16
                            bf''8.
                            cs'''8.
                            bf''16
                            ~
                            bf''8.
                            cs'''16
                            ~
                            cs'''8
                            bf''8
                            ~
                            bf''16
                            cs'''8.
                            ~
                            cs'''16
                            bf''8.
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
                            \mark #5
                            f''8.
                            \mf
                            ef''16
                            ~
                            ef''8.
                            f''16
                            ~
                            f''8
                            ef''8
                            ~
                            ef''16
                            f''8.
                            ~
                            f''16
                            ef''8.
                            f''8.
                            ef''16
                            ~
                            ef''8.
                            f''16
                            ~
                            f''8
                            ef''8
                            ~
                            ef''16
                            f''8.
                            ~
                            f''16
                            ef''8.
                            f''8.
                            ef''16
                            ~
                            ef''8.
                            f''16
                            ~
                            f''8
                            ef''8
                            ~
                            ef''16
                            f''8.
                            ~
                            f''16
                            ef''8.
                            f''8.
                            ef''16
                            ~
                            ef''8.
                            f''16
                            ~
                            f''8
                            ef''8
                            ~
                            ef''16
                            f''8.
                            ~
                            f''16
                            ef''8.
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
                            \mark #5
                            cs'''2
                            \mf
                            a''2
                            r2.
                            r4
                            bf''2
                            r2
                            c'''2
                            d'''2
                            f'''4
                            ~
                            f'''4
                            cs'''2
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
                            \mark #5
                            cs''1
                            \mf
                            a'2.
                            ~
                            a'4
                            r2
                            r1
                            r2
                            bf'4
                            ~
                            bf'2.
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
                            \mark #5
                            f'1
                            \mf
                            a'2.
                            ~
                            a'4
                            r2
                            r1
                            r2
                            ef'4
                            ~
                            ef'2.
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
                            \mark #5
                            f'1
                            \mf
                            a'2.
                            ~
                            a'4
                            r2
                            r1
                            r2
                            ef'4
                            ~
                            ef'2.
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
                            \mark #5
                            a'''4
                            \p
                            f'''8.
                            c''''16
                            ~
                            c''''4
                            ef'''8.
                            d'''16
                            ~
                            d'''16
                            g'''8.
                            a'''4
                            f'''8.
                            c''''16
                            ~
                            c''''4
                            ef'''8.
                            d'''16
                            ~
                            d'''16
                            g'''8
                            ~
                            g'''16
                            a'''4
                            f'''8.
                            c''''16
                            ~
                            c''''4
                            ef'''8.
                            d'''16
                            ~
                            d'''16
                            g'''8.
                            a'''4
                            f'''8.
                            c''''16
                            ~
                            c''''4
                            ef'''8.
                            d'''16
                            ~
                            d'''16
                            g'''8
                            ~
                            g'''16
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
                            \mark #5
                            a''2
                            \p
                            f''4
                            ~
                            f''8
                            c'''8
                            ~
                            c'''2
                            ef''8
                            ~
                            ef''8
                            ~
                            ef''8
                            d''8
                            ~
                            d''8
                            g''8
                            ~
                            g''4
                            a''2
                            f''4
                            ~
                            f''8
                            c'''8
                            ~
                            c'''2
                            ef''8
                            ~
                            ef''8
                            ~
                            ef''8
                            d''8
                            ~
                            d''8
                            g''8
                            ~
                            g''4
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
                            \mark #5
                            e''1
                            \p
                            c''2.
                            g''2.
                            ~
                            g''2
                            bf'4
                            ~
                            bf'4
                            ~
                            bf'4
                            a'2
                            d''2.
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
                            \mark #5
                            a'1
                            \p
                            ~
                            a'2.
                            ~
                            a'4
                            f'2
                            ~
                            f'1
                            c''2.
                            ~
                            c''2.
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
                            \mark #5
                            a1
                            \p
                            ~
                            a2.
                            ~
                            a2.
                            ~
                            a1
                            ~
                            a2
                            f4
                            ~
                            f2.
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
                            \mark #5
                            f'''8.
                            \mf
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            ef'''16
                            ~
                            ef'''8.
                            a'''16
                            ~
                            a'''8
                            g'''8
                            ~
                            g'''16
                            f'''8.
                            ~
                            f'''16
                            ef'''8.
                            a'''8.
                            g'''16
                            ~
                            g'''8.
                            f'''16
                            ~
                            f'''8
                            ef'''8
                            ~
                            ef'''16
                            a'''8.
                            ~
                            a'''16
                            g'''8.
                            f'''8.
                            ef'''16
                            ~
                            ef'''8.
                            a'''16
                            ~
                            a'''8
                            g'''8
                            ~
                            g'''16
                            f'''8.
                            ~
                            f'''16
                            ef'''8.
                            a'''8.
                            g'''16
                            ~
                            g'''8.
                            f'''16
                            ~
                            f'''8
                            ef'''8
                            ~
                            ef'''16
                            a'''8.
                            ~
                            a'''16
                            g'''8.
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
                            \mark #5
                            f''8.
                            \mf
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            ef''16
                            ~
                            ef''8.
                            a''16
                            ~
                            a''8
                            g''8
                            ~
                            g''16
                            f''8.
                            ~
                            f''16
                            ef''8.
                            a''8.
                            g''16
                            ~
                            g''8.
                            f''16
                            ~
                            f''8
                            ef''8
                            ~
                            ef''16
                            a''8.
                            ~
                            a''16
                            g''8.
                            f''8.
                            ef''16
                            ~
                            ef''8.
                            a''16
                            ~
                            a''8
                            g''8
                            ~
                            g''16
                            f''8.
                            ~
                            f''16
                            ef''8.
                            a''8.
                            g''16
                            ~
                            g''8.
                            f''16
                            ~
                            f''8
                            ef''8
                            ~
                            ef''16
                            a''8.
                            ~
                            a''16
                            g''8.
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
                            \mark #5
                            f'8.
                            \mf
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            ef'16
                            ~
                            ef'8.
                            a'16
                            ~
                            a'8
                            g'8
                            ~
                            g'16
                            f'8.
                            ~
                            f'16
                            ef'8.
                            a'8.
                            g'16
                            ~
                            g'8.
                            f'16
                            ~
                            f'8
                            ef'8
                            ~
                            ef'16
                            a'8.
                            ~
                            a'16
                            g'8.
                            f'8.
                            ef'16
                            ~
                            ef'8.
                            a'16
                            ~
                            a'8
                            g'8
                            ~
                            g'16
                            f'8.
                            ~
                            f'16
                            ef'8.
                            a'8.
                            g'16
                            ~
                            g'8.
                            f'16
                            ~
                            f'8
                            ef'8
                            ~
                            ef'16
                            a'8.
                            ~
                            a'16
                            g'8.
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
                            \mark #5
                            f1
                            \f
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            a2.
                            ~
                            a4
                            r2
                            r1
                            r2
                            ef4
                            ~
                            ef2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()