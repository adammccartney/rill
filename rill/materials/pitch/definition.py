import abjad
import rill


"""
  Dictionary of chord voices used:
      Breaking line length style rules, as there seems to be trouble
      initializing the PitchSegment objects otherwise
"""


chord_voicf = abjad.OrderedDict([
    ("blue", abjad.OrderedDict([
        (0, abjad.PitchSegment(
            "f,,, fs,,, d,,, d,,, f,,, as,,, a,,, c,, c,,"
        )),
        (1, abjad.PitchSegment(
            "f,, fs,, d,, d,, f,, as,, a,, c, c,"
        )),
        (2, abjad.PitchSegment(
            "f, fs, d, d, f, as, a, c c"
        )),
        (3, abjad.PitchSegment(
            "f fs d d f as a c' c'"
        )),
        (4, abjad.PitchSegment(
            "f' fs' d' d' f' as' a' c'' c''"
        )),
        (5, abjad.PitchSegment(
            "f'' fs'' d'' d'' f'' as'' a'' c''' c'''"
        )),
        (6, abjad.PitchSegment(
            "f''' fs''' d''' d''' f''' as''' a''' c'''' c''''"
        )),
        (7, abjad.PitchSegment(
            "f'''' fs'''' d'''' d'''' f'''' as'''' a'''' c''''' c'''''"
        )),
        (8,
         abjad.PitchSegment(
             "f''''' fs''''' d''''' d''''' f''''' as''''' a''''' c'''''' c''''''"
         )),
    ])),
    ("green", abjad.OrderedDict([
        (0, abjad.PitchSegment(
            "g,,, fs,,, a,,, a,,, b,,, d,, d,, bf,,, d,,"
        )),
        (1, abjad.PitchSegment(
            "g,, fs,, a,, a,, b,, d, d, bf,, d,"
        )),
        (2, abjad.PitchSegment(
            "g, fs, a, a, b, d d bf, d"
        )),
        (3, abjad.PitchSegment(
            "g fs a a b d' d' bf d'"
        )),
        (4, abjad.PitchSegment(
            "g' fs' a' a' b' d'' d'' bf' d''"
        )),
        (5, abjad.PitchSegment(
            "g'' fs'' a'' a'' b'' d''' d''' bf'' d'''"
        )),
        (6,
         abjad.PitchSegment(
             "g''' fs''' a''' a''' b''' d'''' d'''' bf''' d''''"
         )),
        (7,
         abjad.PitchSegment(
             "g'''' fs'''' a'''' a'''' b'''' d''''' d''''' bf'''' d'''''"
         )),
        (8,
         abjad.PitchSegment(
             "g''''' fs''''' a''''' a''''' b''''' d'''''' d'''''' bf''''' d''''''"
         )),
    ])),
    ("red", abjad.OrderedDict([
        (0, abjad.PitchSegment(
            "g,,, d,, f,,, f,,, g,,, g,,, a,,, g,,, f,,,"
        )),
        (1, abjad.PitchSegment(
            "g,, d, f,, f,, g,, g,, a,, g,, f,,"
        )),
        (2, abjad.PitchSegment(
            "g, d f, f, g, g, a, g, f,"
            )),
        (3, abjad.PitchSegment(
            "g d' f f g g a g f"
        )),
        (4, abjad.PitchSegment(
            "g' d'' f' f' g' g' a' g' f'"
            )),
        (5, abjad.PitchSegment(
            "g'' d''' f'' f'' g'' g'' a'' g'' f''"
            )),
        (6, abjad.PitchSegment(
            "g''' d'''' f''' f''' g''' g''' a''' g''' f'''"
            )),
        (7, abjad.PitchSegment(
            "g'''' d''''' f'''' f'''' g'''' g'''' a'''' g'''' f''''"
            )),
        (8, abjad.PitchSegment(
            "g''''' d'''''' f''''' f''''' g''''' g''''' a''''' g''''' f'''''"
            )),
    ])),
    ("black", abjad.OrderedDict([
        (0, abjad.PitchSegment(
            "c,, as,,, a,,, a,,, g,,, fs,,, f,,, ff,,, d,,,"
            )),
        (1, abjad.PitchSegment(
            "c, as,, a,, a,, g,, fs,, f,, ff,, d,,"
            )),
        (2, abjad.PitchSegment(
            "c as, a, a, g, fs, f, ff, d,"
            )),
        (3, abjad.PitchSegment(
            "c' as a a g fs f ff d"
            )),
        (4, abjad.PitchSegment(
            "c'' as' a' a' g' fs' f' ff' d'"
            )),
        (5, abjad.PitchSegment(
            "c''' as'' a'' a'' g'' fs'' f'' ff'' d''"
            )),
        (6, abjad.PitchSegment(
            "c'''' as''' a''' a''' g''' fs''' f''' ff''' d'''"
            )),
        (7, abjad.PitchSegment(
            "c''''' as'''' a'''' a'''' g'''' fs'''' f'''' ff'''' d''''"
            )),
        (8, abjad.PitchSegment(
            "c'''''' as''''' a''''' a''''' g''''' fs''''' f''''' ff''''' d'''''"
            )),
    ])),
])


