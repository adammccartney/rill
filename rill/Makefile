
SHELL = /bin/bash

.PHONY: materials segments

collect:
	rm -f builds/segments/*.ly;
	cd segments && for segment in segment_*; do \
		sed '/^\\score/,/^\}/!d;/^\\score/d;/^\}/d' $$segment/illustration.ly > ../builds/segments/$${segment/_/-}.ily; \
	done;

segments:
	make segment_A
	make segment_B
	make segment_C
	make segment_D
	make segment_E
	make segment_F
	make segment_G

segment_A:
	python ./segments/A/definition.py

segment_B:
	python ./segments/B/definition.py

segment_C:
	python ./segments/C/definition.py

segment_D:
	python ./segments/D/definition.py

segment_E:
	python ./segments/E/definition.py

segment_F:
	python ./segments/F/definition.py

segment_G:
	python ./segments/G/definition.py


