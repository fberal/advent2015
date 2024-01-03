#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:20:48 2024

@author: fberal
"""


def three_vowels(my_string):
    k=0
    i=0
    l_str = len(my_string)
    while k<3 and i<l_str:
        car_i=my_string[i]
        if car_i in ['a','e','i','o','u']:
            k+=1
        i+=1
    return(k==3)

def double_letter(my_string):
    dl = False
    i = 0
    l_str = len(my_string)-1
    while (not dl) and i<l_str:
        if my_string[i] == my_string[i+1]:
            dl = True
        else:
            i+=1
    return dl

def forbiden_str(my_string):
    fs = False
    i = 0
    l_str = len(my_string)-1
    while (not fs) and i<l_str:
        if my_string[i] + my_string[i+1] in ['ab','cd','pq','xy']:
            fs = True
        else:
            i+=1
    return fs

def nice1(my_string):
    tv = three_vowels(my_string)
    dl = double_letter(my_string)
    fs = not forbiden_str(my_string)
    return (tv and dl and fs)

def count_nice1(my_file):
    count=0
    with open(my_file,"r") as fichier:
        for l in fichier:
            if nice1(l):
                count+=1
    return count

def double_double(my_string):
    l=len(my_string)
    if l<4:
        return False
    elif my_string[0] + my_string[1] in my_string[2:]:
        return True
    else:
        return double_double(my_string[1:])
        
def between(my_string):
    l=len(my_string)
    if l<3:
        return False
    elif my_string[0] == my_string[2]:
        return True
    else:
        return between(my_string[1:])
            
def nice2(my_string):
    dd = double_double(my_string)
    bw = between(my_string)
    return dd and bw

def count_nice2(my_file):
    count=0
    with open(my_file,"r") as fichier:
        for l in fichier:
            if nice2(l):
                count+=1
    return count