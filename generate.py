#!/bin/env python3
import math
import time
import subprocess

from os import system

DEFAULT_SUBSTANCE = 'air'
DEFAULT_SUBSTANCE = 'smooth_stone'

# Offsets determine the origin point (0,0,0) in 3D space
x_offset = 8
y_offset = 8
z_offset = 5

height = 17
length = height*2
bredth = height*2

def main():
    # Clear area
    fill(0,0,0,length,bredth,height,'air')
    fill(0,0,0,-length,bredth,height,'air')
    fill(0,0,0,length,-bredth,height,'air')
    fill(0,0,0,-length,-bredth,height,'air')

    fill_structure()


# This is the function which actually defines the 3D shape
# Change this according to your needs
#TODO: Externalisation
def fill_structure():
    # Central pillar
    fill(0,0,0,0,0,height)

    # Dome
    for z in range(height):
        center=(0,0,z)
        r = radius_at_level(z)
        draw_circle(r,center)
        #time.sleep(1)

def radius_at_level(z):
    # Tip: To picture this curve better, just rotate your imaginary x-y axis
    # such that 'z' variable is horizontal, growing rightwards

    x = height-z

    #return math.floor( math.sqrt ( height**2 - z**2 ) ) -1  # Circle
    return round( math.sqrt( 5*x ) ) # Parabola

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
def draw_circle(r,center):
    shift_x = center[0]
    shift_y = center[1]
    z = center[2]
    prev_y = r
    for x in range(r+1):
        y = round( math.sqrt( (r**2) - ((x)**2)) )
        plot_point(x+shift_x,y+shift_y,z)
        plot_point(x+shift_x,-y+shift_y,z)
        plot_point(-x+shift_x,y+shift_y,z)
        plot_point(-x+shift_x,-y+shift_y,z)
        # Fill empty x spaces if the y jump is too steep
        if prev_y - y > 1:
            for fill_y in range(y+1, prev_y):
                plot_point(x-1+shift_x,fill_y+shift_y,z)
                plot_point(x-1+shift_x,-fill_y+shift_y,z)
                plot_point(-x+1+shift_x,fill_y+shift_y,z)
                plot_point(-x+1+shift_x,-fill_y+shift_y,z)
        prev_y = y

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

main()
