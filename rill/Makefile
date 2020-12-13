
SHELL := /bin/bash
PYTHON := python3

SEGMENTS := A B C D E F G H I J K L

.PHONY: segments clean

all: segments

# TODO: the output file of genDef_v1.py should be given explicitly as an argument or stdout output piped to it
# TODO: first generating the definition.py files and then calling them is awkward. It should be easier to use one generic script with arguments

materials/music_data/music_data_shelve.db: materials/music_data/definition.py
	cd $(dir $<) && $(PYTHON) $(notdir $<)

segments/segment_%/illustration.ly segments/segment_%/illustration.pdf builds/segments/%.ly builds/segments/%.ily: segments/segment_%/genDef_v1.py segments/segment_%/music_data.py materials/music_data/music_data_shelve.db
	-mkdir -p builds/segments
	cd $(dir $<) && \
	s=$(subst /,,$(subst segments/segment_,,$(dir $<))) && \
	ix=`$(PYTHON) -c "import sys; print(sys.argv[2:].index(sys.argv[1]))" $${s} $(SEGMENTS)` && \
	$(PYTHON) ./genDef_v1.py $${s} $$((ix+1))

builds/segments/segment_%.ily: segments/segment_%/illustration.ly
	-mkdir -p $(dir $<)
	sed '/^\\score/,/^\}/!d;/^\\score/d;/^\}/d' $< > $@


segments: $(foreach p, $(SEGMENTS), builds/segments/segment_$(p).ily)


clean:
	for d in `find . -name __pycache__`; do rm -fr $$d; done
	rm -f builds/segments/*.ly
	rm -f builds/segments/*.ily
	rm -f segments/segment_*/illustration.pdf
	rm -f segments/segment_*/illustration.ly
	rm -f segments/segment_*/definition.py
	rm -f materials/music_data/*.db
