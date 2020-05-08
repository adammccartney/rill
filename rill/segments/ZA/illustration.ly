\version "2.19.84"                                                             %! baca.SegmentMaker._make_lilypond_file():abjad.LilyPondFile._get_format_pieces()
\language "english"                                                            %! baca.SegmentMaker._make_lilypond_file():abjad.LilyPondFile._get_format_pieces()

\include "../../stylesheets/stylesheet.ily"                                    %! baca.SegmentMaker._make_lilypond_file():abjad.LilyPondFile._get_formatted_includes()
\include "illustration.ily"                                                    %! abjad.Path.extern()
\paper { first-page-number = #1 }                                              %! __make_segment_pdf__


\score {                                                                       %! baca.SegmentMaker._make_lilypond_file():abjad.LilyPondFile._get_formatted_blocks()
    
    <<                                                                         %! baca.SegmentMaker._make_lilypond_file()

        {                                                                      %! baca.SegmentMaker._make_lilypond_file()
            \include "layout.ly"                                               %! baca.SegmentMaker._make_lilypond_file()
        }                                                                      %! baca.SegmentMaker._make_lilypond_file()

        \context Score = "Score"                                               %! ins_wasser.ScoreTemplate.__call__()
        <<                                                                     %! ins_wasser.ScoreTemplate.__call__()

            \context GlobalContext = "Global_Context"                          %! abjad.ScoreTemplate._make_global_context()
            <<                                                                 %! abjad.ScoreTemplate._make_global_context()

                \context GlobalSkips = "Global_Skips"                          %! abjad.ScoreTemplate._make_global_context()
                \ZA_Global_Skips                                               %! abjad.Path.extern()

            >>                                                                 %! abjad.ScoreTemplate._make_global_context()

            \context MusicContext = "Music_Context"                            %! ins_wasser.ScoreTemplate.__call__()
            {                                                                  %! ins_wasser.ScoreTemplate.__call__()

                \context PianoStaff = "Piano_Staff"                            %! ins_wasser.ScoreTemplate.__call__()
                <<                                                             %! ins_wasser.ScoreTemplate.__call__()

                    \context Staff = "Viola_I"                                 %! ins_wasser.ScoreTemplate.__call__()
                    \ZA_Viola_I                                                %! abjad.Path.extern()

                    \context Staff = "Viola_II"                                %! ins_wasser.ScoreTemplate.__call__()
                    \ZA_Viola_II                                               %! abjad.Path.extern()

                >>                                                             %! ins_wasser.ScoreTemplate.__call__()

            }                                                                  %! ins_wasser.ScoreTemplate.__call__()

        >>                                                                     %! ins_wasser.ScoreTemplate.__call__()

    >>                                                                         %! baca.SegmentMaker._make_lilypond_file()
    
}                                                                              %! baca.SegmentMaker._make_lilypond_file():abjad.LilyPondFile._get_formatted_blocks()