CC = gcc
AR = ar cr
RANLIB = ranlib
CPPFLAGS = -I
CFLAGS = -Wall -O2 
ARFLAGS = cru

LIB_SRC = jcapimin.c jcapistd.c jccoefct.c jccolor.c jcdctmgr.c jchuff.c jcinit.c jcmainct.c jcmarker.c jcmaster.c jcomapi.c jcparam.c jcphuff.c jcprepct.c jcsample.c jctrans.c jdapimin.c jdapistd.c jdatadst.c jdatasrc.c jdcoefct.c jdcolor.c jddctmgr.c jdhuff.c jdinput.c jdmainct.c jdmarker.c jdmaster.c jdmerge.c jdphuff.c jdpostct.c jdsample.c jdtrans.c jerror.c jfdctflt.c jfdctfst.c jfdctint.c jidctflt.c jidctfst.c jidctint.c jidctred.c jquant1.c jquant2.c jutils.c jmemmgr.c jmemnobs.c

CJPEG_SRC = cjpeg.c rdppm.c rdgif.c rdtarga.c rdrle.c rdbmp.c rdswitch.c cdjpeg.c
DJPEG_SRC = djpeg.c wrppm.c wrgif.c wrtarga.c wrrle.c wrbmp.c rdcolmap.c cdjpeg.c
JPEGTRAN_SRC = jpegtran.c rdswitch.c cdjpeg.c transupp.c

OBJ = $(LIB_SRC:.c=.o)
OBJ_CJPEG = $(CJPEG:.c=.o)
OBJ_DJPEG = $(DJPEG:.c=.o)
OBJ_JPEGTRAN = $(JPEGTRAN_SRC:.c=.o)

all:libjpeg.a cjpeg #djpeg jpegtran

depend:$(LIB_SRC) #ajouter le cppflags?
	$(CC) -MM $(LIB_SRC) $(CJPEG_SRC) $(DJPEG_SRC) $(JPEGTRAN_SRC) > .depend

-include .depend

jconfig.h:ckconfig.c
	gcc $< -o ckconfig
	./ckconfig

%.o:%.c
	$(CC) -c $< $(CPPFLAGS) $(CFLAGS) -o $@

libjpeg.a:$(OBJ) jconfig.h
	$(AR) $@ $<
	$(RANLIB) $@


cjpeg:libjpeg.a $(OBJ_SRC)
	$(CC) $< $(CFLAGS) $(OBJ_SRC) -o $@

djpeg:$(DJPEG_SRC) depend
	$(CC) $(CFLAGS) -o $@ $<

jpegtran:$(JPEGTRAN_SRC) depend
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f $(OBJ) jconfig.h ckconfig libjpeg.a $(OBJ_CJPEG) $(OBJ_DJPEG) $(OBJ_JPEGTRAN)

.PHONY: clean depend all
