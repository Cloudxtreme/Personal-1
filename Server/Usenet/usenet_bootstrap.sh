#usenet start script

sudo apt-get update git
sudo apt-get install git-core

##sab
sudo add-apt-repository ppa:jcfp/ppa

echo "deb http://ppa.launchpad.net/jcfp/ppa/ubuntu $(lsb_release -c -s) main" | sudo tee -a /etc/apt/sources.list && sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:11371 --recv-keys 0x98703123E0F52B2BE16D586EF13930B14BB9F05F

sudo apt-get update

sudo apt-get install sabnzbdplus

sudo service sabnzbdplus start

#couchpotato

mkdir ~/Git
cd ~/Git
git clone https://github.com/CouchPotato/CouchPotatoServer.git
sudo cp CouchPotatoServer/init/ubuntu /etc/init.d/couchpotato
sudo cp CouchPotatoServer/init/ubuntu.default /etc/default/couchpotato
sudo chmod +x /etc/init.d/couchpotato
sudo update-rc.d couchpotato defaults

#Sonarr
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC
echo "deb http://apt.sonarr.tv/ master main" | sudo tee /etc/apt/sources.list.d/sonarr.list
sudo apt-get update
sudo apt-get install nzbdrone
mono --debug /opt/NzbDrone/NzbDrone.exe
