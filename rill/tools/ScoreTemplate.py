import abjad
import rill

"""
Defines scoretemplate, subclass of abjad.ScoreTemplate. Segments appended later. 
"""



class ScoreTemplate(abjad.ScoreTemplate):
    """
    Makes a simple score template for trio 
    Violin, Monosynth and Polysynth
    """
    
    ### CLASS VARIABLES ###

    __documentation_section__ = None

    _always_make_global_rests = True

    _global_rests_in_topmost_staff = True

    def __init__(self):
        super(ScoreTemplate, self).__init__()
        self.voice_abbreviations.update(
            {
                "vn": "Violin_Music_Voice", 
                "msy" : "MonoSynth_Music_Voice",
                "rh_v1": "RH_I_Music_Voice",
                #"rh_v2": "RH_II_Music_Voice",
                "lh_v1": "LH_I_Music_Voice",
                #"lh_v2": "LH_II_Music_Voice",
                }
        )

    ### SPECIAL METHODS ###

    def __call__(self) -> abjad.Score:
        """
        Calls score template.
        """
        site = "rill.ScoreTemplate.__call__()"
        tag = abjad.Tag(site)

        # GLOBAL CONTEXT
        global_context = self._make_global_context()

        # Violin
        music_voice = abjad.Voice(name="Violin_Music_Voice", tag=tag)
        violin_staff = abjad.Staff(
            [music_voice],
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
        music_voice = abjad.Voice(name="Monosynth_Music_Voice", tag=tag)
        monosynth_staff = abjad.Staff(
            [music_voice],
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
        music_voice = abjad.Voice(name="RH_I_Music_Voice", tag=tag)

        #rh_voice_2 = abjad.Voice(
        #            lilypond_type="RHVoiceII", name="RH_II_Music_Voice", tag=tag
        #            )
       
        # RH PolySynth Staff 
        polysynth_music_rh_staff = abjad.Staff(
                [music_voice],
                simultaneous=True,
                name="RH_Polysynth",
                tag=tag,
                )
        abjad.annotate(
                polysynth_music_rh_staff, "default_clef", abjad.Clef("treble")
                )
        
        ### LH PolySynth Voices ###
        music_voice = abjad.Voice(name="LH_I_Music_Voice", tag=tag)
        #        lh_voice_2 = abjad.Voice(
        #            lilypond_type="LHVoiceII", name="LH_II_Music_Voice", tag=tag
        #        )
        #
       
        # LH PolySynth Staff
        polysynth_music_lh_staff = abjad.Staff(
                [music_voice],
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
                lilypond_type="PolySynthMusicStaffGroup",
                name="PolySynth_Music_Staff_Group",
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
                [global_context, music_context], name="Score", tag=tag
                )
        return score

    ### PUBLIC PROPERTIES ###

    @property
    def voice_abbreviations(self):
        """Gets voice abbreviations""" 
        return super(ScoreTemplate, self).voice_abbreviations


   
