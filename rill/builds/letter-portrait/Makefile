MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
SCORE_NAME := $(lastword $(subst /, ,$(firstword $(subst build, ,$(MAKEFILE_PATH)))))
BUILD_TARGET := $(notdir $(patsubst %/,%,$(dir $(MAKEFILE_PATH))))
BUILD_PREFIX := $(SCORE_NAME)-$(BUILD_TARGET)

PARTS := flute1 flute2 flute3 Bbclarinet1 vibraphone violin1 violin2 violin3 violin4 violin5 violin6 violin7 violin8 viola

PARTS_PDF := $(foreach p, $(PARTS), parts-$(p).pdf)

.PHONY: parts segments clean dist help

# we only need the score.pdf... it is dependent on everything else
all: score.pdf

parts: $(PARTS_PDF)

segments:
	$(MAKE) -C ../..

music.ly: ../segments.ily segments
	touch $@

parts.ly: ../parts.ily segments
	touch $@

# specific pdf generation

# all parts are generated from one parts.ly
$(PARTS_PDF): parts.ly
	lilypond $<
	
# all pdfs are needed for score.pdf
score.pdf: score.tex front-cover.pdf preface.pdf music.pdf $(PARTS_PDF) back-cover.pdf
	xelatex $<

# generic pdf generation

%.pdf: %.tex
	xelatex $<

%.pdf: %.ly
	lilypond $<

clean:
	rm -f *.pdf
	rm -f *.log
	rm -f *.aux

dist: score.pdf
	mkdir -p ../../distribution/$(BUILD_PREFIX)
	cp score.pdf ../../distribution/$(BUILD_PREFIX)/$(BUILD_PREFIX)-score.pdf
	for part in parts-*.pdf; do \
		mv $$part ../../distribution/$(BUILD_PREFIX)/$(BUILD_PREFIX)-$$part; \
	done;
	cd ../../distribution && zip -r $(BUILD_PREFIX).zip $(BUILD_PREFIX) 

help:
	@echo ""
	@echo "make (all)           - compile score and parts PDFs"
	@echo "                       copy score and parts PDFs to distribution/"
	@echo "                       create ZIP archive of score and parts"
	@echo "                       clean extraneous LaTeX files"
	@echo "make front-cover.pdf - compile front-cover PDF"
	@echo "make preface.pdf     - compile preface PDF"
	@echo "make music.pdf       - compile music PDF"
	@echo "make back-cover.pdf  - compile back-cover PDF"
	@echo "make score.pdf       - compile score PDF"
	@echo "make parts           - compile parts PDFs"
	@echo "make dist            - copy score and parts PDFs to distribution/"
	@echo "                       create ZIP archive of score and parts"
	@echo "make clean           - clean extraneous LaTeX files"
	@echo "make help            - print this message"
	@echo ""
