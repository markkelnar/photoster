#!/bin/bash

WORKING_DIR=$PWD/cache
PHOTO_LIBRARY=$HOME/Pictures/Photos\ Library.photoslibrary/Masters
REMOVEABLE_STORAGE_DIR=/Volumes/Seagate\ Backup\ Plus\ Drive/pics

# Sync files out of the Photos master directory
rsync -av "$PHOTO_LIBRARY/" "$WORKING_DIR/"

# Process Apple iphotos to local external drive
docker run -v ${PWD}/:/workspace/ -v "$WORKING_DIR":/pics.in -v "$REMOVEABLE_STORAGE_DIR":/pics.out photoster ./run.py

# Sync drive to s3 (cloud, offsite)
aws s3 sync "$REMOVEABLE_STORAGE_DIR" s3://storage.kelnar/pics/

