#!/bin/bash

# Process Apple iphotos to local external drive
docker run -v ${PWD}/:/workspace/ -v /Users/mark.kelnar/Pictures/Photos\ Library.photoslibrary/Masters/:/pics.in -v /Volumes/Seagate\ Backup\ Plus\ Drive/pics/:/pics.out photoster ./run.py

# Sync drive to s3 (cloud, offsite)
aws s3 sync /Volumes/Seagate\ Backup\ Plus\ Drive/pics/ s3://storage.kelnar/pics/

