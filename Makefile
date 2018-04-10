.PHONY: all clean clean_deb clean_composer clean_all build require_box require_composer require_fpm deb

# The .phar file we build:
PROJECT := photoster
DOCKER_IMMAGE := photoster

build:
	docker build ${DOCKER_IMAGE} --file "Dockerfile" .

run:
	docker run -it --rm --name ${DOCKER_NAME} ./run.py

