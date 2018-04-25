DESTDIR = /usr/local

all:
	cd src; $(MAKE) $@
	cd tests; $(MAKE) $@

install:all
	cd src; $(MAKE) $@ DESDIR=$(DESTDIR)
	
	mkdir -p $(DESTDIR)/share/man/man1
	cp man/*.1 $(DESTDIR)/share/man/man1
	
	mkdir -p $(DESTDIR)/share/doc/jpeg-6b
	cp doc/*.doc $(DESTDIR)/share/doc/jpeg-6b
	gzip $(DESTDIR)/share/doc/jpeg-6b/*.doc
	
	mkdir -p $(DESTDIR)/share/jpeg-6b
	cp README change.log $(DESTDIR)/share/jpeg-6b

clean:
	cd src; $(MAKE) $@
	cd tests; $(MAKE) $@


.PHONY: all clean install
