#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:20:48 2024

@author: fberal
"""

def area(list_dim):
    a = 3*list_dim[0]*list_dim[1]+2*list_dim[1]*list_dim[2]+2*list_dim[0]*list_dim[2]
    return a

def length_of_ribbon(list_dim):
    lor=2*list_dim[0]+2*list_dim[1]+list_dim[0]*list_dim[1]*list_dim[2]
    return lor

def total_area(fichier):
    s=0
    with open(fichier, "r") as fichiertxt:
        for l in fichiertxt:
            ligne=[int(d) for d in l.split("x")]
            ligne.sort()
            s+=area(ligne)
    return(s)

def total_length(fichier):
    s=0
    with open(fichier, "r") as fichiertxt:
        for l in fichiertxt:
            ligne=[int(d) for d in l.split("x")]
            ligne.sort()
            s+=length_of_ribbon(ligne)
    return(s)

