@echo off
set localhost=false

if not "%1" == "" ( 
  if "%1" == "-l" goto set_localhost
  if "%1" == "--localhost" goto set_localhost
  if "%1" == "-h" goto echo_help 
  if "%1" == "--help" goto echo_help
)

:main
    set dockername=pvp
    docker rm %dockername% 
    docker run --name %dockername% -e "LOCALHOST=%localhost%" -p 20013:20013 -p 20015:20015 -it pvpserver
    exit 0

:set_localhost
    set localhost=true
    goto main

:echo_help
    echo Usage: .\run_pvpdocker.sh [option]...
    echo use this bat run docker container.
    echo:     
    echo Option usage:
    echo -l, --localhost     use this param in localhost
    echo -h, --help          show shell help
    exit 0
