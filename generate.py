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

height = 9
length = 17
bredth = 17

structure = height * [ bredth * [ length * [ False ] ] ] 
#structure = [ [ [ False for _ in range(length) ] for _ in range(bredth) ] for _ in range(height) ]

def main():
    # Clear the area and place markers
    fill(0,0,0,length,bredth,height,'air')
    plot_point(-1,-1,-1,'red_concrete')
    plot_point(-1,bredth+1,-1,'red_concrete')
    plot_point(length+1,-1,-1,'red_concrete')
    plot_point(length+1,bredth+1,-1,'red_concrete')
    plot_point(-1,-1,height+1,'blue_concrete')
    plot_point(-1,bredth+1,height+1,'blue_concrete')
    plot_point(length+1,-1,height+1,'blue_concrete')
    plot_point(length+1,-1,height+1,'blue_concrete')


    # fill 3D map 'structure' with shapes
    fill_structure()

    time.sleep(3)
    for z, z_list in enumerate(structure):
        for y, y_list in enumerate(z_list):
            for x, x_list in enumerate(y_list):
                if(structure[z][y][x]):
                    plot_point(x,y,z)
        time.sleep(1)


# This is the function which actually defines the 3D shape
# Change this according to your needs
#TODO: Externalisation
def fill_structure():
    for z, _ in enumerate(structure):
        r = radius_at_level(z)
        print(z,r)
        structure[z] = moved(circle(radius=r), z)

def radius_at_level(z):
    return math.floor( math.sqrt ( 8**2 - z**2 ) ) -1 

# ---------------------------------


# ---- Utilities --------------
def moved(matrix, distance):
    # Moves a given 2D matrix w.r.t origin by a given distance
    # Returns a new matrix
    filled = [ [ False for _ in range(length) ] for _ in range(bredth) ]
    for y,row in enumerate(matrix):
        for x,_ in enumerate(row):
            if (x+distance) < length and (y+distance) < bredth:
                filled[y+distance][x+distance] = matrix[y][x]
    return filled

# ---------------------------------


# ---- Common Shapes --------------
# Each function returns 2d array

def circle(radius=1):
    # Actual size of circle is 1+diameter
    # Equation of shifted circle: (x-a)^2 + (y-b)^2 = r^2
    # The following is expression for the above, but for y,
    # shifted by r along both axes
    shift = radius
    size = (radius*2) + 1
    circle = [ [ False for _ in range(size) ] for _ in range(size) ]
    prev_y = radius
    for x in range(radius+1):
        y = math.floor( math.sqrt( (radius**2) - ((x)**2)) )
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
    #print(cmd)
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

main()
#print_2d(moved(circle(4), 0))
