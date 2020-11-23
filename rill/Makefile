
SHELL = /bin/bash

.PHONY: materials segments

segments:
	cd segments && ./clean_segments && ./make_segments

collect:
	mkdir -p builds/segments
	rm -f builds/segments/*.ly;
	cd segments && for segment in segment_*; do \
	sed '/^\\score/,/^\}/!d;/^\\score/d;/^\}/d' $$segment/illustration.ly > ../builds/segments/$${segment/_/_}.ily; \
	done;

clean:
	for d in `find . -name __pycache__`; do rm -fr $d; done
	rm -f builds/segments/*ly
	rm -f builds/segments/*ily
