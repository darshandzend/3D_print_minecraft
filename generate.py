#!/bin/env python3
import math
import time
import subprocess

from os import system

DEFAULT_SUBSTANCE = 'smooth_stone'

# Offsets determine the origin point (0,0,0) in 3D space
x_offset = 0
y_offset = 0
z_offset = 5

height = 8
length = 16
bredth = 16

structure = height * [ length * [ bredth * [False]]]

def main():
    # initialise the area
    fill(0,0,0,length,bredth,height,'air')
    plot_point(-1,-1,-1,'red_concrete')
    plot_point(length+1,bredth+1,height+1,'blue_concrete')


    # fill structure with shapes
    fill_structure()

    time.sleep(3)
    for z, z_list in enumerate(structure):
        for y, y_list in enumerate(z_list):
            for x, x_list in enumerate(y_list):
                print(x,y,z)
                if(structure[z][y][x]):
                    plot_point(x,y,z)
        time.sleep(1)


# This is the function which actually defined the 3d shape
# Change this according to your needs
def fill_structure():
    for z, z_list in enumerate(structure):
        structure[z] = circle(radius=(int(bredth/2))-z)

# ---- Common Shapes --------------
# Each function returns 2d array

def circle(radius=1):
    # Actual size of circle is 1+diameter
    # Equation of shifted circle: (x-a)^2 + (y-b)^2 = r^2
    # The following is expression for the above, but for y,
    # shifted by r along both axes
    shift = radius
    size = (radius*2) + 1
    circle = list(map(lambda _:
            list(map(lambda _: False, range(size))),
        range(size)))
    prev_y = radius
    for x in range(radius+1):
        y = math.floor( math.sqrt( (radius**2) - ((x)**2)) )
        print("Coords y,x:",y,x)
        # Fill main points
        #circle[y][x] = True
        circle[y+shift][x+shift] = True
        circle[y+shift][-x+shift] = True
        circle[-y+shift][x+shift] = True
        circle[-y+shift][-x+shift] = True
        # Fill empty x spaces if the y jump is too steep
        if prev_y - y > 1:
            for fill_y in range(y+1, prev_y):
                #circle[fill_y][x-1] = True
                circle[fill_y+shift][x-1+shift] = True
                circle[fill_y+shift][-x+1+shift] = True
                circle[-fill_y+shift][x-1+shift] = True
                circle[-fill_y+shift][-x+1+shift] = True
        prev_y = y
    return circle
# ---------------------------------


# ---- Core Utility functions -----
def plot_point(x,y,z,substance=DEFAULT_SUBSTANCE):
    fill(x, y, z, x, y, z, substance)

def fill(x1, y1, z1, x2, y2, z2, substance=DEFAULT_SUBSTANCE):
    x1 += x_offset
    x2 += x_offset
    y1 += y_offset
    y2 += y_offset
    z1 += z_offset
    z2 += z_offset
    send_cmd("fill {} {} {} {} {} {} {}".format(x1, z1, y1, x2, z2, y2, substance))

def send_cmd(cmd):
    print(cmd)
    cmd = cmd + "\\n"
    subprocess.call(["screen", "-S", "minecraft", "-X", "stuff", "{}".format(cmd)])

    #input("")
# ---------------------------------


# ---- Debug helpers --------------
def print_2d(array_2d):
    print("Rows: ",len(array_2d))
    for y in reversed(array_2d):
        line = ""
        for x in y:
            if(x):
                line += "■"
            else:
                line += "·"
        print(line)

#main()
print_2d(circle(8))

