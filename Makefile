# install / update files

DESTDIR := /opt
APACHE_DIR := $(DESTDIR)/etc/apache2
CONF_DIR := $(APACHE_DIR)/conf-available
CGI_DIR := $(DESTDIR)/usr/lib/cgi-bin
HTML_DIR := $(DESTDIR)/usr/share/web-misc

HTML_FILES:= $(wildcard *.html)
CGI_FILES:= $(wildcard *.py *.sh)
CONF_FILES:= $(wildcard *.conf)

HTML_TARGETS := $(addprefix $(HTML_DIR)/,$(HTML_FILES))
CGI_TARGETS := $(addprefix $(CGI_DIR)/,$(CGI_FILES))
CONF_TARGETS := $(addprefix $(CONF_DIR)/,$(CONF_FILES))

all: $(CGI_FILES) $(HTML_FILES)

install:  $(CGI_TARGETS) $(HTML_TARGETS) $(CONF_TARGETS)
install:  $(CONF_DIR) $(CGI_DIR) $(HTML_DIR)

$(CGI_DIR):
	mkdir -p $(CGI_DIR)

$(HTML_DIR):
	mkdir -p $(HTML_DIR)

$(HTML_DIR)/%.html: %.html $(HTML_DIR)
	cp $< $@

$(CONF_DIR):
	mkdir -p $(CONF_DIR)

$(CGI_DIR)/%.py: %.py $(CGI_DIR)
	cp $< $@

$(CGI_DIR)/%.sh: %.sh $(CGI_DIR)
	cp $< $@

$(CONF_DIR)/%.conf: %.conf $(CONF_DIR)
	cp $< $@
