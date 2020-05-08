import abjad


persist = abjad.OrderedDict(
    [
        (
            'alive_during_segment',
            [
                'Score',
                'Global_Context',
                'Global_Skips',
                'Music_Context',
                'Piano_Staff',
                'Viola_I',
                'Global_Rests',
                'Viola_I_Markup_Voice',
                'Viola_I_Markup_Rest_Voice',
                'Viola_I_Music_Voice',
                'Viola_I_Rest_Voice',
                'Viola_I_Dynamics_Voice',
                'Viola_I_Dynamics_Rest_Voice',
                'Viola_II',
                'Viola_II_Markup_Voice',
                'Viola_II_Markup_Rest_Voice',
                'Viola_II_Music_Voice',
                'Viola_II_Rest_Voice',
                'Viola_II_Dynamics_Voice',
                'Viola_II_Dynamics_Rest_Voice',
                ],
            ),
        (
            'persistent_indicators',
            abjad.OrderedDict(
                [
                    (
                        'Score',
                        [
                            abjad.Momento(
                                context='Global_Skips',
                                manifest='metronome_marks',
                                value='36',
                                ),
                            abjad.Momento(
                                context='Global_Skips',
                                prototype='abjad.TimeSignature',
                                value='1/4',
                                ),
                            ],
                        ),
                    (
                        'Viola_I',
                        [
                            abjad.Momento(
                                context='Viola_I_Markup_Voice',
                                prototype='abjad.Clef',
                                value='alto',
                                ),
                            abjad.Momento(
                                context='Viola_I_Music_Voice',
                                edition=abjad.Tag('-PARTS'),
                                manifest='margin_markups',
                                value='Va. I',
                                ),
                            abjad.Momento(
                                context='Viola_I_Music_Voice',
                                manifest='instruments',
                                value='ViolaI',
                                ),
                            ],
                        ),
                    (
                        'Viola_II',
                        [
                            abjad.Momento(
                                context='Viola_II_Markup_Voice',
                                prototype='abjad.Clef',
                                value='alto',
                                ),
                            abjad.Momento(
                                context='Viola_II_Music_Voice',
                                edition=abjad.Tag('-PARTS'),
                                manifest='margin_markups',
                                value='Va. II',
                                ),
                            abjad.Momento(
                                context='Viola_II_Music_Voice',
                                manifest='instruments',
                                value='ViolaII',
                                ),
                            ],
                        ),
                    (
                        'Viola_II_Music_Voice',
                        [
                            abjad.Momento(
                                context='Viola_II_Music_Voice',
                                prototype='abjad.Dynamic',
                                value='mf',
                                ),
                            ],
                        ),
                    (
                        'Viola_I_Music_Voice',
                        [
                            abjad.Momento(
                                context='Viola_I_Music_Voice',
                                prototype='abjad.Dynamic',
                                value='niente',
                                ),
                            ],
                        ),
                    ]
                ),
            ),
        ]
    )
