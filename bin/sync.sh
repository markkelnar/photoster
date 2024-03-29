#!/bin/bash
# Run this after files have been processed from "Photos" to the watched folder and processed by the single.sh docker script.
# This file will sync files to the external attached drive and aws s3

echo `date`

FROM_DIR=/Users/mark.kelnar/Desktop/photoster-process/processed-photos/

# sync that output folder to the external drive
rsync -av "$FROM_DIR" "/Volumes/Seagate Backup Plus Drive/pics/"

# Sync processed photo to s3 (cloud, offsite)
aws s3 sync "$FROM_DIR" s3://storage.kelnar/pics/
