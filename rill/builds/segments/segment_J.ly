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
                            \mark #10
                            r4
                            \p
                            e''4
                            \staccato
                            r4
                            fs''4
                            \staccato
                            r2
                            cs''4
                            \staccato
                            r4
                            e''4
                            \staccato
                            r4
                            fs''4
                            \staccato
                            r4
                            cs''4
                            \staccato
                            r4
                            e''4
                            \staccato
                            r2
                            fs''4
                            \staccato
                            r4
                            cs''4
                            \staccato
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
                            \mark #10
                            r4
                            \p
                            e'4
                            \staccato
                            r4
                            fs'4
                            \staccato
                            r2
                            cs'4
                            \staccato
                            r4
                            e'4
                            \staccato
                            r4
                            fs'4
                            \staccato
                            r4
                            cs'4
                            \staccato
                            r4
                            e'4
                            \staccato
                            r2
                            fs'4
                            \staccato
                            r4
                            cs'4
                            \staccato
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
                            \mark #10
                            r8
                            \pp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            g''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            e''8
                            \staccato
                            r4
                            \once \override NoteHead.style = #'cross
                            fs''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            as''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            a''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            g''8
                            \staccato
                            r8
                            r8
                            \once \override NoteHead.style = #'cross
                            e''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            fs''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            as''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''8
                            \staccato
                            r4
                            \once \override NoteHead.style = #'cross
                            a''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            g''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            e''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            fs''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            as''8
                            \staccato
                            r8
                            r8
                            \once \override NoteHead.style = #'cross
                            cs'''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            a''8
                            \staccato
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
                            \mark #10
                            r8
                            \pp
                            ^ \markup {
                                \upright
                                    aeolian
                                }
                            \once \override NoteHead.style = #'cross
                            c''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            e''8
                            \staccato
                            r4
                            \once \override NoteHead.style = #'cross
                            as'8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            a'8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            c''8
                            \staccato
                            r8
                            r8
                            \once \override NoteHead.style = #'cross
                            e''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            as'8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            a'8
                            \staccato
                            r4
                            \once \override NoteHead.style = #'cross
                            cs''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            c''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            e''8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            as'8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''8
                            \staccato
                            r8
                            r8
                            \once \override NoteHead.style = #'cross
                            a'8
                            \staccato
                            r8
                            \once \override NoteHead.style = #'cross
                            cs''8
                            \staccato
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
                            \mark #10
                            gs1
                            \mf
                            e2.
                            as2.
                            ~
                            as2
                            d'4
                            ~
                            d'4
                            ~
                            d'4
                            cs'2
                            fs2.
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
                            \mark #10
                            gs'1
                            \mf
                            e'2.
                            as'2.
                            ~
                            as'2
                            d''4
                            ~
                            d''4
                            ~
                            d''4
                            cs''2
                            fs'2.
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
                            \mark #10
                            r4
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            g'''4
                            r4
                            fs'''4
                            r2
                            a'''4
                            r4
                            g'''4
                            r4
                            fs'''4
                            r4
                            a'''4
                            r4
                            g'''4
                            r2
                            fs'''4
                            r4
                            a'''4
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
                            \mark #10
                            r4
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            g'''4
                            r4
                            fs'''4
                            r2
                            a'''4
                            r4
                            g'''4
                            r4
                            fs'''4
                            r4
                            a'''4
                            r4
                            g'''4
                            r2
                            fs'''4
                            r4
                            a'''4
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
                            \mark #10
                            r4
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            g'''4
                            r4
                            fs'''4
                            r2
                            a'''4
                            r4
                            g'''4
                            r4
                            fs'''4
                            r4
                            a'''4
                            r4
                            g'''4
                            r2
                            fs'''4
                            r4
                            a'''4
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
                            \mark #10
                            r4
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            g'''4
                            r4
                            fs'''4
                            r2
                            a'''4
                            r4
                            g'''4
                            r4
                            fs'''4
                            r4
                            a'''4
                            r4
                            g'''4
                            r2
                            fs'''4
                            r4
                            a'''4
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
                            \mark #10
                            r4
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            g'''4
                            r4
                            fs'''4
                            r2
                            a'''4
                            r4
                            g'''4
                            r4
                            fs'''4
                            r4
                            a'''4
                            r4
                            g'''4
                            r2
                            fs'''4
                            r4
                            a'''4
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
                            \mark #10
                            r4
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            a''4
                            r4
                            c'''4
                            r2
                            as''4
                            r4
                            e''4
                            r4
                            g''4
                            r4
                            cs'''4
                            r4
                            a''4
                            r2
                            c'''4
                            r4
                            as''4
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
                            \mark #10
                            r4
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            a''4
                            r4
                            c'''4
                            r2
                            as''4
                            r4
                            e''4
                            r4
                            g''4
                            r4
                            cs'''4
                            r4
                            a''4
                            r2
                            c'''4
                            r4
                            as''4
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
                            \mark #10
                            r4
                            \p
                            ^ \markup {
                                \upright
                                    pizz.
                                }
                            a''4
                            r4
                            c'''4
                            r2
                            as''4
                            r4
                            e''4
                            r4
                            g''4
                            r4
                            cs'''4
                            r4
                            a''4
                            r2
                            c'''4
                            r4
                            as''4
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
                            \mark #10
                            ds''1
                            \p
                            ^ \markup {
                                \upright
                                    "sul tasto"
                                }
                            b'2.
                            es''2.
                            ~
                            es''2
                            a''4
                            ~
                            a''4
                            ~
                            a''4
                            gs''2
                            cs''2.
                        }
                    }                                                          %! rill.ScoreTemplate.__call__()
                >>                                                             %! rill.ScoreTemplate.__call__()
            >>                                                                 %! rill.ScoreTemplate.__call__()
        >>                                                                     %! rill.ScoreTemplate.__call__()
    >>                                                                         %! rill.ScoreTemplate.__call__()