#! /bin/bash

sudo apt-get update

sudo apt-get install -y ssh software-properties-common software-properties-common \
                       nano vim screen

source /synced/bittorent_vpn/torrent_setup.sh