melody_voice = abjad.OrderedDict([
    ("blue", abjad.OrderedDict([
        ("p1", abjad.OrderedDict([
            (1, abjad.PitchSegment("f c g as a d")),
            (2, abjad.PitchSegment("f' c' g' as' a' d'")),
            (3, abjad.PitchSegment("b' g' d'' g'' f'' a'")),
            (4, abjad.PitchSegment("f'' c'' g'' as'' a'' d''")),
            (5, abjad.PitchSegment("g'' f'' as'' d''' d''' g''")),
            (6, abjad.PitchSegment("b'' g'' d''' g''' f''' a''")),
            (8, abjad.PitchSegment("f''' c''' g''' as''' a''' d'''")),
            (10, abjad.PitchSegment("g''' f''' as''' ds'''' d'''' g'''")),
            ])
         ),
        ("p2", abjad.OrderedDict([
            (1, abjad.PitchSegment("d a, d f g g a")),
            (2, abjad.PitchSegment("d' a d' f' g' g' a'")),
            (3, abjad.PitchSegment("a' f' a' b' ds'' d'' f''")),
            (4, abjad.PitchSegment("d'' a' d'' f'' g'' g'' a''")),
            (5, abjad.PitchSegment("g'' d'' g'' g'' bs'' as'' d'''")),
            (6, abjad.PitchSegment("a'' f'' a'' b'' ds''' d''' f'''")),
            (8, abjad.PitchSegment("d''' a'' d''' f''' g''' g''' a'''")),
            (10, abjad.PitchSegment("g''' d''' g''' g''' bs''' as''' d''''")),
            ])
         ),
        ("p3", abjad.OrderedDict([
            (1, abjad.PitchSegment("a f c' ff d g")),
            (2, abjad.PitchSegment("a' f' c'' ff' d' g'")),
            (3, abjad.PitchSegment("f'' c'' g'' bf' a'' d''")),
            (4, abjad.PitchSegment("a'' f'' c''' ff'' d'' g''")),
            (5, abjad.PitchSegment("d''' a'' f''' g'' g'' b''")),
            (6, abjad.PitchSegment("f''' c''' g''' bf'' a''' d'''")),
            (8, abjad.PitchSegment("a''' f''' c'''' ff''' d''' g'''")),
            (10, abjad.PitchSegment("d'''' a''' f'''' g''' g''' b'''")),
            ])
         ),
    ])),
    ("green", abjad.OrderedDict([
        ("p1", abjad.OrderedDict([
            (1, abjad.PitchSegment("g g' as d' ds' f' a'")),
            (2, abjad.PitchSegment("g' g'' as' d'' ds'' f'' a''")),
            (3, abjad.PitchSegment("d'' d''' g'' g'' as'' b'' f'''")),
            (4, abjad.PitchSegment("g'' g''' as'' d''' ds''' f''' a'''")),
            (5, abjad.PitchSegment("b'' b''' ds''' g''' gs''' g''' d''''")),
            (6, abjad.PitchSegment("d''' d'''' g''' g''' as''' b''' f''''")),
            (8, abjad.PitchSegment("g''' g'''' as''' d'''' ds'''' f'''' a''''")),
            (10, abjad.PitchSegment("b''' b'''' ds'''' g'''' gs'''' g'''' d'''''")),
            ])
         ),
        ("p2", abjad.OrderedDict([
            (1, abjad.PitchSegment("a a' g b d' g' d'")),
            (2, abjad.PitchSegment("a' a'' g' b' d'' g'' d''")),
            (3, abjad.PitchSegment("f'' f''' ds'' g'' g'' ds''' g''")),
            (4, abjad.PitchSegment("a'' a''' g'' b'' d''' g''' d'''")),
            (5, abjad.PitchSegment("d''' d'''' bs'' ds''' g''' bs''' g'''")),
            (6, abjad.PitchSegment("f''' f'''' ds''' g''' g''' ds'''' g'''")),
            (8, abjad.PitchSegment("a''' a'''' g''' b''' d'''' g'''' d''''")),
            (10, abjad.PitchSegment("d'''' d''''' bs''' ds'''' g'''' bs'''' g''''")),
            ])
         ),
        ("p3", abjad.OrderedDict([
            (1, abjad.PitchSegment("d d' ff g a g c")),
            (2, abjad.PitchSegment("d' d'' ff' g' a' g' c'")),
            (3, abjad.PitchSegment("g' g'' bf' d'' f'' d'' g'")),
            (4, abjad.PitchSegment("d'' d''' ff'' g'' a'' g'' c''")),
            (5, abjad.PitchSegment("g'' g''' g'' b'' d''' b'' f''")),
            (6, abjad.PitchSegment("g'' g''' bf'' d''' f''' d''' g''")),
            (8, abjad.PitchSegment("d''' d'''' ff''' g''' a''' g''' c'''")),
            (10, abjad.PitchSegment("g''' g'''' g''' b''' d'''' b''' f'''")),
            ])
         ),
    ])),
])


