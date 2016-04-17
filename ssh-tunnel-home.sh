#! /bin/bash

echo "PORT:9000	- UBNT GUI"
echo "PORT:9100 - Verizon Modem"
echo "PORT:9200 - Server VNC"
echo "PORT:9300 - iMAC VNC"
echo "PORT:9400 - Server SAB"
echo "PORT:9500 - Unifi GUI"

sudo ssh adamschoonover@nonstopflights.ddns.net -L 9000:10.0.0.1:80 -L 9100:192.168.1.1:80 -L 9200:10.0.0.50:5900 -L 9300:10.0.0.10:5900 -L 9400:10.0.0.50:8085 -L 9500:10.0.0.50:8443
