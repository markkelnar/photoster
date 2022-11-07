FROM python:3

# Perl and exiftool
# borrowed from https://exiftool.org/install.html
ENV EXIFTOOL_VERSION=12.49
RUN cd /tmp \
	&& wget https://exiftool.org/Image-ExifTool-${EXIFTOOL_VERSION}.tar.gz \
	&& tar -zxvf Image-ExifTool-${EXIFTOOL_VERSION}.tar.gz \
	&& cd Image-ExifTool-${EXIFTOOL_VERSION} \
	&& perl Makefile.PL \
	&& make test \
	&& make install \
	&& cd .. \
	&& rm -rf Image-ExifTool-${EXIFTOOL_VERSION}

RUN pip install pyexiftool

WORKDIR /workspace
