#! /bin/bash

RED='\033[0;31m'
LG='\033[1;32m'
NC='\033[0m' # No Color

echo -e "

######### SSH TUNNEL HOME ##########

"

printf "${LG}PORT:9100${NC} - Verizon Modem\n"
printf "${LG}PORT:9200${NC} - Server VNC\n"
printf "${LG}PORT:9300${NC} - iMAC VNC\n"



echo ""

ssh adamschoonover@nonstopflights.ddns.net -p 9234 -L \
9100:192.168.1.1:80 -L \
9200:10.0.0.50:5900 -L \
9300:10.0.0.10:5900
