#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:20:48 2024

@author: fberal
"""

def position(pos,mouv):
    p=pos
    if mouv == '<':
        p[0] -= 1
    elif mouv == '>':
        p[0] += 1
    elif mouv == '^':
        p[1] += 1
    else:
        p[1] -= 1
    return p


def santa1(file):
    pos=[0,0]
    list_pos=[[0,0]]
    with open(file,"r") as ftxt:
        ligne=ftxt.readline()
        for i in ligne:
            pos1=[int(d) for d in position(pos, i)]
            if not(pos1 in list_pos):
                list_pos.append(pos1)
    nb_houses=len(list_pos)
    return(nb_houses)

def santa2(file):
    pos_santa=[0,0]
    pos_robo=[0,0]
    list_pos_santa=[[0,0]]
    list_pos_robo=[[0,0]]
    santa=True
    with open(file,"r") as ftxt:
        ligne=ftxt.readline()
        for i in ligne:
            if santa:
                pos1=[int(d) for d in position(pos_santa, i)]
                if not(pos1 in list_pos_santa):
                    list_pos_santa.append(pos1)
                santa=not(santa)
            else:
                pos1=[int(d) for d in position(pos_robo, i)]
                if not(pos1 in list_pos_robo):
                    list_pos_robo.append(pos1)
                santa=not(santa)
    for k in list_pos_robo:
        if not(k in list_pos_santa):
            list_pos_santa.append(k)
    nb_houses=len(list_pos_santa)
    return(nb_houses)

