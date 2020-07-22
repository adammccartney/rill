import abjad
import rill

"""
Defines scoretemplate, subclass of abjad.ScoreTemplate. Segments appended later. 
"""

class ScoreTemplate(object):
    """
    Makes a simple score template for trio 
    Violin, Monosynth and Polysynth
    """
    
    ### SPECIAL METHODS ###

    def __call__(self) -> abjad.Score:
        """
        Calls score template.
        """
        site = "rill.ScoreTemplate.__call__()"
        tag = abjad.Tag(site)

        # GLOBAL CONTEXT
        #global_context = self._make_global_context()

        # Violin
        markup_voice = abjad.Voice(name="Violin_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Violin_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Violin_Dynamics_Voice", tag=tag)
        violin_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="Violin",
            tag=tag,
        )
        abjad.annotate(
            violin_staff,
            "default_instrument",
            rill.instruments["Violin"],
        )
        abjad.annotate(violin_staff, "default_clef", abjad.Clef("treble"))

        # MonoSynth
        markup_voice = abjad.Voice(name="Monosynth_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="Monosynth_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="Monosynth_Dynamics_Voice", tag=tag)
        monosynth_staff = abjad.Staff(
            [markup_voice, music_voice, dynamics_voice],
            simultaneous=True,
            name="Monosynth",
            tag=tag,
        )
        abjad.annotate(
            monosynth_staff,
            "default_instrument",
            rill.instruments["Monosynth"],
        )
        abjad.annotate(monosynth_staff, "default_clef", abjad.Clef("treble"))


        ### RH PolySynth Voices ###
        markup_voice = abjad.Voice(name="RH_I_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="RH_I_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="RH_I_Dynamics_Voice", tag=tag)
        #rh_voice_2 = abjad.Voice(
        #            lilypond_type="RHVoiceII", name="RH_II_Music_Voice", tag=tag
        #            )
       
        # RH PolySynth Staff 
        polysynth_music_rh_staff = abjad.Staff(
                [markup_voice, music_voice, dynamics_voice],
                simultaneous=True,
                name="RH_Polysynth",
                tag=tag,
                )
        abjad.annotate(
                polysynth_music_rh_staff, "default_clef", abjad.Clef("treble")
                )
        
        ### LH PolySynth Voices ###
        markup_voice = abjad.Voice(name="LH_I_Markup_Voice", tag=tag)
        music_voice = abjad.Voice(name="LH_I_Music_Voice", tag=tag)
        dynamics_voice = abjad.Voice(name="LH_I_Dynamics_Voice", tag=tag)
        #        lh_voice_2 = abjad.Voice(
        #            lilypond_type="LHVoiceII", name="LH_II_Music_Voice", tag=tag
        #        )
        #
       
        # LH PolySynth Staff
        polysynth_music_lh_staff = abjad.Staff(
                [markup_voice, music_voice, dynamics_voice],
                simultaneous=True,
                name="LH_Polysynth",
                tag=tag,
                )
        abjad.annotate(
                polysynth_music_lh_staff, "default_clef", abjad.Clef("bass")
                )

        # PolySynth Staff Group 
        polysynth_music_staff_group = abjad.StaffGroup(
                [polysynth_music_rh_staff, polysynth_music_lh_staff],
                lilypond_type="Polysynth_Music_Staff_Group",
                name="Polysynth_Music_Staff_Group",
                tag=tag,
                )
        polysynth = rill.instruments["Polysynth"]
        abjad.annotate(polysynth_music_staff_group, "default_insrument", polysynth)

        # PolySynth Music Context
        polysynth_music_context = abjad.Context(
                [polysynth_music_staff_group],
                lilypond_type="MusicContext",
                name="Polysynth_Music_Context",
                tag=tag
                )
        
        # Music Context
        music_context = abjad.Context(
                [
                    violin_staff,
                    monosynth_staff,
                    polysynth_music_context,
                ],
                lilypond_type="MusicContext",
                simultaneous=True,
                name="Music_Context",
                tag=tag,
                )

        # Score
        score = abjad.Score(
                [music_context], name="Score", tag=tag
                )
        return score
    
    ### PRIVATE METHODS ###

    def _make_global_context(self):
        site = "abjad.ScoreTemplate._make_global_context()"
        tag = abjad.Tag(site)
        global_rests = abjad.Context(
            lilypond_type="GlobalRests", name="Global_Rests", tag=tag,
        )
        global_skips = abjad.Context(
            lilypond_type="GlobalSkips", name="Global_Skips", tag=tag,
        )
        global_context = abjad.Context(
            [global_rests, global_skips],
            lilypond_type="GlobalContext",
            simultaneous=True,
            name="Global_Context",
            tag=tag,
        )
        return global_context


    ### PUBLIC PROPERTIES ###

    @property
    def voice_abbreviations(self):
        """Gets voice abbreviations""" 
        return super(ScoreTemplate, self).voice_abbreviations


if __name__ == '__main__':
    score = ScoreTemplate()
    score_template = score()
    abjad.f(score_template)
