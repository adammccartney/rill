
SHELL = /bin/bash

.PHONY: materials segments

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

segments: segment_A segment_B segment_C segment_D segment_E segment_F segment_G

segment_A:
	python ./segments/$@/definition.py

segment_B:
	python ./segments/$@/definition.py

segment_C:
	python ./segments/$@/definition.py

segment_D:
	python ./segments/$@/definition.py

segment_E:
	python ./segments/$@/definition.py

segment_F:
	python ./segments/$@/definition.py

segment_G:
	python ./segments/$@/definition.py
