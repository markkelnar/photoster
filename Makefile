.PHONY: all clean clean_deb clean_composer clean_all build require_box require_composer require_fpm deb

# The .phar file we build:
PROJECT := photoster
DOCKER_IMAGE := photoster

build:
	docker build -t ${DOCKER_IMAGE} --file "Dockerfile" .

shell:
	docker run -it -v ${PWD}/:/workspace/ ${DOCKER_IMAGE} /bin/bash

run:
	docker run -v ${PWD}/:/workspace/ -v /Users/mark.kelnar/Pictures/Photos\ Library.photoslibrary/Masters/:/pics.in -v /Volumes/Seagate\ Backup\ Plus\ Drive/pics/:/pics.out photoster ./run.py

