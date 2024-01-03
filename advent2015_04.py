#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:20:48 2024

@author: fberal
"""

import hashlib

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

def mine1(code):
    k=1
    solve=False
    while not solve:
        code1=code + str(k)
        hash5=computeMD5hash(code1)[:5]
        if hash5 == '00000':
            solve=True
        else:
            k+=1
    return k
            
def mine2(code):
    k=1
    solve=False
    while not solve:
        code1=code + str(k)
        hash5=computeMD5hash(code1)[:6]
        if hash5 == '000000':
            solve=True
        else:
            k+=1
    return k