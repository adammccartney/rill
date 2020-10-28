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
            \context StaffGroup = "Woodwind_Staff_Group"                       %! rill.ScoreTemplate.__call__()
            <<                                                                 %! rill.ScoreTemplate.__call__()
                \tag #'fluteOne
                \context Staff = "flute1"                                      %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute1_Markup_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 3/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 3/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/2
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute1_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \once \override DynamicLineSpanner.staff-padding = #3
                            \time 4/4
                            \clef "treble"
                            \mark #1
                            fs''8
                            \p
                            - \accent
                            \<
                            cs''8
                            ~
                            cs''8
                            \f
                            r4.
                            \once \override DynamicLineSpanner.staff-padding = #3
                            fs''4
                            \p
                            - \accent
                            \<
                            ~
                            \time 3/4
                            fs''4
                            cs''8
                            fs''8
                            ~
                            fs''8
                            \f
                            r8
                            \time 3/4
                            r4
                            \once \override DynamicLineSpanner.staff-padding = #3
                            cs''2
                            \p
                            - \accent
                            \<
                            \time 4/4
                            fs''8
                            cs''8
                            ~
                            cs''8
                            \f
                            r4.
                            \once \override DynamicLineSpanner.staff-padding = #3
                            fs''4
                            \p
                            - \accent
                            \<
                            ~
                            \time 3/4
                            fs''4
                            cs''8
                            fs''8
                            ~
                            fs''8
                            \f
                            r8
                            \time 3/4
                            r4
                            cs''2
                            \ppp
                            - \accent
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute1_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 3/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/2
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 3/8
                        s1 * 1/4
                        s1 * 1/4
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/4
                        s1 * 1/2
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'fluteTwo
                \context Staff = "flute2"                                      %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Markup_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        {
                            \once \override DynamicLineSpanner.staff-padding = #3
                            \time 4/4
                            \clef "treble"
                            \mark #1
                            fs'16
                            \p
                            - \accent
                            \<
                            a'16
                            ~
                            a'16
                            \f
                            r16
                            r8
                            \once \override DynamicLineSpanner.staff-padding = #3
                            fs'8
                            \p
                            - \accent
                            \<
                            ~
                            fs'8
                            a'16
                            fs'16
                            ~
                            fs'16
                            \f
                            r8.
                            \once \override DynamicLineSpanner.staff-padding = #3
                            \time 3/4
                            a'4
                            \p
                            - \accent
                            \<
                            fs'16
                            a'16
                            ~
                            a'16
                            \f
                            r16
                            r8
                            \once \override DynamicLineSpanner.staff-padding = #3
                            fs'8
                            \p
                            - \accent
                            \<
                            ~
                            \time 3/4
                            fs'8
                            a'16
                            fs'16
                            ~
                            fs'16
                            \f
                            r8.
                            \once \override DynamicLineSpanner.staff-padding = #3
                            a'4
                            \p
                            - \accent
                            \<
                            \time 4/4
                            fs'16
                            a'16
                            ~
                            a'16
                            \f
                            r16
                            r8
                            \once \override DynamicLineSpanner.staff-padding = #3
                            fs'8
                            \p
                            - \accent
                            \<
                            ~
                            fs'8
                            a'16
                            fs'16
                            ~
                            fs'16
                            \f
                            r8.
                            \once \override DynamicLineSpanner.staff-padding = #3
                            \time 3/4
                            a'4
                            \p
                            - \accent
                            \<
                            fs'16
                            a'16
                            ~
                            a'16
                            \f
                            r16
                            r8
                            \once \override DynamicLineSpanner.staff-padding = #3
                            fs'8
                            \p
                            - \accent
                            \<
                            ~
                            \time 3/4
                            fs'8
                            a'16
                            fs'16
                            ~
                            fs'16
                            \f
                            r8.
                            a'4
                            \ppp
                            - \accent
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute2_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/4
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/8
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 1/16
                        s1 * 3/16
                        s1 * 1/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'fluteThree
                \context Staff = "flute3"                                      %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"flute"                                  %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute3_Markup_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute3_Music_Voice"                      %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Flute3_Dynamics_Voice"                   %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'BbclarinetOne
                \context Staff = "Bbclarinet1"                                 %! rill.ScoreTemplate.__call__()
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
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Music_Voice"                 %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Bbclarinet1_Dynamics_Voice"              %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
            \context StaffGroup = "Percussion_Staff_Group"                     %! rill.ScoreTemplate.__call__()
            <<                                                                 %! rill.ScoreTemplate.__call__()
                \tag #'vibraphone
                \context Staff = "vibraphone"                                  %! rill.ScoreTemplate.__call__()
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
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Vibraphone_Music_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Vibraphone_Dynamics_Voice"               %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
            \context StaffGroup = "String_Staff_Group"                         %! rill.ScoreTemplate.__call__()
            <<                                                                 %! rill.ScoreTemplate.__call__()
                \tag #'violinOne
                \context Staff = "violin1"                                     %! rill.ScoreTemplate.__call__()
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
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin1_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin1_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinTwo
                \context Staff = "violin2"                                     %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin2_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinThree
                \context Staff = "violin3"                                     %! rill.ScoreTemplate.__call__()
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
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin3_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin3_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinFour
                \context Staff = "violin4"                                     %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin4_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinFive
                \context Staff = "violin5"                                     %! rill.ScoreTemplate.__call__()
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
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin5_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin5_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinSix
                \context Staff = "violin6"                                     %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin6_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'violinSeven
                \context Staff = "violin7"                                     %! rill.ScoreTemplate.__call__()
                \with                                                          %! rill.ScoreTemplate.__call__()
                {                                                              %! rill.ScoreTemplate.__call__()
                    midiInstrument = #"violin"                                 %! rill.ScoreTemplate.__call__()
                }                                                              %! rill.ScoreTemplate.__call__()
                <<                                                             %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Markup_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Music_Voice"                     %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Violin7_Dynamics_Voice"                  %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
                \tag #'viola
                \context Staff = "viola"                                       %! rill.ScoreTemplate.__call__()
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
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \stopTextSpan
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Viola_Music_Voice"                       %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        \mark #1
                        r1
                        r2.
                        r2.
                        r1
                        r2.
                        r2.
                    }                                                          %! rill.ScoreTemplate.__call__()
                    \context Voice = "Viola_Dynamics_Voice"                    %! rill.ScoreTemplate.__call__()
                    {                                                          %! rill.ScoreTemplate.__call__()
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        s1 * 1/1
                        s1 * 3/4
                        s1 * 3/4
                        \!
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()