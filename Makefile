.PHONY: all clean clean_deb clean_composer clean_all build require_box require_composer require_fpm deb

# The .phar file we build:
PROJECT := photoster
DOCKER_IMMAGE := photoster

build:
	docker build ${DOCKER_IMAGE} --file "Dockerfile" .

run:
	docker run -it --rm --name ${DOCKER_NAME} ./run.py

#	docker run --rm -v ${PWD}/:/workspace/ -v ~/pics.in:/p.in -v ~/pics.out:/p.out photoster ./run.py
# Run with 
#  docker run -v ${PWD}/:/workspace/ -v ~/pics/in:/pics.in -v ~/pics/out:/pics.out photoster ./run.py
# The -v are volumes (directories) that are mounted within the docker image as a volume
# /pics.in and /pics.out are paths that the run.py app are looking for.  Those are how the names are 
# mounted within the Docker image.  Use those.
# The other names are directory names external to the Docker image.

# For output to the Seagate mounted drive
# docker run -v ${PWD}/:/workspace/ -v ~/pics/in:/pics.in -v /Volumes/Seagate\ Backup\ Plus\ Drive/pics/:/pics.out photoster ./run.py
