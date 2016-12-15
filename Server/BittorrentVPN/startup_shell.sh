#! /bin/bash

# version .1 
# first scritpt to be run after the first vagrant up

set -o nounset
set -o errexit

if [ "$(id -u)" != "0" ]; then
  echo "Sorry, you are not root."
  exit 1
fi

apt-get update

apt-get install -y \
	ssh 				\
	software-properties-common 	\
	software-properties-common 	\
        nano 				\
	vim 				\
	screen

source /synced/bittorent_vpn/torrent_setup.sh
