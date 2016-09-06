#! /bin/bash

# Script to either convert flac files inside a folder or in a parent folder

echo "Convert this folder or all folders from flac to Apple lossless: "
echo ""
echo "[1] This folder. Must be INSIDE the folder."
echo "[2] All Folders. Must be in the PARENT folder"
echo ""
echo "Script will deleted original FLAC file"

read folder
if [ $folder == 1 ]; then
	for f in ./*.flac; do avconv -i "$f" -c:a alac "${f%.*}.m4a" && rm "$f" && mv *.m4a /mnt/NAS/Music/iTunes//Automatically\ Add\ to\ iTunes.localized/; done
	exit 0
elif [ $folder == 2 ]; then
	shopt -s globstar
	for f in ./**/*.flac; do avconv -i "$f" -c:a alac "${f%.*}.m4a" && rm "$f" && mv *.m4a /mnt/NAS/Music/iTunes//Automatically\ Add\ to\ iTunes.localized/; done
	exit 0
else
	echo "Please enter [1] or [2]."

	fi
fi
