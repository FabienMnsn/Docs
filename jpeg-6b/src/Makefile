CC = gcc
AR = ar
RANLIB = ranlib
CPPFLAGS = -I
CFLAGS = -Wall -O2 
ARFLAGS = cru
DESTDIR = /usr/local

LIB_SRC = jcapimin.c jcapistd.c jccoefct.c jccolor.c jcdctmgr.c jchuff.c jcinit.c jcmainct.c jcmarker.c jcmaster.c jcomapi.c jcparam.c jcphuff.c jcprepct.c jcsample.c jctrans.c jdapimin.c jdapistd.c jdatadst.c jdatasrc.c jdcoefct.c jdcolor.c jddctmgr.c jdhuff.c jdinput.c jdmainct.c jdmarker.c jdmaster.c jdmerge.c jdphuff.c jdpostct.c jdsample.c jdtrans.c jerror.c jfdctflt.c jfdctfst.c jfdctint.c jidctflt.c jidctfst.c jidctint.c jidctred.c jquant1.c jquant2.c jutils.c jmemmgr.c jmemnobs.c

OBJ = $(LIB_SRC:.c=.o)

CJPEG = cjpeg.c
DJPEG = djpeg.
JPEGTRAN = jpegtran.c
CJPEG_SRC = cjpeg.c rdppm.c rdgif.c rdtarga.c rdrle.c rdbmp.c rdswitch.c cdjpeg.c
DJPEG_SRC = djpeg.c wrppm.c wrgif.c wrtarga.c wrrle.c wrbmp.c rdcolmap.c cdjpeg.c
JPEGTRAN_SRC = jpegtran.c rdswitch.c cdjpeg.c transupp.c
UTILITAIRES = cjpeg djpeg jpegtran rdjpgcom wrjpgcom

HEADERS = jconfig.h jpeglib.h jerror.h jpegint.h

all:libjpeg.a $(UTILITAIRES)


jconfig.h:ckconfig.c
	$(CC) $(CFLAGS) $< -o ckconfig
	./ckconfig


%.o:%.c
	$(CC) -c $< $(CPPFLAGS) $(CFLAGS) -o $@


libjpeg.a:$(OBJ) jconfig.h
	$(AR) $(ARFLAGS) $@ $(OBJ)
	$(RANLIB) $@


cjpeg:$(CJPEG_SRC) libjpeg.a
	$(CC) $(CFLAGS) -o $@ $^

djpeg:$(DJPEG_SRC) libjpeg.a
	$(CC) $(CFLAGS) -o $@ $^

jpegtran:$(JPEGTRAN_SRC) libjpeg.a
	$(CC) $(CFLAGS) -o $@ $^

rdjpgcom: rdjpgcom.c
	$(CC) $(CFLAGS) -o $@ $<

wrjpgcom:wrjpgcom.c
	$(CC) $(CFLAGS) -o $@ $<


depend:$(LIB_SRC) $(CJPEG) $(DJPEG) $(JPEGTRAN)
	$(CC) -MM $^ > .depend

-include .depend

install:
	mkdir -p $(DESTDIR)/lib
	cp libjpeg.a $(DESTDIR)/lib
	mkdir -p $(DESTDIR)/include
	cp $(HEADERS) $(DESTDIR)/include
	mkdir -p $(DESTDIR)/bin
	cp $(UTILITAIRES) $(DESTDIR)/bin

clean:
	rm -f $(OBJ) jconfig.h ckconfig libjpeg.a $(UTILITAIRES) .depend


.PHONY: clean depend all
