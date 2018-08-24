#!/bin/bash

localhost=false
if [ -n "$1" ]; then
  if [[ "$1" == '-l' || "$1" == '--localhost' ]]; then
    localhost=true
  elif [[ "$1" == '-h' || "$1" == '--help' ]]; then
    echo "Usage: bash run_pvpdocker.sh [option]..."
    echo "use this bash run docker container."
    echo ""
    echo "Option usage:"
    echo "-l, --localhost     use this param in localhost"
    echo "-h, --help          show shell help"
    exit 0
  fi  
fi

dockername=pvp
docker rm $dockername 
docker run --name $dockername -e "LOCALHOST=$localhost" -p 20013:20013 -p 20015:20015 -it pvpserver