tremolo_voice = abjad.OrderedDict([
    ("blue", abjad.OrderedDict([
        (2, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("f, c, fs, d, d, a,")),
            ("v2", abjad.PitchSegment("d, f, f, b,, as, g,")),
            ("v3", abjad.PitchSegment("a, d bf, c c d")),
            ])
         ),
        (3, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("f c fs d d a")),
            ("v2", abjad.PitchSegment("d f f b, as g")),
            ("v3", abjad.PitchSegment("a d' bf c' c' d'")),
            ])
         ),
        (4, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("f' c' fs' d' d' a'")),
            ("v2", abjad.PitchSegment("d' f' f' b as' g'")),
            ("v3", abjad.PitchSegment("a' d'' bf' c'' c'' d''")),
            ])
         ),
        (5, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("f'' c'' fs'' d'' d'' a''")),
            ("v2", abjad.PitchSegment("d'' f'' f'' b' as'' g''")),
            ("v3", abjad.PitchSegment("a'' d''' bf'' c''' c''' d'''")),
            ])
         ),
        (6, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("f''' c''' fs''' d''' d''' a'''")),
            ("v2", abjad.PitchSegment("d''' f''' f''' b'' as''' g'''")),
            ("v3", abjad.PitchSegment("a''' d'''' bf''' c'''' c'''' d''''")),
            ])
         ),
    ])),
    ("green", abjad.OrderedDict([
        (2, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("g, f, fs, as, d a,")),
            ("v2", abjad.PitchSegment("a, f, b, d d fs,")),
            ("v3", abjad.PitchSegment("d a, bf, c d f")),
            ])
         ),
        (3, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("g f fs as d' a")),
            ("v2", abjad.PitchSegment("a f b d' d' fs'")),
            ("v3", abjad.PitchSegment("d' a bf c' d' f'")),
            ])
         ),
        (4, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("g' f' fs' as' d'' a'")),
            ("v2", abjad.PitchSegment("a' f' b' d'' d'' fs''")),
            ("v3", abjad.PitchSegment("d'' a' bf' c'' d'' f''")),
            ])
         ),
        (5, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("g'' f'' fs'' as'' d''' a''")),
            ("v2", abjad.PitchSegment("a'' f'' b'' d''' d''' fs'''")),
            ("v3", abjad.PitchSegment("d''' a'' bf'' c''' d''' f'''")),
            ])
         ),
        (6, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("g'' f'' fs'' as'' d''' a''")),
            ("v2", abjad.PitchSegment("a'' f'' b'' d''' d''' fs'''")),
            ("v3", abjad.PitchSegment("d''' a'' bf'' c''' d''' f'''")),
            ])
         ),
    ])),
    ("red", abjad.OrderedDict([
        (1, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("g,, c, f, d, f,, d,,")),
            ("v2", abjad.PitchSegment("f,, a,, g,, d,, g,, as,,")),
            ("v3", abjad.PitchSegment("a,, f,, g,, ff,, f,, d,,")),
            ])
         ),
        (2, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("g, c f d f, d,")),
            ("v2", abjad.PitchSegment("f, a, g, d, g, as,")),
            ("v3", abjad.PitchSegment("a, f, g, ff, f, d,")),
            ])
         ),
        (3, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("g c' f' d' f d")),
            ("v2", abjad.PitchSegment("f a g d g as")),
            ("v3", abjad.PitchSegment("a f g ff f d")),
            ])
         ),
        (4, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("g' c'' f'' d'' f' d'")),
            ("v2", abjad.PitchSegment("f' a' g' d' g' as'")),
            ("v3", abjad.PitchSegment("a' f' g' ff' f' d'")),
            ])
         ),
        (5, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("g'' c''' f''' d''' f'' d''")),
            ("v2", abjad.PitchSegment("f'' a'' g'' d'' g'' as''")),
            ("v3", abjad.PitchSegment("a'' f'' g'' ff'' f'' d''")),
            ])
         ),
    ])),
    ("black", abjad.OrderedDict([
        (2, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("c f as, d a, d")),
            ("v2", abjad.PitchSegment("a, d g, b, fs, g,")),
            ("v3", abjad.PitchSegment("f, a, ff, g, d, f,")),
            ])
         ),
        (3, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("c' f' as d' a d'")),
            ("v2", abjad.PitchSegment("a d' g b fs g")),
            ("v3", abjad.PitchSegment("f a ff g d f")),
            ])
         ),
        (4, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("c'' f'' as' d'' a' d''")),
            ("v2", abjad.PitchSegment("a' d'' g' b' fs' g'")),
            ("v3", abjad.PitchSegment("f' a' ff' g' d' f'")),
            ])
         ),
        (5, abjad.OrderedDict([
            ("v1", abjad.PitchSegment("c''' f''' as'' d''' a'' d'''")),
            ("v2", abjad.PitchSegment("a'' d''' g'' b'' fs'' g''")),
            ("v3", abjad.PitchSegment("f'' a'' ff'' g'' d'' f''")),
            ])
         ),
    ])),
])


