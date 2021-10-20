#!/bin/bash 
cd server
screen -S minecraft java -Xmx10G -jar server.jar nogui
