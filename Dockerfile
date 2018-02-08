FROM python:3

# Perl and exiftool
# borrowed from https://github.com/Miljar/exiftool-docker
ENV EXIFTOOL_VERSION=10.20
RUN cd /tmp \
	&& wget http://www.sno.phy.queensu.ca/~phil/exiftool/Image-ExifTool-${EXIFTOOL_VERSION}.tar.gz \
	&& tar -zxvf Image-ExifTool-${EXIFTOOL_VERSION}.tar.gz \
	&& cd Image-ExifTool-${EXIFTOOL_VERSION} \
	&& perl Makefile.PL \
	&& make test \
	&& make install \
	&& cd .. \
	&& rm -rf Image-ExifTool-${EXIFTOOL_VERSION}


RUN pip install pillow
RUN pip install pyexifinfo

WORKDIR /workspace
