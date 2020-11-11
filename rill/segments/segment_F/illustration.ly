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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute1_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            e''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            cs''8
                            - \tenuto
                            ~
                            \staccato
                            cs''8
                            e''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            cs''8
                            - \tenuto
                            ~
                            \staccato
                            cs''8
                            e''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute1_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            g''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            a''4
                            - \tenuto
                            \staccato
                            g''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            a''4
                            - \tenuto
                            \staccato
                            g''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            a''8
                            - \tenuto
                            ~
                            \staccato
                            a''8
                            g''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            a''4
                            - \tenuto
                            \staccato
                            g''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            a''4
                            - \tenuto
                            \staccato
                            g''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            a''4
                            - \tenuto
                            \staccato
                            g''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            a''8
                            - \tenuto
                            ~
                            \staccato
                            a''8
                            g''16
                            - \tenuto
                            \staccato
                            fs''8
                            - \tenuto
                            \staccato
                            r8.
                            a''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute3_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            g''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            fs''4
                            - \tenuto
                            \staccato
                            as''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            a''4
                            - \tenuto
                            \staccato
                            g''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            fs''8
                            - \tenuto
                            ~
                            \staccato
                            fs''8
                            as''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            a''4
                            - \tenuto
                            \staccato
                            g''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            fs''4
                            - \tenuto
                            \staccato
                            as''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            a''4
                            - \tenuto
                            \staccato
                            g''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            fs''8
                            - \tenuto
                            ~
                            \staccato
                            fs''8
                            as''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            a''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute3_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute4_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            c'''16
                            - \tenuto
                            \staccato
                            e'''8
                            - \tenuto
                            \staccato
                            r8.
                            as''4
                            - \tenuto
                            \staccato
                            cs'''16
                            - \tenuto
                            \staccato
                            a''8
                            - \tenuto
                            \staccato
                            r8.
                            cs'''4
                            - \tenuto
                            \staccato
                            c'''16
                            - \tenuto
                            \staccato
                            e'''8
                            - \tenuto
                            \staccato
                            r8.
                            as''8
                            - \tenuto
                            ~
                            \staccato
                            as''8
                            cs'''16
                            - \tenuto
                            \staccato
                            a''8
                            - \tenuto
                            \staccato
                            r8.
                            cs'''4
                            - \tenuto
                            \staccato
                            c'''16
                            - \tenuto
                            \staccato
                            e'''8
                            - \tenuto
                            \staccato
                            r8.
                            as''4
                            - \tenuto
                            \staccato
                            cs'''16
                            - \tenuto
                            \staccato
                            a''8
                            - \tenuto
                            \staccato
                            r8.
                            cs'''4
                            - \tenuto
                            \staccato
                            c'''16
                            - \tenuto
                            \staccato
                            e'''8
                            - \tenuto
                            \staccato
                            r8.
                            as''8
                            - \tenuto
                            ~
                            \staccato
                            as''8
                            cs'''16
                            - \tenuto
                            \staccato
                            a''8
                            - \tenuto
                            \staccato
                            r8.
                            cs'''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute4_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Music_Voice"                 %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''8
                            - \tenuto
                            ~
                            \staccato
                            cs''8
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''8
                            - \tenuto
                            ~
                            \staccato
                            cs''8
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Dynamics_Voice"              %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
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
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Vibraphone_Music_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''8
                            - \tenuto
                            ~
                            \staccato
                            cs''8
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''8
                            - \tenuto
                            ~
                            \staccato
                            cs''8
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Vibraphone_Dynamics_Voice"               %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin1_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin1_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin3_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin3_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin5_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin5_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin8_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''4
                            - \tenuto
                            \staccato
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                            e''16
                            - \tenuto
                            \staccato
                            cs'''8
                            - \tenuto
                            \staccato
                            r8.
                            g''8
                            - \tenuto
                            ~
                            \staccato
                            g''8
                            a''16
                            - \tenuto
                            \staccato
                            as''8
                            - \tenuto
                            \staccato
                            r8.
                            c'''4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin8_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
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
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Viola_Music_Voice"                       %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \mark #6
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''8
                            - \tenuto
                            ~
                            \staccato
                            cs''8
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''4
                            - \tenuto
                            \staccato
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                            b'16
                            - \tenuto
                            \staccato
                            g'8
                            - \tenuto
                            \staccato
                            r8.
                            cs''8
                            - \tenuto
                            ~
                            \staccato
                            cs''8
                            es''16
                            - \tenuto
                            \staccato
                            e''8
                            - \tenuto
                            \staccato
                            r8.
                            a'4
                            - \tenuto
                            \staccato
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Viola_Dynamics_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 3/16
                        s1 * 1/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()