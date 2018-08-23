#!/bin/bash
service mysql start 
mysql < ./schema.sql 
service mysql status 

myip=$(curl ipconfig.me)
sed -i "s/<externalAddress>.*<\/externalAddress>/<externalAddress>$myip<\/externalAddress>/g" ./res/server/kbengine.xml 

sh ./start_server.sh
sh -c "$*" 

tail -f /dev/null

