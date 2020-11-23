
SHELL = /bin/bash

.PHONY: materials segments

clean:
	for d in `find . -name __pycache__`; do rm -fr $d; done
	rm -f builds/segments/*.ly
	rm -f builds/segments/*.ily

segments:
	cd segments && ./clean_segments && ./make_segments
