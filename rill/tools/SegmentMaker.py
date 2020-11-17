import os
import pathlib

import abjad
import copy
import rill

from abjadext import rmakers

"""Design of RhythmDefinition and SegmentMaker
   borrowed gratefully from Trevor Baca's ins_wasser repository"""


class RhythmDefinition(object):
    """
    Rhythm definition.

    """

    # CLASS ATTRIBUTES #

    __slots__ = ("_score", "dynamics", "instrument_name", "markup", "notes")

    # INITIALIZER #

    def __init__(
        self, dynamics=None, instrument_name=None, markup=None, notes=None
    ):
        self.dynamics = dynamics or []
        self.instrument_name = instrument_name
        self.markup = markup or []
        self.notes = notes or []

    # SPECIAL METHODS #

    def __call__(self, score):
        """
        Calls rhythm definition.

        Returns none.
        """
        self._score = score
        self._handle_notes()
        #self._handle_dynamics()
        #self._handle_markup()

    def __format__(self, format_specification="") -> str:
        """
        Formats articulation.
        """
        return abjad.StorageFormatManager(self).get_storage_format()

    # PRIVATE METHODS #

    def _get_music_voices(self):
        return (
                self._score["Flute1_Music_Voice"],
                self._score["Flute2_Music_Voice"],
                self._score["Flute3_Music_Voice"],
                self._score["Flute4_Music_Voice"],
                self._score["Bbclarinet1_Music_Voice"],
                self._score["Vibraphone_Music_Voice"],
                self._score["Violin1_Music_Voice"],
                self._score["Violin2_Music_Voice"],
                self._score["Violin3_Music_Voice"],
                self._score["Violin4_Music_Voice"],
                self._score["Violin5_Music_Voice"],
                self._score["Violin6_Music_Voice"],
                self._score["Violin7_Music_Voice"],
                self._score["Violin8_Music_Voice"],
                self._score["Viola_Music_Voice"],
        )

    def _get_staves(self):
        return (
                self._score["Flute1"],
                self._score["Flute2"],
                self._score["Flute3"],
                self._score["Flute4"],
                self._score["Bbclarinet1"],
                self._score["Vibraphone"],
                self._score["Violin1"],
                self._score["Violin2"],
                self._score["Violin3"],
                self._score["Violin4"],
                self._score["Violin5"],
                self._score["Violin6"],
                self._score["Violin7"],
                self._score["Violin8"],
                self._score["Viola"],
        )

    #def _handle_dynamics(self):
    #    voice = self._score[f"{self.instrument_name}_Music_Voice"]
    #    leaves = abjad.select(voice).leaves()
    #    if not leaves:
    #        return
    #    music_durations = [abjad.inspect(_).duration() for _ in leaves]
    #    maker = rmakers.multiplied_duration(abjad.Skip)
    #    dynamics_skips = maker(music_durations)
    #    dynamics_voice = self._score[f"{self.instrument_name}_Dynamics_Voice"]
    #    dynamics_voice.extend(dynamics_skips)
    #    for expression in self.dynamics:
    #        index = expression[0]
    #        string = expression[1]
    #        leaf = dynamics_voice[index]
    #        if string in ("<", ">"):
    #            indicator = abjad.LilyPondLiteral("\\" + string, "after")
    #        elif string == "-|":
    #            indicator = abjad.LilyPondLiteral(r"\<", "after")
    #            stencil = abjad.Scheme("constante-hairpin")
    #            abjad.override(leaf).hairpin.stencil = stencil
    #        elif string == "<!":
    #            indicator = abjad.LilyPondLiteral(r"\<", "after")
    #            stencil = abjad.Scheme("abjad-flared-hairpin")
    #            abjad.override(leaf).hairpin.stencil = stencil
    #        elif string == "!>":
    #            indicator = abjad.LilyPondLiteral(r"\>", "after")
    #            stencil = abjad.Scheme("abjad-flared-hairpin")
    #            abjad.override(leaf).hairpin.stencil = stencil
    #        else:
    #            indicator = abjad.Dynamic(string)
    #        abjad.attach(indicator, leaf)
    #        if len(expression) == 3:
    #            staff_padding = expression[2]
    #            string = r"\override DynamicLineSpanner.staff-padding ="
    #            string += f" {staff_padding}"
    #            command = abjad.LilyPondLiteral(string)
    #            abjad.attach(command, leaf)
    #    last_leaf = dynamics_voice[-1]
    #    prototype = abjad.LilyPondLiteral
    #    if not abjad.inspect(last_leaf).has_indicator(prototype):
    #        if not abjad.inspect(last_leaf).has_indicator(abjad.Dynamic):
    #            indicator = abjad.LilyPondLiteral(r"\!", "after")
    #            abjad.attach(indicator, last_leaf)

    #def _handle_markup(self):
    #    voice = self._score[f"{self.instrument_name}_Music_Voice"]
    #    leaves = abjad.select(voice).leaves()
    #    if not leaves:
    #        return
    #    music_durations = [abjad.inspect(_).duration() for _ in leaves]
    #    maker = rmakers.multiplied_duration(abjad.Skip)
    #    selections = maker(music_durations)
    #    skips = abjad.select(selections).components(abjad.Skip)
    #    markup_voice = self._score[f"{self.instrument_name}_Markup_Voice"]
    #    markup_voice.extend(skips)
    #    expressions = self.markup
    #    for i, expression in enumerate(expressions):
    #        index = expression[0]
    #        markup = expression[1]
    #        skip = skips[index]
    #        if len(expression) == 3 and isinstance(expression[2], tuple):
    #            abjad.attach(markup, skip)
    #            extra_offset = expression[2]
    #            x, y = extra_offset
    #            string = r"\once \override TextScript.extra-offset"
    #            string += f" = #'({x} . {y})"
    #            command = abjad.LilyPondLiteral(string)
    #            abjad.attach(command, skip)
    #            continue
    #        if 0 < i:
    #            stop_text_span = abjad.StopTextSpan()
    #            abjad.attach(stop_text_span, skip)
    #        if isinstance(markup, list):
    #            markup = markup[0]
    #            style = "dashed-line-with-arrow"
    #        else:
    #            style = "invisible-line"
    #        start_text_span = abjad.StartTextSpan(
    #            left_text=markup, style=style
    #        )
    #        abjad.attach(start_text_span, skip)
    #        if len(expression) == 3:
    #            staff_padding = expression[2]
    #            string = (
    #                fr"\override TextScript.staff-padding = {staff_padding}"
    #            )
    #            command = abjad.LilyPondLiteral(string)
    #            abjad.attach(command, skip)
    #            value = staff_padding + 0.75
    #            string = fr"\override TextSpanner.staff-padding = {value}"
    #            command = abjad.LilyPondLiteral(string)
    #            abjad.attach(command, skip)
    #    stop_text_span = abjad.StopTextSpan()
    #    abjad.attach(stop_text_span, skips[-1])

    def _handle_notes(self):
        voice = self._score[f"{self.instrument_name}_Music_Voice"]
        print(self.notes)
        for argument in self.notes:
            if isinstance(argument, abjad.Component):
                copied_expr = copy.deepcopy(argument)
                voice.append(copied_expr)
            elif isinstance(argument, abjad.Container):
                copied_expr = copy.deepcopy(argument)
                voice.append(copied_expr)
            elif isinstance(argument, str):
                if argument.startswith("r"):
                    rest = abjad.Rest(argument)
                    voice.append(rest)
                else:
                    raise ValueError(f"what is {argument!r}?")
            elif isinstance(argument, tuple):
                component = self._tuple_to_component(argument)
                voice.append(component)
            else:
                raise ValueError(f"what is {argument!r}?")

    def _make_leaf(self, pitch, duration_string):
        duration = abjad.Duration(duration_string)
        maker = abjad.LeafMaker()
        leaves = maker([pitch], [duration])
        return leaves

    def _tuple_to_component(self, argument):
        pitch_string = argument[0]
        duration = argument[1]
        if isinstance(argument[0], abjad.Component):
            component = argument[0]
        elif " " in pitch_string:
            component = abjad.Chord([], duration)
            pitches = pitch_string.split()
            for pitch in pitches:
                component.note_heads.append(pitch)
        else:
            component = abjad.Note(pitch_string, duration)
        for indicator in argument[2:]:
            if indicator == "parenthesize":
                if isinstance(component, abjad.Note):
                    component.note_head.is_parenthesized = True
                elif isinstance(component, abjad.Chord):
                    for note_head in component.note_heads:
                        note_head.is_parenthesized = True
            else:
                copied_indicator = copy.deepcopy(indicator)
                abjad.attach(copied_indicator, component)
        return component


