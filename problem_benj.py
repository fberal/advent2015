#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Benj

@author: fberal
"""


def possib_k(k):
    if k==0:
        return []
    elif k==1:
        return [[2],[3]]
    else:
        possib = [[2],[3]]
        for a in range(k-1):
            add2 = [possib[i]+[2] for i in range(len(possib))]
            add3 = [possib[i]+[3] for i in range(len(possib))]
            possib = add2 + add3
    return possib

def all_possi(x):
    ans = []
    min = x // 3
    max = x // 2
    for k in range(min, max+1):
        poss = possib_k(k)
        for d in poss:
            if sum(d) <= x:
                ans.append(d)
    return ans

def sol_lign(x):
    ans = []
    for d in all_possi(x):
        if sum(d) == x:
            ans.append(d)
    return ans

def superpose(l0,l1):
    i = 0
    j = 0
    a = l0[0]
    b = l1[0]
    x = sum(l0)
    while a!= b:
        if a < b:
            i += 1
            a += l0[i]
        else:
            j += 1
            b += l1[j]
    return a == x or b == x

def add_lign(lign0,k):
    res = []
    ligne_up = sol_lign(k)
    for d in lign0:
        for l_u in ligne_up:
            if superpose(d, l_u):
                res.append(l_u)
    return res
    
    
def mur(x,y):
    ligne_up = sol_lign(x)
    for i in range(y-1):
        ligne_up = add_lign(ligne_up,x)
        if ligne_up == []:
            break
    return ligne_up
        
x = 10
y = 3
solution = len(mur(x,y))

if y == 1:
    lignes = "ligne"
else:
    lignes = "lignes"

if solution <2:
    solus = "solution"
else:
    solus = "solutions"


print(f"Mur de {x} de large et de {y} {lignes} : {solution} {solus}.")

    