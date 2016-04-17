#! /bin/bash

UPDATE="apt-get update"
USER="debian-transmission"
#PWD="transmission"
VAGRANT_HOME="/home/vagrant"

sudo add-apt-repository ppa:transmissionbt/ppa

$UPDATE

sudo useradd debian-transmission -m -s /bin/bash

sudo adduser $USER root

sudo apt-get install -y transmission-cli transmission-common transmission-daemon

sudo usermod -a -G debian-transmission adamschoonover

sudo service transmission-daemon reload

echo "alias t-start='sudo service transmission-daemon start'" >> $VAGRANT_HOME/.bashrc
echo "alias t-stop='sudo service transmission-daemon stop'" >> $VAGRANT_HOME.bashrc
echo "alias t-reload='sudo service transmission-daemon reload'" >> $VAGRANT_HOME/.bashrc
echo "alias t-list='transmission-remote -n 'transmission:transmission' -l'" >> $VAGRANT_HOME/.bashrc
echo "alias t-basicstats='transmission-remote -n 'transmission:transmission' -st'" >> $VAGRANT_HOME/.bashrc
echo "alias t-fullstats='transmission-remote -n 'transmission:transmission' -si'" >> $VAGRANT_HOME/.bashrc

source $VAGRANT_HOME

sudo cp ./transmission/settings.json /etc/transmission-daemon/settings.json

sudo service transmission-daemon reload
