# 3D Print minecraft structures with mathematical functions

## Components
1. Python 3
2. Minecraft Server 1.16
3. [Screen (linux utility)](https://linux.die.net/man/1/screen)
4. Docker (optional, only for ease of packaging)

## How it works

1. Start a superflat world with minecraft server on port specified in server.properties. This starts the server in a terminal
2. You can join the server from the minecraft client to see blocks being placed in real time
3. 'Screen' connects to this terminal to send minecraft commands
4. `generate.py` generates y and z coordinates (corrosponding to x) with specified functions
5. `generate.py` also sends the `screen` commands to the minecraft server


