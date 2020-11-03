import shelve
from copy import deepcopy

db = shelve.open('music_data_shelve')
for key in db:
    result = deepcopy(db[key])
    print(result)
db.close()
