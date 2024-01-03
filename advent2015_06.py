#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:20:48 2024

@author: fberal
"""

import numpy as np

lights_array = np.zeros( (1000, 1000) )

def turn_on(my_array,my_list):
    x0 = my_list[0]
    x1 = my_list[2]+1
    y0 = my_list[1]
    y1 = my_list[3]+1
    for x in range(x0,x1):
        for y in range(y0,y1):
            my_array[x][y]=1

def turn_off(my_array,my_list):
    x0 = my_list[0]
    x1 = my_list[2]+1
    y0 = my_list[1]
    y1 = my_list[3]+1
    for x in range(x0,x1):
        for y in range(y0,y1):
            my_array[x][y]=0

def toggle(my_array,my_list):
    x0 = my_list[0]
    x1 = my_list[2]+1
    y0 = my_list[1]
    y1 = my_list[3]+1
    for x in range(x0,x1):
        for y in range(y0,y1):
            if my_array[x][y]==0:
                my_array[x][y]=1
            else:
                my_array[x][y]=0


def turn_on1(my_array,my_list):
    x0 = my_list[0]
    x1 = my_list[2]+1
    y0 = my_list[1]
    y1 = my_list[3]+1
    for x in range(x0,x1):
        for y in range(y0,y1):
            my_array[x][y]+=1

def turn_off1(my_array,my_list):
    x0 = my_list[0]
    x1 = my_list[2]+1
    y0 = my_list[1]
    y1 = my_list[3]+1
    for x in range(x0,x1):
        for y in range(y0,y1):
            my_array[x][y]=max(0,my_array[x][y]-1)

def toggle1(my_array,my_list):
    x0 = my_list[0]
    x1 = my_list[2]+1
    y0 = my_list[1]
    y1 = my_list[3]+1
    for x in range(x0,x1):
        for y in range(y0,y1):
            my_array[x][y]+=2

def get_begin_end(my_list):
    if my_list[0] == 'turn':
        begin = [int(d) for d in my_list[2].split(",")]
        end = [int(d) for d in my_list[4].split(",")]
    else:
        begin = [int(d) for d in my_list[1].split(",")]
        end = [int(d) for d in my_list[3].split(",")]
    return begin + end

def lights(fichier):
    with open(fichier, "r") as fichiertxt:
        for l in fichiertxt:
            ligne=[str(d) for d in l.split(" ")]
            b_e = get_begin_end(ligne)
            if ligne[0] == 'turn':
                if ligne[1] == 'on':
                    turn_on(lights_array,b_e)
                else:
                    turn_off(lights_array,b_e)
            else:
                toggle(lights_array,b_e)
    return(np.sum(lights_array))


def lights1(fichier):
    with open(fichier, "r") as fichiertxt:
        for l in fichiertxt:
            ligne=[str(d) for d in l.split(" ")]
            b_e = get_begin_end(ligne)
            if ligne[0] == 'turn':
                if ligne[1] == 'on':
                    turn_on1(lights_array,b_e)
                else:
                    turn_off1(lights_array,b_e)
            else:
                toggle1(lights_array,b_e)
    return(np.sum(lights_array))








