.PHONY: all clean clean_deb clean_composer clean_all build require_box require_composer require_fpm deb

# The .phar file we build:
PROJECT := photoster
DOCKER_IMMAGE := photoster

docker_build:
	docker build -t ${DOCKER_IMAGE} .

docker_clean:
	docker clean

docker_test_unit:
	docker run --rm -v ${PWD}/:/workspace/ ${DOCKER_IMAGE} make test

run:
	docker run -it --rm --name ${DOCKER_NAME} run.py
