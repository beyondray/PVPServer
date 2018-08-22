#!/bin/bash
service mysql start 
mysql < ./schema.sql 
service mysql status 

sh ./start_server.sh
sh -c "$*" 

tail -f /dev/null

