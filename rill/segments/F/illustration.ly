\version "2.19.84"                                                             %! abjad.LilyPondFile._get_format_pieces()
\language "english"                                                            %! abjad.LilyPondFile._get_format_pieces()

#(ly:set-option 'relative-includes #t)

\include "../../stylesheets/stylesheet.ily"                                    %! abjad.LilyPondFile._get_formatted_includes()

\header {                                                                      %! abjad.LilyPondFile._get_formatted_blocks()
    title = ##f
    composer = ##f
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()
\include "illustration.ily"                                                    %! abjad.Path.extern()


\score {                                                                       %! abjad.LilyPondFile._get_formatted_blocks()
    \context Score = "Score"                                                   %! ins_wasser.ScoreTemplate.__call__()
    <<                                                                         %! ins_wasser.ScoreTemplate.__call__()
        \context GlobalContext = "Global_Context"                              %! abjad.ScoreTemplate._make_global_context()
        <<                                                                     %! abjad.ScoreTemplate._make_global_context()
            \context GlobalRests = "Global_Rests"                              %! abjad.ScoreTemplate._make_global_context()
            \F_Global_Rests                                                    %! abjad.Path.extern()
            \context GlobalSkips = "Global_Skips"                              %! abjad.ScoreTemplate._make_global_context()
            \F_Global_Skips                                                    %! abjad.Path.extern()
        >>                                                                     %! abjad.ScoreTemplate._make_global_context()
        \context MusicContext = "Music_Context"                                %! ins_wasser.ScoreTemplate.__call__()
        {                                                                      %! ins_wasser.ScoreTemplate.__call__()
            \context PianoStaff = "Piano_Staff"                                %! ins_wasser.ScoreTemplate.__call__()
            <<                                                                 %! ins_wasser.ScoreTemplate.__call__()
                \context Staff = "Viola_I"                                     %! ins_wasser.ScoreTemplate.__call__()
                \F_Viola_I                                                     %! abjad.Path.extern()
                \context Staff = "Viola_II"                                    %! ins_wasser.ScoreTemplate.__call__()
                \F_Viola_II                                                    %! abjad.Path.extern()
            >>                                                                 %! ins_wasser.ScoreTemplate.__call__()
        }                                                                      %! ins_wasser.ScoreTemplate.__call__()
    >>                                                                         %! ins_wasser.ScoreTemplate.__call__()
}                                                                              %! abjad.LilyPondFile._get_formatted_blocks()