#! /bin/bash

if [ "$(id -u)" != "0" ]; then
  echo "Sorry, you are not root."
  exit 1
fi

#inital update
apt-get update

# ADD REPOS SECTION
echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" >> /etc/apt/sources.list

#install basic programs
echo "--> Installing basic "

listofapps="git apache2 nautilus nautilus-dropbox virtualbox \
ssh samba samba-common snmp snmpd snmp-mibs-downloader \
strace tcpdump ruby Python perl dump docker diffutils \
coreutils nano x11vnc vim wget unifi tree terminator ppa-purge \
software-properties-common"

sudo apt-get install --force-yes $listofapps -y

# mysql automatic installation
echo "--> Installing mysql. User = root. Password = ATT&bangbang"\r

debconf-set-selections <<< 'mysql-server mysql-server/root_password password CuIeyy7j!!'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password CuIeyy7j!!'
apt-get update
apt-get install -y mysql-server
