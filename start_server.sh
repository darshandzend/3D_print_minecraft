#!/bin/bash 
set -e
cd server
if [[ ! -f server.jar ]]; then
    curl -vkL 'https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar' -o server.jar;
fi
     
screen -S minecraft java -Xmx10G -jar server.jar nogui
