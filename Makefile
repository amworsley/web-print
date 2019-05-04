# install / update files

DESTDIR := /opt
CGI_DIR := $(DESTDIR)/usr/lib/cgi-bin
HTML_DIR := $(DESTDIR)/var/www

HTML_FILES:= $(wildcard *.html)
CGI_FILES:= $(wildcard *.py *.sh)

HTML_TARGETS := $(addprefix $(HTML_DIR)/,$(HTML_FILES))
CGI_TARGETS := $(addprefix $(CGI_DIR)/,$(CGI_FILES))

all: $(CGI_FILES) $(HTML_FILES)

install:  $(CGI_TARGETS) $(HTML_TARGETS) $(CGI_DIR) $(HTML_DIR)

$(CGI_DIR):
	mkdir -p $(CGI_DIR)

$(HTML_DIR):
	mkdir -p $(HTML_DIR)


$(HTML_DIR)/%.html: %.html $(HTML_DIR)
	cp $< $@

$(CGI_DIR)/%.py: %.py $(CGI_DIR)
	cp $< $@

$(CGI_DIR)/%.sh: %.sh $(CGI_DIR)
	cp $< $@
