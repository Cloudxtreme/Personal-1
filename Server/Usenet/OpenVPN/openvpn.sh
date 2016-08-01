sudo openvpn --config cstorm_USeast.ovpn --daemon 

sleep 3

ps -ef | grep vpn
