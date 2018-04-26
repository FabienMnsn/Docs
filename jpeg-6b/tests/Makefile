OUTFILE = testout


all:check

img:
	../src/djpeg -dct int -ppm -outfile $(OUTFILE).ppm testorig.jpg	
	../src/djpeg -dct int -bmp -colors 256 -outfile $(OUTFILE).bmp testorig.jpg
	../src/cjpeg -dct int -outfile $(OUTFILE).jpg testimg.ppm
	../src/djpeg -dct int -ppm -outfile $(OUTFILE)p.ppm testprog.jpg
	../src/cjpeg -dct int -progressive -opt -outfile $(OUTFILE)p.jpg testimg.ppm
	../src/jpegtran -outfile $(OUTFILE)t.jpg testprog.jpg

check:img
	cmp testimg.ppm $(OUTFILE).ppm	
	cmp testimg.bmp $(OUTFILE).bmp
	cmp testimg.jpg $(OUTFILE).jpg
	cmp testimg.ppm $(OUTFILE)p.ppm
	cmp testimgp.jpg $(OUTFILE)p.jpg
	cmp testorig.jpg $(OUTFILE)t.jpg

clean:
	rm -f $(OUTFILE)*

.PHONY:	all check clean
