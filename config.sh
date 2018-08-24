#!/bin/bash
service mysql start 
mysql < ./schema.sql 
service mysql status 

apt-get install -y iproute iproute-doc
myip=$(/sbin/ip route|awk '/default/ { print $3 }')
echo "ip:"${myip}
sed -i "s|<externalAddress>.*<\/externalAddress>|<externalAddress>${myip}<\/externalAddress>|g" ./res/server/kbengine.xml 

sh ./start_server.sh
sh -c "$*" 

tail -f /dev/null

