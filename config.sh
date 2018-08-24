#!/bin/bash
service mysql start 
mysql < ./schema.sql 
service mysql status 

myip=$(/sbin/ip route|awk '/default/ { print $3 }')
if $LOCALHOST == true; then 
  myip=127.0.0.1
fi

echo "ip:"${myip}
sed -i "s|<externalAddress>.*<\/externalAddress>|<externalAddress>${myip}<\/externalAddress>|g" ./res/server/kbengine.xml 

sh ./start_server.sh
sh -c "$*" 

tail -f /dev/null

