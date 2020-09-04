#!/bin/bash
# Run this after files have been processed from "Photos" to the watched folder and processed by the single.sh docker script.
# This file will sync files to the external attached drive and aws s3

echo `date`

OUT_DIR=/Users/mark.kelnar/Desktop/out/
REMOVEABLE_STORAGE_DIR=/Volumes/Seagate\ Backup\ Plus\ Drive/pics

# sync that output folder to the external drive
rsync -av "$OUT_DIR" "$REMOVEABLE_STORAGE_DIR"

# Sync processed photo to s3 (cloud, offsite)
#aws s3 sync "$OUTDIR" s3://storage.kelnar/pics/
