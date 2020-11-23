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
                            \once \override NoteHead.style = #'cross
                            \clef "treble"
                            \mark #1
                            c'''4
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            ~
                            \once \override NoteHead.style = #'cross
                            c'''8
                            \once \override NoteHead.style = #'cross
                            as''8
                            ~
                            \once \override NoteHead.style = #'cross
                            as''4
                            ~
                            \once \override NoteHead.style = #'cross
                            as''8
                            \once \override NoteHead.style = #'cross
                            a''8
                            ~
                            \once \override NoteHead.style = #'cross
                            a''4
                            \once \override NoteHead.style = #'cross
                            g''4
                            ~
                            \once \override NoteHead.style = #'cross
                            g''8
                            \once \override NoteHead.style = #'cross
                            cs'''8
                            ~
                            \once \override NoteHead.style = #'cross
                            cs'''4
                            ~
                            \once \override NoteHead.style = #'cross
                            cs'''8
                            \once \override NoteHead.style = #'cross
                            e''8
                            ~
                            \once \override NoteHead.style = #'cross
                            e''4
                            \once \override NoteHead.style = #'cross
                            c'''4
                            ~
                            \once \override NoteHead.style = #'cross
                            c'''8
                            \once \override NoteHead.style = #'cross
                            as''8
                            ~
                            \once \override NoteHead.style = #'cross
                            as''4
                            ~
                            \once \override NoteHead.style = #'cross
                            as''8
                            \once \override NoteHead.style = #'cross
                            a''8
                            ~
                            \once \override NoteHead.style = #'cross
                            a''4
                            \once \override NoteHead.style = #'cross
                            g''4
                            ~
                            \once \override NoteHead.style = #'cross
                            g''8
                            \once \override NoteHead.style = #'cross
                            cs'''8
                            ~
                            \once \override NoteHead.style = #'cross
                            cs'''4
                            ~
                            \once \override NoteHead.style = #'cross
                            cs'''8
                            \once \override NoteHead.style = #'cross
                            e''8
                            ~
                            \once \override NoteHead.style = #'cross
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
                            \once \override NoteHead.style = #'cross
                            \clef "treble"
                            \mark #1
                            c''8.
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            as'16
                            ~
                            \once \override NoteHead.style = #'cross
                            as'8.
                            \once \override NoteHead.style = #'cross
                            a'16
                            ~
                            \once \override NoteHead.style = #'cross
                            a'8
                            \once \override NoteHead.style = #'cross
                            g'8
                            ~
                            \once \override NoteHead.style = #'cross
                            g'16
                            \once \override NoteHead.style = #'cross
                            cs''8.
                            ~
                            \once \override NoteHead.style = #'cross
                            cs''16
                            \once \override NoteHead.style = #'cross
                            e'8.
                            \once \override NoteHead.style = #'cross
                            c''8.
                            \once \override NoteHead.style = #'cross
                            as'16
                            ~
                            \once \override NoteHead.style = #'cross
                            as'8.
                            \once \override NoteHead.style = #'cross
                            a'16
                            ~
                            \once \override NoteHead.style = #'cross
                            a'8
                            \once \override NoteHead.style = #'cross
                            g'8
                            ~
                            \once \override NoteHead.style = #'cross
                            g'16
                            \once \override NoteHead.style = #'cross
                            cs''8.
                            ~
                            \once \override NoteHead.style = #'cross
                            cs''16
                            \once \override NoteHead.style = #'cross
                            e'8.
                            \once \override NoteHead.style = #'cross
                            c''8.
                            \once \override NoteHead.style = #'cross
                            as'16
                            ~
                            \once \override NoteHead.style = #'cross
                            as'8.
                            \once \override NoteHead.style = #'cross
                            a'16
                            ~
                            \once \override NoteHead.style = #'cross
                            a'8
                            \once \override NoteHead.style = #'cross
                            g'8
                            ~
                            \once \override NoteHead.style = #'cross
                            g'16
                            \once \override NoteHead.style = #'cross
                            cs''8.
                            ~
                            \once \override NoteHead.style = #'cross
                            cs''16
                            \once \override NoteHead.style = #'cross
                            e'8.
                            \once \override NoteHead.style = #'cross
                            c''8.
                            \once \override NoteHead.style = #'cross
                            as'16
                            ~
                            \once \override NoteHead.style = #'cross
                            as'8.
                            \once \override NoteHead.style = #'cross
                            a'16
                            ~
                            \once \override NoteHead.style = #'cross
                            a'8
                            \once \override NoteHead.style = #'cross
                            g'8
                            ~
                            \once \override NoteHead.style = #'cross
                            g'16
                            \once \override NoteHead.style = #'cross
                            cs''8.
                            ~
                            \once \override NoteHead.style = #'cross
                            cs''16
                            \once \override NoteHead.style = #'cross
                            e'8.
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
                            \once \override NoteHead.style = #'cross
                            \clef "treble"
                            \mark #1
                            c''4
                            \ppp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            ~
                            \once \override NoteHead.style = #'cross
                            c''8
                            \once \override NoteHead.style = #'cross
                            as'8
                            ~
                            \once \override NoteHead.style = #'cross
                            as'4
                            ~
                            \once \override NoteHead.style = #'cross
                            as'8
                            \once \override NoteHead.style = #'cross
                            a'8
                            ~
                            \once \override NoteHead.style = #'cross
                            a'4
                            \once \override NoteHead.style = #'cross
                            g'4
                            ~
                            \once \override NoteHead.style = #'cross
                            g'8
                            \once \override NoteHead.style = #'cross
                            cs''8
                            ~
                            \once \override NoteHead.style = #'cross
                            cs''4
                            ~
                            \once \override NoteHead.style = #'cross
                            cs''8
                            \once \override NoteHead.style = #'cross
                            e'8
                            ~
                            \once \override NoteHead.style = #'cross
                            e'4
                            \once \override NoteHead.style = #'cross
                            c''4
                            ~
                            \once \override NoteHead.style = #'cross
                            c''8
                            \once \override NoteHead.style = #'cross
                            as'8
                            ~
                            \once \override NoteHead.style = #'cross
                            as'4
                            ~
                            \once \override NoteHead.style = #'cross
                            as'8
                            \once \override NoteHead.style = #'cross
                            a'8
                            ~
                            \once \override NoteHead.style = #'cross
                            a'4
                            \once \override NoteHead.style = #'cross
                            g'4
                            ~
                            \once \override NoteHead.style = #'cross
                            g'8
                            \once \override NoteHead.style = #'cross
                            cs''8
                            ~
                            \once \override NoteHead.style = #'cross
                            cs''4
                            ~
                            \once \override NoteHead.style = #'cross
                            cs''8
                            \once \override NoteHead.style = #'cross
                            e'8
                            ~
                            \once \override NoteHead.style = #'cross
                            e'4
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
                            \mark #1
                            c''4
                            \p
                            ~
                            c''8
                            as'8
                            ~
                            as'4
                            ~
                            as'8
                            a'8
                            ~
                            a'4
                            g'4
                            ~
                            g'8
                            cs''8
                            ~
                            cs''4
                            ~
                            cs''8
                            e'8
                            ~
                            e'4
                            c''4
                            ~
                            c''8
                            as'8
                            ~
                            as'4
                            ~
                            as'8
                            a'8
                            ~
                            a'4
                            g'4
                            ~
                            g'8
                            cs''8
                            ~
                            cs''4
                            ~
                            cs''8
                            e'8
                            ~
                            e'4
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
                            \mark #1
                            c''8.
                            \p
                            as'16
                            ~
                            as'8.
                            a'16
                            ~
                            a'8
                            g'8
                            ~
                            g'16
                            cs''8.
                            ~
                            cs''16
                            e'8.
                            c''8.
                            as'16
                            ~
                            as'8.
                            a'16
                            ~
                            a'8
                            g'8
                            ~
                            g'16
                            cs''8.
                            ~
                            cs''16
                            e'8.
                            c''8.
                            as'16
                            ~
                            as'8.
                            a'16
                            ~
                            a'8
                            g'8
                            ~
                            g'16
                            cs''8.
                            ~
                            cs''16
                            e'8.
                            c''8.
                            as'16
                            ~
                            as'8.
                            a'16
                            ~
                            a'8
                            g'8
                            ~
                            g'16
                            cs''8.
                            ~
                            cs''16
                            e'8.
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
                            \mark #1
                            c''16
                            \p
                            as'16
                            ~
                            as'16
                            r16
                            r8
                            a'8
                            ~
                            a'8
                            g'16
                            cs''16
                            ~
                            cs''16
                            r8.
                            e'4
                            c''16
                            as'16
                            ~
                            as'16
                            r16
                            r8
                            a'8
                            ~
                            a'8
                            g'16
                            cs''16
                            ~
                            cs''16
                            r8.
                            e'4
                            c''16
                            as'16
                            ~
                            as'16
                            r16
                            r8
                            a'8
                            ~
                            a'8
                            g'16
                            cs''16
                            ~
                            cs''16
                            r8.
                            e'4
                            c''16
                            as'16
                            ~
                            as'16
                            r16
                            r8
                            a'8
                            ~
                            a'8
                            g'16
                            cs''16
                            ~
                            cs''16
                            r8.
                            e'4
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
                            \mark #1
                            g''16
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
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
                            \mark #1
                            g''16
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
                            g''16
                            e''16
                            r8
                            fs''16
                            r16
                            as''16
                            cs'''16
                            a''16
                            r16
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
                            \mark #1
                            c'''16
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
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
                            \mark #1
                            c'''16
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
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
                            \mark #1
                            c'''16
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
                            c'''16
                            e'''16
                            r8
                            as''16
                            r16
                            cs'''16
                            a''16
                            cs'''16
                            r16
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
                            \mark #1
                            c''8.
                            \pp
                            ^ \markup {
                                \upright
                                    legato
                                }
                            ^ \markup {
                                \upright
                                    "con sord."
                                }
                            as'16
                            ~
                            as'8.
                            a'16
                            ~
                            a'8
                            g'8
                            ~
                            g'16
                            cs''8.
                            ~
                            cs''16
                            e'8.
                            c''8.
                            as'16
                            ~
                            as'8.
                            a'16
                            ~
                            a'8
                            g'8
                            ~
                            g'16
                            cs''8.
                            ~
                            cs''16
                            e'8.
                            c''8.
                            as'16
                            ~
                            as'8.
                            a'16
                            ~
                            a'8
                            g'8
                            ~
                            g'16
                            cs''8.
                            ~
                            cs''16
                            e'8.
                            c''8.
                            as'16
                            ~
                            as'8.
                            a'16
                            ~
                            a'8
                            g'8
                            ~
                            g'16
                            cs''8.
                            ~
                            cs''16
                            e'8.
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
                            \mark #1
                            c''4
                            \pp
                            ^ \markup {
                                \upright
                                    legato
                                }
                            ^ \markup {
                                \upright
                                    "con sord."
                                }
                            ~
                            c''8
                            as'8
                            ~
                            as'4
                            ~
                            as'8
                            a'8
                            ~
                            a'4
                            g'4
                            ~
                            g'8
                            cs''8
                            ~
                            cs''4
                            ~
                            cs''8
                            e'8
                            ~
                            e'4
                            c''4
                            ~
                            c''8
                            as'8
                            ~
                            as'4
                            ~
                            as'8
                            a'8
                            ~
                            a'4
                            g'4
                            ~
                            g'8
                            cs''8
                            ~
                            cs''4
                            ~
                            cs''8
                            e'8
                            ~
                            e'4
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
                            \mark #1
                            c''2.
                            \pp
                            ^ \markup {
                                \upright
                                    legato
                                }
                            ^ \markup {
                                \upright
                                    "con sord."
                                }
                            as'4
                            ~
                            as'2.
                            a'2.
                            g'2.
                            cs''4
                            ~
                            cs''2.
                            e'2.
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
                            \mark #1
                            c'1
                            \pp
                            ^ \markup {
                                \upright
                                    legato
                                }
                            ^ \markup {
                                \upright
                                    "con sord."
                                }
                            ~
                            c'2
                            as4
                            ~
                            as2.
                            ~
                            as1
                            a2.
                            ~
                            a2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()