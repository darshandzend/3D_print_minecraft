# 3D Print minecraft structures with mathematical functions

https://user-images.githubusercontent.com/4941002/138025226-a1703ead-04fb-48b7-a994-c3c429587f2c.mp4


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

# Useful resources and Tips
* https://www.desmos.com/calculator to visualize a function in 2D
* You can undo generated structure by setting `DEFAULT_SUBSTANCE` to 'air' and rerunning 

