import shelve

from rill.materials.music_init_data.definition import (
    InstrumentMusicData,
    SegmentMusicData,
    )

from rill.materials.instruments.definition import instruments

from pathlib import Path

default_vals = InstrumentMusicData()

default_instrument_data = InstrumentMusicData
default_segment_data = SegmentMusicData

db = shelve.open('music_data_shelve')

db['default_instrument_data'] = default_instrument_data()
db['default_segment_data'] = default_segment_data()

db.close()
