import shelve

from pathlib import Path

up_two_dirs = Path.cwd().parents[1]
db_path = up_two_dirs / 'materials' / 'music_data' / 'music_data_shelve'

print(db_path)

db = shelve.open(str(db_path))

for key in db:
    print(key)

db.close()
