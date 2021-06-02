#!/bin/bash
# ./single.sh /path/to/file.jpg

echo `date`

FILENAME=${1?Need a value}
BASENAME=$(basename "$FILENAME")
DIRNAME=$(dirname "$FILENAME")
OUT_DIR=/Users/mark.kelnar/Desktop/photoster-process/processed-photos/
REMOVEABLE_STORAGE_DIR=/Volumes/Seagate\ Backup\ Plus\ Drive/pics

# Process the one photo to a folder
/usr/local/bin/docker run -v ${PWD}/:/workspace/ -v "$DIRNAME":/pics.in/ -v "$OUT_DIR":/pics.out photoster ./run.py "/pics.in/$BASENAME"
