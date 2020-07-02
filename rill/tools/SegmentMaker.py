import pathlib

import abjad
import copy
import rill
import mccartney 

from rill.tools.PhraseMaker import PhraseOutflow as PhraseOutflow

class SegmentMaker(object):
    """Segment Maker definition for rill
    makes a persistent section of the score.
    """

    __slots__ = (
            "_lilypond_file",
            "_score",
            "_phrase_outflows",
            "build_path",
            "current_directory",
            "segment_name",
            "tempo",
            "time_signatures",
            )



    def __init__(
            self,
            _lilypond_file=None,
            _score=None,
            _phrase_outflows=None,
            build_path=None,
            current_directory=None, 
            segment_name=None, 
            tempo=None,
            time_signatures=None,
        ):
            self._lilypond_file = None
            self._phrase_outflows = []
            self._score = _score
            self.build_path = build_path
            self.current_directory = current_directory
            self.segment_name = segment_name
            self.tempo = ((1, 4), 60)
            self.time_signatures = time_signatures 

    def _build_segment(self):
        current_directory = self.current_directory 
        score_content = open(f"{directory}/illustration.ly").readlines()
        build_path = (self.build_path / "score").resolve()
        open(f"{build_path}/{self.segment_name}.ly").writelines(score_content)

    def _render_illustration(self):
        score_file = self._lilypond_file
        directory = self.current_directory
        print("direcitory: ", directory)
        pdf_path = f"{directory}/illustration.pdf"
        print("pdf_path: ", pdf_path)
        #ly_path = f"{directory}/illustration.ly"
        path = pathlib.Path("illustration.pdf")
        if path.exists():
            print(f"Removing {pdf_path} ...")
            path.unlink()
        print(f"Persisting {pdf_path} ...")
        result = abjad.persist(score_file).as_pdf(pdf_path, strict=79) 
        if path.exists():
            print(f"Opening {pdf_path} ...")
            os.system(f"open {pdf_path}")

    def _make_lilypond_file(self, midi=False):
        path = abjad.Path('rill', 'stylesheets', 'contexts.ily')
        lilypond_file = abjad.LilyPondFile.new(
                music=self._score, includes=[path], use_relative_includes=True
                )
        delattr(lilypond_file.header_block, "tagline")
        for item in lilypond_file.items[:]:
            if getattr(item, "name", None) in ("layout", "paper"):
                lilypond_file.items.remove(item)
        self._lilypond_file = lilypond_file


    def stream_phrases(self, instrument_name, phrases):
        """
        Calls a PhraseOutflow
        Streams phrases to a voice in score
        """
        phrase_outflow = PhraseOutflow()
        phrase_outflow.instrument_name = instrument_name
        phrase_outflow.phrases = phrases
        self._phrase_outflows.append(phrase_outflow)
        return phrase_outflow

    def _call_phrase_outflows(self):
        """
        Phrase streams flow into score by instrument_name
        """
        for phrase_outflow in self._phrase_outflows:
            phrase_outflow(self._score)

    def run(self):
        """
        Runs segment maker
        
        Returns Lilypond file
        """
        self._make_lilypond_file()
        self._call_phrase_outflows()
        self._render_illustration()
        return self._lilypond_file


if __name__ == '__main__':
    import rill.tools.FuzzyHarmony as FuzzyHarmony
    import rill.tools.PhraseMaker as PhraseMaker
    from rill.tools.PhraseMaker import PhraseStream as PhraseStream
    

    ## Set up segment 
    test_current_directory = pathlib.Path(__file__).parent
    test_build_path = (pathlib.Path(__file__).parent/".."/"build").resolve()
    score = rill.ScoreTemplate()
    score_template = score()

    segment_maker = rill.SegmentMaker(
                                      _lilypond_file=None,
                                      _phrase_outflows=None,
                                      _score=score_template,
                                      current_directory=test_current_directory,
                                      build_path=test_build_path,
                                      segment_name='A',
                                      tempo=((1, 4), 50),
                                      time_signatures=([(4, 4)] * 20),
                                    )


    ## Set up material for segment 

    durations = [
            abjad.Duration(1, 2), 
            abjad.Duration(3, 4), 
            abjad.Duration(3, 4), 
            abjad.Duration(3, 2),
            abjad.Duration(1, 2),
            ]
    
    harmony_one = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
    harmony_two = FuzzyHarmony('bf_ii', abjad.PitchSegment("g' bf' c'' ef''"), 2) 
    harmony_three = FuzzyHarmony('bf_ii', abjad.PitchSegment("bf' c'' ef'' g''"), 3)   
    harmony_four = FuzzyHarmony('bf_ii', abjad.PitchSegment("c'' ef'' g'' bf''"), 0)
 
    pitch_lists = [
              harmony_one.numbered_pitch_list,
              harmony_two.numbered_pitch_list,
              harmony_three.numbered_pitch_list,
              harmony_four.numbered_pitch_list,
              ]

    # Routine to order material into containers

    dry_phrase_stream = PhraseStream([])
    def order_material(pitch_lists, durations, phrase_stream):
        """Makes phrases and adds them to stream"""
        for items in pitch_lists:
            pitches = items
            pitches.append(None)
            phrase_stream.make_extension(pitches, durations)
        return phrase_stream
   
    wet_phrase_stream = order_material(
                                       pitch_lists, 
                                       durations, 
                                       dry_phrase_stream,
                                    )  

    list_phrases = wet_phrase_stream.phrases
    print("list phrase :", list_phrases)
    components = wet_phrase_stream.components
    print("phrase stream components :", components)

    phrase_outflow = segment_maker.stream_phrases(
                                                  instrument_name = "LH_I", 
                                                  phrases = list_phrases,
                                                  )

    lilypond_file = segment_maker.run()
   # Routine to order 


#   
#    phrases = PhraseCatcher("Violin", caught_phrases)    
#    
#
#    routed_score = phrases(segment_maker.score)
#    #abjad.f(routed_score) 
#    liypond_file = segment_maker.run()
#
#
#
