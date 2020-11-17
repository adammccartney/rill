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
                    \context Voice = "Flute1_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            a''4
                            \p
                            ~
                            a''8
                            c'''8
                            a''4
                            ~
                            a''8
                            c'''8
                            a''4
                            c'''4
                            ~
                            c'''8
                            a''8
                            c'''4
                            ~
                            c'''8
                            a''8
                            c'''4
                            a''4
                            ~
                            a''8
                            c'''8
                            a''4
                            ~
                            a''8
                            c'''8
                            a''4
                            c'''4
                            ~
                            c'''8
                            a''8
                            c'''4
                            ~
                            c'''8
                            a''8
                            c'''4
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute1_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
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
                \tag #'fluteTwo
                \context FluteTwoStaff = "Flute2"                              %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Markup_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \once \override NoteHead.style = #'cross
                            \mark #4
                            a''2.
                            \p
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            c'''4
                            \once \override NoteHead.style = #'cross
                            a''2.
                            \once \override NoteHead.style = #'cross
                            c'''4
                            \once \override NoteHead.style = #'cross
                            a''2
                            \once \override NoteHead.style = #'cross
                            c'''2.
                            \once \override NoteHead.style = #'cross
                            a''4
                            \once \override NoteHead.style = #'cross
                            c'''2.
                            \once \override NoteHead.style = #'cross
                            a''4
                            \once \override NoteHead.style = #'cross
                            c'''2
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
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
                    \context Voice = "Flute3_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            cs''4
                            ~
                            cs''8
                            bf'8
                            cs''4
                            ~
                            cs''8
                            bf'8
                            cs''4
                            bf'4
                            ~
                            bf'8
                            cs''8
                            bf'4
                            ~
                            bf'8
                            cs''8
                            bf'4
                            cs''4
                            ~
                            cs''8
                            bf'8
                            cs''4
                            ~
                            cs''8
                            bf'8
                            cs''4
                            bf'4
                            ~
                            bf'8
                            cs''8
                            bf'4
                            ~
                            bf'8
                            cs''8
                            bf'4
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute3_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
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
                \tag #'fluteFour
                \context FluteFourStaff = "Flute4"                             %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute4_Markup_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute4_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \once \override NoteHead.style = #'cross
                            \mark #4
                            cs''2.
                            \p
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            bf'4
                            \once \override NoteHead.style = #'cross
                            cs''2.
                            \once \override NoteHead.style = #'cross
                            bf'4
                            \once \override NoteHead.style = #'cross
                            cs''2
                            \once \override NoteHead.style = #'cross
                            bf'2.
                            \once \override NoteHead.style = #'cross
                            cs''4
                            \once \override NoteHead.style = #'cross
                            bf'2.
                            \once \override NoteHead.style = #'cross
                            cs''4
                            \once \override NoteHead.style = #'cross
                            bf'2
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute4_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
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
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Music_Voice"                 %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \once \override NoteHead.style = #'cross
                            \mark #4
                            f''32
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            f''32
                            \once \override NoteHead.style = #'cross
                            ef''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Dynamics_Voice"              %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
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
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Vibraphone_Music_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            f''16
                            \pp
                            r16
                            ef''16
                            a''16
                            g''16
                            r16
                            r16
                            f''16
                            ef''16
                            a''16
                            g''16
                            r16
                            f''16
                            ef''16
                            a''16
                            r16
                            r16
                            g''16
                            f''16
                            ef''16
                            a''16
                            r16
                            g''16
                            f''16
                            ef''16
                            r16
                            r16
                            a''16
                            g''16
                            f''16
                            ef''16
                            r16
                            a''16
                            g''16
                            f''16
                            r16
                            r16
                            ef''16
                            a''16
                            g''16
                            f''16
                            r16
                            ef''16
                            a''16
                            g''16
                            r16
                            r16
                            f''16
                            ef''16
                            a''16
                            g''16
                            r16
                            f''16
                            ef''16
                            a''16
                            r16
                            r16
                            g''16
                            f''16
                            ef''16
                            a''16
                            r16
                            g''16
                            f''16
                            ef''16
                            r16
                            r16
                            a''16
                            g''16
                            f''16
                            ef''16
                            r16
                            a''16
                            g''16
                            f''16
                            r16
                            r16
                            ef''16
                            a''16
                            g''16
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Vibraphone_Dynamics_Voice"               %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
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
                    \context Voice = "Violin1_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            e'''1
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            c'''2.
                            g'''2.
                            ~
                            g'''2
                            bf''4
                            ~
                            bf''4
                            ~
                            bf''4
                            a'''2
                            d'''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin1_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
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
                \tag #'violinTwo
                \context ViolinTwoStaff = "Violin2"                            %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            e''1
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            ~
                            e''2.
                            ~
                            e''4
                            c''2
                            ~
                            c''1
                            g''2.
                            ~
                            g''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
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
                    \context Voice = "Violin3_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            e'''1
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            c'''2.
                            g'''2.
                            ~
                            g'''2
                            bf''4
                            ~
                            bf''4
                            ~
                            bf''4
                            a'''2
                            d'''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin3_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
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
                \tag #'violinFour
                \context ViolinFourStaff = "Violin4"                           %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            e''1
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            ~
                            e''2.
                            ~
                            e''4
                            c''2
                            ~
                            c''1
                            g''2.
                            ~
                            g''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
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
                    \context Voice = "Violin5_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            e''1
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            c''2.
                            g''2.
                            ~
                            g''2
                            bf'4
                            ~
                            bf'4
                            ~
                            bf'4
                            a''2
                            d''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin5_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
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
                \tag #'violinSix
                \context ViolinSixStaff = "Violin6"                            %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            r1
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            cs'2.
                            ~
                            cs'4
                            r2
                            r2
                            a2
                            ~
                            a2
                            r4
                            r2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
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
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/1
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            r1
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            r2.
                            r4
                            cs''2
                            ~
                            cs''1
                            ~
                            cs''2
                            r4
                            r2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/1
                        s1 * 1/2
                        s1 * 1/4
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
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin8_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #4
                            r1
                            \pp
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            cs'2.
                            ~
                            cs'4
                            r2
                            r2
                            a2
                            ~
                            a2
                            r4
                            r2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin8_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/2
                        s1 * 1/4
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
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Viola_Music_Voice"                       %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \once \override NoteHead.style = #'cross
                            \mark #4
                            f'32
                            \ppp
                            ^ \markup {
                                \upright
                                    legato
                                }
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            f'32
                            \once \override NoteHead.style = #'cross
                            ef'32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            g'32
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Viola_Dynamics_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        s1 * 1/32
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()