class SegmentMaker(abjad.SegmentMaker):
    """Segment Maker definition for marana
    makes a persistent section of the score.
    """

    __slots__ = (
            "_lilypond_file",
            "_score",
            "_rhythm_definitions",
            "build_path",
            "current_directory",
            "markup_leaves",
            "metronome_marks",
            "rehearsal_mark",
            "segment_name",
            "tempo",
            "time_signatures",
            )

    def __init__(
            self,
            _lilypond_file=None,
            _score=None,
            build_path=None,
            current_directory=None,
            markup_leaves=None,
            metronome_marks=None,
            segment_name=None,
            rehearsal_mark=None,
            tempo=None,
            time_signatures=None,
         ):
        super(SegmentMaker, self).__init__()
        self._lilypond_file = None
        self._rhythm_definitions = []
        self._score = _score
        self.build_path = build_path
        self.current_directory = current_directory
        self.markup_leaves = markup_leaves
        self.metronome_marks = metronome_marks or []
        self.segment_name = segment_name
        self.rehearsal_mark = rehearsal_mark
        self.tempo = ((1, 4), 60)
        self.time_signatures = time_signatures or []

    # PRIVATE PROPERTIES #
    @property
    def _music_voices(self):
        """Returns quadruple of staves from score"""
        return (
                self._score["Flute1_Music_Voice"],
                self._score["Flute2_Music_Voice"],
                self._score["Flute3_Music_Voice"],
                self._score["Flute4_Music_Voice"],
                self._score["Bbclarinet1_Music_Voice"],
                self._score["Vibraphone_Music_Voice"],
                self._score["Violin1_Music_Voice"],
                self._score["Violin2_Music_Voice"],
                self._score["Violin3_Music_Voice"],
                self._score["Violin4_Music_Voice"],
                self._score["Violin5_Music_Voice"],
                self._score["Violin6_Music_Voice"],
                self._score["Violin7_Music_Voice"],
                self._score["Violin8_Music_Voice"],
                self._score["Viola_Music_Voice"],
                )

    # PRIVATE METHODS #
    def _attach_leaf_index_markup(self):
        if not self.markup_leaves:
            return
        for voice in self._music_voices:
            logical_ties = abjad.iterate(voice).logical_ties()
            for i, logical_tie in enumerate(logical_ties):
                markup = abjad.Markup(i)
                abjad.attach(markup, logical_tie.head)

    def _build_segment(self):
        directory = self.current_directory
        file = open(f"{directory}/illustration.ly", 'r')
        score_content = file.readlines()
        file.close()
        build_path = (self.build_path / "segments").resolve()
        file = open(f"{build_path}/{self.segment_name}.ly", 'w')
        file.writelines(score_content[13:-1])
        file.close()

    def _render_illustration(self):
        score_file = self._lilypond_file
        directory = self.current_directory
        pdf_path = f"{directory}/illustration.pdf"
        ly_path = f"{directory}/illustration.ly"
        path = pathlib.Path("illustration.pdf")
        if path.exists():
            print(f"Removing {pdf_path} ...")
            path.unlink()
        print(f"Persisting {pdf_path} ...")
        result = abjad.persist(score_file).as_pdf(pdf_path, strict=79)
        if path.exists():
            print(f"Opening {pdf_path} ...")
            os.system(f"open {pdf_path}")

    def _call_rhythm_definitions(self):
        for rhythm_definition in self._rhythm_definitions:
            rhythm_definition(self._score)

    def _configure_lilypond_file(self):
        lilypond_file = self._lilypond_file
        lilypond_file.header_block.title = None
        lilypond_file.header_block.composer = None

    def _configure_rehearsal_mark(self):
        mark_num = self.rehearsal_mark
        voices = self._music_voices
        for voice in voices:
            print("at voice: ", voice)
            leaf = abjad.inspect(voice).leaf(0)
            print("this is the leaf: ", leaf)
            abjad.attach(abjad.RehearsalMark(number=mark_num), leaf)
        scheme = abjad.Scheme('format-mark-box-alphabet')
        score = self._score
        abjad.setting(score).markFormatter = scheme

    def _sort_instruments_by_clef(self, voice_list, target):
        if isinstance(voice_list, list):
            for i in range(len(voice_list)):
                target.append(voice_list[i])
            return target
        else:
            single_voice = voice_list
            target.append(single_voice)
            return target

    def _configure_score(self):
        voices = self._music_voices  # list of voices
        treble_voices = voices[:-1]
        alto_voice = voices[-1]
        for voice in treble_voices:
            leaf = abjad.inspect(voice).leaf(0)
            abjad.attach(abjad.Clef("treble"), leaf)
        leaf = abjad.inspect(alto_voice).leaf(0)
        abjad.attach.inspect(abjad.Clef("alto"), leaf)

        #treble, alto, bass = [], [], []
        #temp = voices[0:11]  # fl x3 , Bbclarinet, vb, vn x7
        #temp = voices[12]
        #self._sort_instruments_by_clef(temp, alto)  # va

    def _handle_metronome_marks(self):
        if not self.metronome_marks:
            return
        context = self._score["Global_Skips"]
        skips = abjad.select(context).components(abjad.Skip)
        skip_count = len(skips)
        for i, expression in enumerate(self.metronome_marks):
            index = expression[0]
            if index < 0:
                index = skip_count + index
            skip = skips[index]
            indicator = expression[1]
            trend = None
            if isinstance(indicator, list):
                assert len(indicator) == 2, repr(indicator)
                indicator, trend = indicator
                trend = copy.copy(trend)
            indicator = copy.copy(indicator)

    def _handle_time_signatures(self):
        if not self.metronome_marks:
            return
        context = self._score["Global_Skips"]
        skips = []
        for item in self.time_signatures:
            skip = abjad.Skip(1, multiplier=item)
            time_signature = abjad.TimeSignature(item)
            abjad.attach(time_signature, skip, context="Score")
            skips.append(skip)
        context.extend(skips)
        context = self._score["Global_Rests"]
        rests = []
        for item in self.time_signatures:
            rest = abjad.MultimeasureRest(1, multiplier=item)
            rests.append(rest)
        context.extend(rests)

    def _make_lilypond_file(self):
        path = "../../stylesheets/stylesheet.ily"
        lilypond_file = abjad.LilyPondFile.new(
            music=self._score, includes=[path], use_relative_includes=True
        )
        delattr(lilypond_file.header_block, "tagline")
        for item in lilypond_file.items[:]:
            if getattr(item, "name", None) in ("layout", "paper"):
                lilypond_file.items.remove(item)
        self._lilypond_file = lilypond_file

    # PUBLIC METHODS #

    def define_rhythm(self):
        """
        Makes rhythm definition
        Returns rhythm definition
        """
        rhythm_definition = RhythmDefinition()
        self._rhythm_definitions.append(rhythm_definition)
        return rhythm_definition

    def run(self):
        """
        Runs segment maker

        Returns Lilypond file
        """
        print("# STARTING RUN #")
        self._make_lilypond_file()
        self._configure_lilypond_file()
        self._handle_time_signatures()
        # self._handle_metronome_marks()
        self._call_rhythm_definitions()
        self._configure_score()
        self._configure_rehearsal_mark()
        self._attach_leaf_index_markup()
        self._render_illustration()
        self._build_segment()
        return self._lilypond_file
