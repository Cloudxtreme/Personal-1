#!/bin/bash

# This script is to move the recently downloaded file to /mnt/NAS/Downloads

# change owner from root
sudo chown -R adamschoonover /opt/Downloads/*
 
# move to Downloads

sudo mv -r $TR_TORRENT_NAME /mnt/NAS/Downloads/
