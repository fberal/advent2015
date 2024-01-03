#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:20:48 2024

@author: fberal
"""

def position(pos,mouv):
    if mouv == '<':
        p=(pos[0]-1,pos[1])
    elif mouv == '>':
        p=(pos[0]+1,pos[1])
    elif mouv == '^':
        p=(pos[0],pos[1]+1)
    else:
        p=(pos[0],pos[1]-1)
    return p


def santa1(file):
    pos=(0,0)
    set_pos={(0,0)}
    with open(file,"r") as ftxt:
        ligne=ftxt.readline()
        for i in ligne:
            pos=position(pos, i)
            posi=(int(pos[0]),int(pos[1]))
            set_pos.add(posi)
    nb_houses=len(set_pos)
    return(nb_houses)

def santa2(file):
    pos_santa=(0,0)
    pos_robo=(0,0)
    set_pos_santa={(0,0)}
    set_pos_robo={(0,0)}
    santa=True
    with open(file,"r") as ftxt:
        ligne=ftxt.readline()
        for i in ligne:
            if santa:
                pos_santa = position(pos_santa, i)
                posi=(int(pos_santa[0]),int(pos_santa[1]))
                set_pos_santa.add(posi)
                santa=not(santa)
            else:
                pos_robo = position(pos_robo, i)
                posi=(int(pos_robo[0]),int(pos_robo[1]))
                set_pos_robo.add(posi)
                santa=not(santa)
    set_all = set_pos_santa | set_pos_robo
    nb_houses=len(set_all)
    return(nb_houses)

