import os
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
        directory = self.current_directory 
        file = open(f"{directory}/illustration.ly", 'r')
        score_content = file.readlines()
        file.close()
        print("score content: ", score_content[13:-1])
        build_path = (self.build_path / "segments").resolve()
        print("build_path: ", build_path)
        print("file to build: ", f"{self.segment_name}.ly")
        file = open(f"{build_path}/{self.segment_name}.ly", 'w')
        file.writelines(score_content[13:-1])
        file.close()

    def _render_illustration(self):
        score_file = self._lilypond_file
        directory = self.current_directory
        print("directory: ", directory)
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

    def _configure_lilypond_file(self):
        lilypond_file = self._lilypond_file
        lilypond_file.header_block.title = None
        lilypond_file.header_block.composer = None

    def _configure_score(self):
        voices  = self._get_voices()
        for voice in voices[0:3]: # violin, monosynth, rh polysynth 
            leaf = abjad.inspect(voice).leaf(0)
            abjad.attach(abjad.Clef("treble"), leaf)
        voice = voices[3]  # lh polysynth
        leaf = abjad.inspect(voice).leaf(0)
        abjad.attach(abjad.Clef("bass"), leaf)

    def _get_voices(self):
        """Returns quadruple of staves from score"""
        return (
                self._score["Violin_Music_Voice"],
                self._score["Monosynth_Music_Voice"],
                self._score["RH_I_Music_Voice"],
                self._score["LH_I_Music_Voice"],
                )

    def run(self):
        """
        Runs segment maker
        
        Returns Lilypond file
        """
        self._make_lilypond_file()
        self._configure_lilypond_file()
        self._call_phrase_outflows()
        self._configure_score()    # only needed in first segment / special cases
        self._render_illustration()
        self._build_segment()
        return self._lilypond_file

