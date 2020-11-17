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
                    \context Voice = "Flute1_Markup_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute1_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            d''2
                            \mf
                            e''2
                            r2
                            d''4
                            ~
                            d''4
                            r2
                            e''2
                            d''2
                            r2
                            e''4
                            ~
                            e''4
                            d''2
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute1_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'fluteTwo
                \context FluteTwoStaff = "Flute2"                              %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Markup_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            a''2
                            \mf
                            b''2
                            r2
                            a''4
                            ~
                            a''4
                            r2
                            b''2
                            a''2
                            r2
                            b''4
                            ~
                            b''4
                            a''2
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'fluteThree
                \context FluteThreeStaff = "Flute3"                            %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute3_Markup_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute3_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            r8
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            r8
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            r8
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            r8
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            r8
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            r8
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            r8
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            r8
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            r8
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            r8
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            r8
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            b''32
                            \once \override NoteHead.style = #'cross
                            d'''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            fs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            f''32
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute3_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'fluteFour
                \context FluteFourStaff = "Flute4"                             %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute4_Markup_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute4_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            r8
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            r8
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            r8
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            r8
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            r8
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            r8
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            r8
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            r8
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            r8
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            r8
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            r8
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            fs'32
                            \once \override NoteHead.style = #'cross
                            gs'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            d''32
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute4_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/8
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'BbclarinetOne
                \context BbclarinetOneStaff = "Bbclarinet1"                    %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"Bbclarinet"                             %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Markup_Voice"                %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Music_Voice"                 %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \once \override NoteHead.style = #'cross
                            \mark #7
                            d''1
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            a'2.
                            \once \override NoteHead.style = #'cross
                            d''2.
                            ~
                            \once \override NoteHead.style = #'cross
                            d''2
                            \once \override NoteHead.style = #'cross
                            e''4
                            ~
                            \once \override NoteHead.style = #'cross
                            e''4
                            ~
                            \once \override NoteHead.style = #'cross
                            e''4
                            \once \override NoteHead.style = #'cross
                            gs''2
                            \once \override NoteHead.style = #'cross
                            fs''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Dynamics_Voice"              %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 3/4
                        \!
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
                    \context Voice = "Vibraphone_Markup_Voice"                 %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Vibraphone_Music_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            d''1
                            \pp
                            a'2.
                            d''2.
                            ~
                            d''2
                            e''4
                            ~
                            e''4
                            ~
                            e''4
                            gs''2
                            fs''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Vibraphone_Dynamics_Voice"               %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 3/4
                        \!
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
                    \context Voice = "Violin1_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin1_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            gs'''8.
                            f'''16
                            ~
                            f'''8.
                            gs'''16
                            ~
                            gs'''8
                            a'''8
                            ~
                            a'''16
                            gs'''8.
                            ~
                            gs'''16
                            f'''8.
                            gs'''8.
                            a'''16
                            ~
                            a'''8.
                            gs'''16
                            ~
                            gs'''8
                            f'''8
                            ~
                            f'''16
                            gs'''8.
                            ~
                            gs'''16
                            a'''8.
                            gs'''8.
                            f'''16
                            ~
                            f'''8.
                            gs'''16
                            ~
                            gs'''8
                            a'''8
                            ~
                            a'''16
                            gs'''8.
                            ~
                            gs'''16
                            f'''8.
                            gs'''8.
                            a'''16
                            ~
                            a'''8.
                            gs'''16
                            ~
                            gs'''8
                            f'''8
                            ~
                            f'''16
                            gs'''8.
                            ~
                            gs'''16
                            a'''8.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin1_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinTwo
                \context ViolinTwoStaff = "Violin2"                            %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            gs''8.
                            \p
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            f''16
                            ~
                            f''8.
                            gs''16
                            ~
                            gs''8
                            a''8
                            ~
                            a''16
                            gs''8.
                            ~
                            gs''16
                            f''8.
                            gs''8.
                            a''16
                            ~
                            a''8.
                            gs''16
                            ~
                            gs''8
                            f''8
                            ~
                            f''16
                            gs''8.
                            ~
                            gs''16
                            a''8.
                            gs''8.
                            f''16
                            ~
                            f''8.
                            gs''16
                            ~
                            gs''8
                            a''8
                            ~
                            a''16
                            gs''8.
                            ~
                            gs''16
                            f''8.
                            gs''8.
                            a''16
                            ~
                            a''8.
                            gs''16
                            ~
                            gs''8
                            f''8
                            ~
                            f''16
                            gs''8.
                            ~
                            gs''16
                            a''8.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/16
                        s1 * 3/16
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinThree
                \context ViolinThreeStaff = "Violin3"                          %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin3_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin3_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            gs'''4
                            \p
                            ^ \markup {
                                \upright
                                    ord.
                                }
                            ~
                            gs'''8
                            f'''8
                            ~
                            f'''4
                            ~
                            f'''8
                            gs'''8
                            ~
                            gs'''4
                            a'''4
                            ~
                            a'''8
                            gs'''8
                            ~
                            gs'''4
                            ~
                            gs'''8
                            f'''8
                            ~
                            f'''4
                            gs'''4
                            ~
                            gs'''8
                            a'''8
                            ~
                            a'''4
                            ~
                            a'''8
                            gs'''8
                            ~
                            gs'''4
                            f'''4
                            ~
                            f'''8
                            gs'''8
                            ~
                            gs'''4
                            ~
                            gs'''8
                            a'''8
                            ~
                            a'''4
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin3_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinFour
                \context ViolinFourStaff = "Violin4"                           %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            gs''4
                            \p
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
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
                            a''4
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
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinFive
                \context ViolinFiveStaff = "Violin5"                           %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin5_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin5_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            gs'''2.
                            \p
                            ^ \markup {
                                \upright
                                    ord.
                                }
                            f'''4
                            ~
                            f'''2.
                            gs'''2.
                            a'''2.
                            gs'''4
                            ~
                            gs'''2.
                            f'''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin5_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinSix
                \context ViolinSixStaff = "Violin6"                            %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            gs''2.
                            \p
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            f''4
                            ~
                            f''2.
                            gs''2.
                            a''2.
                            gs''4
                            ~
                            gs''2.
                            f''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinSeven
                \context ViolinSevenStaff = "Violin7"                          %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            gs'''1
                            \p
                            ^ \markup {
                                \upright
                                    ord.
                                }
                            ~
                            gs'''2
                            f'''4
                            ~
                            f'''2.
                            ~
                            f'''1
                            gs'''2.
                            ~
                            gs'''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinEight
                \context ViolinEightStaff = "Violin8"                          %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin8_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin8_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            gs''1
                            \p
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            ~
                            gs''2
                            f''4
                            ~
                            f''2.
                            ~
                            f''1
                            gs''2.
                            ~
                            gs''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin8_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'viola
                \context ViolaStaff = "Viola"                                  %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"viola"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Viola_Markup_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Viola_Music_Voice"                       %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #7
                            d'1
                            \mf
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
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
                    \context Voice = "Viola_Dynamics_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()