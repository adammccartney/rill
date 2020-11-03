import shelve

from pathlib import Path

up_two_dirs = Path.cwd().parents[1]
db_path = up_two_dirs / 'materials' / 'music_data' / 'music_data_shelve'

print(db_path)

db = shelve.open(str(db_path), 'r')

for key in db:
    print(key, '=>\n', db[key])

#retrieved = db['default_instrument_data']


#default_music_initializer = db['default_music_initializer']
#print(default_music_initializer)

#segment_data_dict = segment_data.instrument_music_data

db.close()
