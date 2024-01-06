#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:44:18 2024

@author: fberal
"""

bit16 = 2**16


my_dict = {'AND':' & ','OR':' | ','LSHIFT':' << ','RSHIFT':' >> '}

my_file_in = "input-2015_07.txt"

with open(my_file_in, "r") as file_in:
    export = []
    export_init = []
    end = ' % bit16 \n'
    for l in file_in:
        ligne = [str(d) for d in l.split(" ")]
        k = len(ligne)
        begin = ligne[-1]
        begin = begin.removesuffix('\n')
        export_init.append(begin)
        if k == 3:
            export.append([begin, ligne[0]])
        elif k == 4:
            export.append([begin, '~ ', ligne[1]])
        else:
            ope = my_dict[ligne[1]]
            export.append([begin, ligne[0], ope, ligne[2]])
            
def my_index(var,list_index): 
    if var in list_index:
        return list_index.index(var)
    else:
        return -1
            
def index_def(x,list_index): 
    k = len(x)
    if k < 4:
        x1 = x[-1]
        return my_index(x1,list_index)
    else:
        x1 = x[1]
        x2 = x[3]
        k1 = my_index(x1, list_index)
        k2 = my_index(x2, list_index)
        return max(k1,k2)
    
def permute(index0,index1,x,my_list):
    my_list.insert(index1+1,x)
    my_list.pop(index0)
    

def is_def(x,list_index):
    x_ind = list_index.index(x[0])
    x_def = index_def(x,list_index)
    return x_ind > x_def

def ranger(my_list,list_index):
    k = len(my_list)
    i = 0
    while i < k-1:
        x = my_list[i]
        x_ind_def = index_def(x,list_index)
        if x_ind_def < i:
            i += 1
        else:
            permute(i, x_ind_def, x, my_list)
            permute(i, x_ind_def, x[0], list_index)

ranger(export, export_init)


my_file_out = "export-2015_07_1.txt"

with open(my_file_out, "a") as file_out:
    for d in export:
        ligne = ''
        d[0] += ' = '
        d[-1] += end
        for i in d:
            ligne += i
        file_out.write(ligne)


