# install / update files

CGI_DIR := /usr/lib/cgi-bin
HTML_DIR := /var/www

HTML_FILES:= $(wildcard *.html)
CGI_FILES:= $(wildcard *.py *.sh)

HTML_TARGETS := $(addprefix $(HTML_DIR)/,$(HTML_FILES))
CGI_TARGETS := $(addprefix $(CGI_DIR)/,$(CGI_FILES))

install:  $(CGI_TARGETS) $(HTML_TARGETS)


$(HTML_DIR)/%.html: %.html
	cp $< $@

$(CGI_DIR)/%.py: %.py
	cp $< $@

$(CGI_DIR)/%.sh: %.sh
	cp $< $@
