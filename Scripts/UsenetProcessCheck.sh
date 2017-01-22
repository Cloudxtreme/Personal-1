#!/bin/bash

couch=$(ps -ef | grep -i CouchPotato.py | grep -v grep | wc -l)
sabnzbd=$(ps -ef | grep -i sabnzbd | grep -v grep | wc -l)
nzbdrone=$(ps -ef | grep -i nzbdrone | grep -v grep | wc -l)

if [ $couch != 1 ]; then
	sudo service couchpotato start
	echo "Starting Couchpotato"
else
	echo "Couchpotato [OK]"

fi

if [ $sabnzbd != 1 ]; then
	sudo service sabnzbdplus start
	echo "Starting Couchpotato"
else
	echo "Sabnzbd [OK]"

fi

if [ $nzbdrone != 1 ]; then
	sudo service nzbdrone start
	echo "Starting Couchpotato"
else
	echo "Sonar [OK]"

fi
