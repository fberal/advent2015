#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 16:20:48 2024

@author: fberal
"""

import time

start = time.time()

"""
Exemple Ben
class Test:
    def __init__(self, tup):
        self.counter = 0
        self.lights_array = np.zeros( tup )
        
    def change_value(self, x, y, value):
        prev = self.lights_array[x][y]
        self.counter += max(0, prev + value)
        self.lights_array[x][y] = max(0, prev + value)
        

test = Test((1000, 1000))
test.change_value(2, 3)
print(test.counter)
"""

class light_grid:
    def __init__(self, size):
        self.size = size
        
    def turn_on(self, begin, end):
        for x in range(begin[0], end[0]+1):
            for y in range(begin[1], end[1]+1):
                place = x * self.size + y
                self.grid[place] = 1
    
    def turn_off(self, begin, end):
        for x in range(begin[0], end[0]+1):
            for y in range(begin[1], end[1]+1):
                place = x * self.size + y
                self.grid[place] = 0
    
    def toggle(self, begin, end):
        for x in range(begin[0], end[0]+1):
            for y in range(begin[1], end[1]+1):
                place = x * self.size + y
                self.grid[place] = (self.grid[place] + 1) % 2
                
    def somme(self):
        return sum(self.grid)
                
class instruction:    
    def __init__(self,liste):
        self.all = liste
        self.length = len(liste)
    
    def begin(self):
        if self.length == 4:
            k=1
        else:
            k=2
        return [int(d) for d in self.all[k].split(",")]

    def end(self):
        if self.length == 4:
            k=3
        else:
            k=4
        return [int(d) for d in self.all[k].split(",")]
    
size = 1000
            
santa = light_grid(size)
santa.grid = [0 for i in range(size * size)]

def lights(fichier):
    with open(fichier, "r") as fichiertxt:
        for l in fichiertxt:
            ligne=[str(d) for d in l.split(" ")]
            instr = instruction(ligne)
            if len(ligne) == 4:
                santa.toggle(instr.begin(), instr.end())
            elif ligne[1] == 'on':
                santa.turn_on(instr.begin(), instr.end())
            else:
                santa.turn_off(instr.begin(), instr.end())
    global before_return
    before_return = time.time()
    return santa.somme()

my_file = "input-2015_06.txt"

print(lights(my_file))

end = time.time()

print(before_return - start)
print(end-start)
