init_commands=(
    'gamerule doDaylightCycle false'
    'gamerule doWeatherCycle false'
    'setworldspawn -10 -10 5'
    'spawnpoint _zork_ -10 -10 5'
)

for cmd in "${init_commands[@]}"; do
    screen -S minecraft -X stuff "${cmd}\n"
done

