# Alps technical training @ Swiss AI Initiative Annual Meeting 2026 — build entry point.
#
#   make all       build PPTX, HTML and PDF of the full deck
#   make pptx      PowerPoint, with Marpit presenter notes in the speaker-notes pane
#   make html      self-contained HTML; press "p" for the built-in presenter view
#   make pdf       PDF with the speaker notes attached as annotations
#   make public    the same deck with the speaker notes removed
#   make site      build/site/ — exactly what may be published, and nothing else
#   make handout   handout/quickstart.md -> build/quickstart.pdf
#   make M=01 module   build one module on its own (fast rehearsal loop)
#   make serve     live-reloading preview of the full deck
#   make check     slide count per module — the 60-minute budget lives or dies on this
#   make clean     remove build/
#
# Requires Node.js (for npx) and a Chromium that marp-cli can drive.
#
# Two things that are easy to get wrong and are deliberate here:
#   * --html is needed for EVERY target, not just the HTML one: the slides use
#     <div class="cols"> / <div class="card"> layout blocks, stripped otherwise.
#   * --pptx-editable is NOT used: that experimental mode drops presenter notes.

# --no-stdin is not optional: without a terminal, marp-cli waits on stdin forever and
# the build hangs rather than failing. That bites any non-interactive run — a script, a
# background job, CI.
MARP        := npx --yes @marp-team/marp-cli@4.5.0 --no-stdin
BUILD       := build

# The theme is rebuilt with its logos inlined as data URIs. Marp injects the theme
# into the rendered HTML, where the source's relative asset paths would resolve
# against the output directory and silently drop the logos.
THEME_SRC   := slides/theme/cscs.css
THEME       := $(BUILD)/theme/cscs.css

MARP_FLAGS  := --allow-local-files --html --theme $(THEME)

SLIDES      := $(sort $(wildcard slides/[0-9]*.md))
DECK        := $(BUILD)/deck.md

# The public deck is a second assembly of the same sources with the speaker notes
# stripped, not a post-processing of the first: notes reach the HTML, the PDF annotations
# and the PowerPoint notes pane by three different routes, and removing them from three
# outputs is three chances to miss one.
PUBLIC_DECK := $(BUILD)/deck-public.md
PUBLIC      := $(BUILD)/public
SITE        := $(BUILD)/site

.PHONY: all pptx html pdf public site handout module serve clean check runsheet footers

all: pptx html pdf

