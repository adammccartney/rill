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
                            \mark #6
                            e''2
                            \mf
                            fs''2
                            cs''2
                            e''4
                            ~
                            e''4
                            fs''2
                            cs''2
                            e''2
                            fs''2
                            cs''4
                            ~
                            cs''4
                            r2
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
                            \mark #6
                            g'2
                            \mf
                            fs'2
                            a'2
                            g'4
                            ~
                            g'4
                            fs'2
                            a'2
                            g'2
                            fs'2
                            a'4
                            ~
                            a'4
                            r2
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
                            \mark #6
                            r8
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            r8
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            r8
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            r8
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            r8
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            fs''32
                            \once \override NoteHead.style = #'cross
                            as''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            cs'''32
                            \once \override NoteHead.style = #'cross
                            a''32
                            \once \override NoteHead.style = #'cross
                            g''32
                            \once \override NoteHead.style = #'cross
                            e''32
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
                            \mark #6
                            r8
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r8
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r8
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r8
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r8
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r8
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r8
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r8
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r8
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            r8
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r8
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            as'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            c''32
                            \once \override NoteHead.style = #'cross
                            e''32
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
                            \mark #6
                            r8
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            r8
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            r8
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            r8
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            r8
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            r8
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            r8
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            r8
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            r8
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            r8
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
                            \once \override NoteHead.style = #'cross
                            cs''32
                            \once \override NoteHead.style = #'cross
                            es''32
                            r16
                            r16
                            \once \override NoteHead.style = #'cross
                            e''32
                            \once \override NoteHead.style = #'cross
                            a'32
                            \once \override NoteHead.style = #'cross
                            b'32
                            \once \override NoteHead.style = #'cross
                            g'32
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
                            \mark #6
                            r8
                            \pp
                            b'32
                            g'32
                            cs''32
                            es''32
                            r8
                            e''32
                            a'32
                            b'32
                            g'32
                            r8
                            cs''32
                            es''32
                            e''32
                            a'32
                            r8
                            b'32
                            g'32
                            cs''32
                            es''32
                            r8
                            e''32
                            a'32
                            b'32
                            g'32
                            r8
                            cs''32
                            es''32
                            e''32
                            a'32
                            r16
                            r16
                            b'32
                            g'32
                            cs''32
                            es''32
                            r8
                            e''32
                            a'32
                            b'32
                            g'32
                            r8
                            cs''32
                            es''32
                            e''32
                            a'32
                            r16
                            r16
                            b'32
                            g'32
                            cs''32
                            es''32
                            r8
                            e''32
                            a'32
                            b'32
                            g'32
                            r8
                            cs''32
                            es''32
                            e''32
                            a'32
                            r8
                            b'32
                            g'32
                            cs''32
                            es''32
                            r8
                            e''32
                            a'32
                            b'32
                            g'32
                            r8
                            cs''32
                            es''32
                            e''32
                            a'32
                            r8
                            b'32
                            g'32
                            cs''32
                            es''32
                            r16
                            r16
                            e''32
                            a'32
                            b'32
                            g'32
                            r8
                            cs''32
                            es''32
                            e''32
                            a'32
                            r8
                            b'32
                            g'32
                            cs''32
                            es''32
                            r16
                            r16
                            e''32
                            a'32
                            b'32
                            g'32
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
                            \mark #6
                            e''8.
                            cs'''16
                            ~
                            cs'''8.
                            g''16
                            ~
                            g''8
                            a''8
                            ~
                            a''16
                            as''8.
                            ~
                            as''16
                            c'''8.
                            e''8.
                            cs'''16
                            ~
                            cs'''8.
                            g''16
                            ~
                            g''8
                            a''8
                            ~
                            a''16
                            as''8.
                            ~
                            as''16
                            c'''8.
                            e''8.
                            cs'''16
                            ~
                            cs'''8.
                            g''16
                            ~
                            g''8
                            a''8
                            ~
                            a''16
                            as''8.
                            ~
                            as''16
                            c'''8.
                            e''8.
                            cs'''16
                            ~
                            cs'''8.
                            g''16
                            ~
                            g''8
                            a''8
                            ~
                            a''16
                            as''8.
                            ~
                            as''16
                            c'''8.
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
                            \mark #6
                            e'8.
                            \p
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            cs''16
                            ~
                            cs''8.
                            g'16
                            ~
                            g'8
                            a'8
                            ~
                            a'16
                            as'8.
                            ~
                            as'16
                            c''8.
                            e'8.
                            cs''16
                            ~
                            cs''8.
                            g'16
                            ~
                            g'8
                            a'8
                            ~
                            a'16
                            as'8.
                            ~
                            as'16
                            c''8.
                            e'8.
                            cs''16
                            ~
                            cs''8.
                            g'16
                            ~
                            g'8
                            a'8
                            ~
                            a'16
                            as'8.
                            ~
                            as'16
                            c''8.
                            e'8.
                            cs''16
                            ~
                            cs''8.
                            g'16
                            ~
                            g'8
                            a'8
                            ~
                            a'16
                            as'8.
                            ~
                            as'16
                            c''8.
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
                            \mark #6
                            e''4
                            \p
                            ^ \markup {
                                \upright
                                    ord.
                                }
                            ~
                            e''8
                            cs'''8
                            ~
                            cs'''4
                            ~
                            cs'''8
                            g''8
                            ~
                            g''4
                            a''4
                            ~
                            a''8
                            as''8
                            ~
                            as''4
                            ~
                            as''8
                            c'''8
                            ~
                            c'''4
                            e''4
                            ~
                            e''8
                            cs'''8
                            ~
                            cs'''4
                            ~
                            cs'''8
                            g''8
                            ~
                            g''4
                            a''4
                            ~
                            a''8
                            as''8
                            ~
                            as''4
                            ~
                            as''8
                            c'''8
                            ~
                            c'''4
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
                            \mark #6
                            e'4
                            \p
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            ~
                            e'8
                            cs''8
                            ~
                            cs''4
                            ~
                            cs''8
                            g'8
                            ~
                            g'4
                            a'4
                            ~
                            a'8
                            as'8
                            ~
                            as'4
                            ~
                            as'8
                            c''8
                            ~
                            c''4
                            e'4
                            ~
                            e'8
                            cs''8
                            ~
                            cs''4
                            ~
                            cs''8
                            g'8
                            ~
                            g'4
                            a'4
                            ~
                            a'8
                            as'8
                            ~
                            as'4
                            ~
                            as'8
                            c''8
                            ~
                            c''4
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
                            \mark #6
                            e''2.
                            \p
                            ^ \markup {
                                \upright
                                    ord.
                                }
                            cs'''4
                            ~
                            cs'''2.
                            g''2.
                            a''2.
                            as''4
                            ~
                            as''2.
                            c'''2.
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
                            \mark #6
                            e'2.
                            \p
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            cs''4
                            ~
                            cs''2.
                            g'2.
                            a'2.
                            as'4
                            ~
                            as'2.
                            c''2.
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
                            \mark #6
                            e''1
                            \p
                            ^ \markup {
                                \upright
                                    ord.
                                }
                            ~
                            e''2
                            cs'''4
                            ~
                            cs'''2.
                            ~
                            cs'''1
                            g''2.
                            ~
                            g''2.
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
                            \mark #6
                            e'1
                            \p
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            ~
                            e'2
                            cs''4
                            ~
                            cs''2.
                            ~
                            cs''1
                            g'2.
                            ~
                            g'2.
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
                            \mark #6
                            b1
                            \f
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            g2.
                            cs'2.
                            ~
                            cs'2
                            es'4
                            ~
                            es'4
                            ~
                            es'4
                            e'2
                            a2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()