$(THEME): $(THEME_SRC) $(wildcard assets/logos/*) tools/inline-assets.py
	python3 tools/inline-assets.py $(THEME_SRC) -o $@

$(DECK): $(SLIDES) tools/assemble.py
	@mkdir -p $(BUILD)
	python3 tools/assemble.py $(SLIDES) -o $@

$(PUBLIC_DECK): $(SLIDES) tools/assemble.py
	@mkdir -p $(BUILD)
	python3 tools/assemble.py --no-notes $(SLIDES) -o $@

pptx: $(BUILD)/deck.pptx
html: $(BUILD)/deck.html
pdf:  $(BUILD)/deck.pdf

# PowerPoint renders speaker notes at 12pt, which is unreadable at a glance on stage.
# Nothing upstream can change it, so the size is set after the file exists. The step is
# optional: without python-pptx it prints a hint and the build carries on.
$(BUILD)/deck.pptx: $(DECK) $(THEME) tools/enlarge-notes.py
	$(MARP) $(MARP_FLAGS) -o $@ -- $(DECK)
	@python3 tools/enlarge-notes.py $@

$(BUILD)/deck.html: $(DECK) $(THEME) tools/enlarge-notes.py
	$(MARP) $(MARP_FLAGS) -o $@ -- $(DECK)
	@python3 tools/enlarge-notes.py $@

$(BUILD)/deck.pdf: $(DECK) $(THEME)
	$(MARP) $(MARP_FLAGS) --pdf --pdf-notes -o $@ -- $(DECK)

# The deck as it goes out: no speaker notes anywhere, and no --pdf-notes.
public: $(PUBLIC)/deck.html $(PUBLIC)/deck.pdf $(PUBLIC)/deck.pptx

$(PUBLIC)/deck.html: $(PUBLIC_DECK) $(THEME)
	@mkdir -p $(PUBLIC)
	$(MARP) $(MARP_FLAGS) -o $@ -- $(PUBLIC_DECK)

$(PUBLIC)/deck.pptx: $(PUBLIC_DECK) $(THEME)
	@mkdir -p $(PUBLIC)
	$(MARP) $(MARP_FLAGS) -o $@ -- $(PUBLIC_DECK)

$(PUBLIC)/deck.pdf: $(PUBLIC_DECK) $(THEME)
	@mkdir -p $(PUBLIC)
	$(MARP) $(MARP_FLAGS) --pdf -o $@ -- $(PUBLIC_DECK)

# What gets published, listed rather than swept up. build/ also holds the assembled
# source, the run sheet and the deck with notes; publishing the directory wholesale is
# how all three ended up on a public URL. Adding a file here is a decision someone makes
# on purpose.
site: public handout
	@rm -rf $(SITE) && mkdir -p $(SITE)
	cp web/index.html $(SITE)/index.html
	cp $(PUBLIC)/deck.html $(PUBLIC)/deck.pdf $(PUBLIC)/deck.pptx $(SITE)/
	cp $(BUILD)/quickstart.pdf $(SITE)/
	@python3 tools/no-notes.py $(SITE)

# Build a single module: make M=01 module
module: $(THEME)
	@test -n "$(M)" || { echo "usage: make M=01 module"; exit 1; }
	$(eval SRC := $(wildcard slides/$(M)-*.md))
	@test -n "$(SRC)" || { echo "no slides/$(M)-*.md found"; exit 1; }
	$(MARP) $(MARP_FLAGS) -o $(BUILD)/module-$(M).html -- $(SRC)
	$(MARP) $(MARP_FLAGS) -o $(BUILD)/module-$(M).pptx -- $(SRC)

# The handout is A4 portrait, not a slide, so it uses its own theme. Marp takes the
# page size from that theme's section width/height.
handout: $(BUILD)/quickstart.pdf

$(BUILD)/quickstart.pdf: handout/quickstart.md handout/handout.css
	@mkdir -p $(BUILD)
	$(MARP) --allow-local-files --html --theme handout/handout.css --pdf -o $@ -- $<

serve: $(DECK) $(THEME)
	$(MARP) $(MARP_FLAGS) --server $(BUILD)

check:
	@python3 tools/slide-count.py $(SLIDES)
	@python3 tools/speaking-time.py $(SLIDES)
	@python3 tools/sync-footers.py --check $(SLIDES)
# A relative image path in the published HTML resolves against build/, which is the
# whole site on GitHub Pages — the file sits outside it and the slide shows alt text.
# It looks correct locally, so only a check catches it.
	@test ! -f $(BUILD)/deck.html || ! grep -q 'src="\.\./' $(BUILD)/deck.html || \
	  { echo 'check: deck.html links an image outside build/ — it will 404 on Pages'; exit 1; }
# Speaker notes must not reach anything published. Checked on the built site, not on the
# sources, because that is where the mistake would actually be.
	@test ! -d $(SITE) || python3 tools/no-notes.py $(SITE)

# Each slide's footer carries the docs page it came from, derived from its DOCS: line.
# Edit the DOCS line in the speaker notes, then run this — never edit a footer by hand.
footers:
	@python3 tools/sync-footers.py $(SLIDES)

# Who speaks when, and what each module drops if the clock slips. Budgets are read from
# the module dividers, so this cannot drift from what is on screen.
runsheet: $(BUILD)/run-sheet.pdf

$(BUILD)/run-sheet.md: $(SLIDES) tools/run-sheet.py
	@mkdir -p $(BUILD)
	python3 tools/run-sheet.py $(SLIDES) -o $@ --start 13:30

$(BUILD)/run-sheet.pdf: $(BUILD)/run-sheet.md handout/handout.css
	$(MARP) --allow-local-files --html --theme handout/handout.css --pdf -o $@ -- $<

clean:
	rm -rf $(BUILD)
