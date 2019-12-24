import sys
import unittest
import os
import time

INPUT = """#.#..
.....
.#.#.
.##..
.##.#"""

TEST = """....#
#..#.
#..##
..#..
#...."""

BUG = '#'
EMPTY = '.'

def debug(arg):
    #pass
    print(arg)

class Grid():
    def __init__(self):
        self.grid = []
        for y in range(0,5):
            line = []
            for x in range(0,5):
                line.append(EMPTY)
            self.grid.append(line)
        self.states = set()

    def unravel(self):
        u = []
        for l in self.grid:
            for c in l:
                u.append(c)
        return (''.join(u))

    def remember(self):
        self.states.add(self.unravel())
        
    def get(self,x,y):
        return self.grid[y][x]
    
    def put(self,x,y,b):
        self.grid[y][x] = b

    def bug(self,x,y):
        if x<0 or y<0 or x>4 or y>4:
            return 0
        elif self.grid[y][x] == BUG:
            return 1
        else:
            return 0

    def neighbours(self,x,y):
        return self.bug(x+1,y) + self.bug(x-1,y) + self.bug(x,y+1) + self.bug(x,y-1)

            
    def step(self):
        new_grid = Grid()
        for y in range(0,5):
            for x in range(0,5):
                bugs = self.neighbours(x,y)
                if self.get(x,y) == BUG:
                    if bugs == 1:
                        new_grid.put(x,y,BUG)
                    else:
                        new_grid.put(x,y,EMPTY)
                else:
                    if bugs == 1 or bugs == 2:
                        new_grid.put(x,y,BUG)
                    else:
                        new_grid.put(x,y,EMPTY)
        self.grid = new_grid.grid
        if self.unravel() in self.states:
            return True
        else:
            self.remember()
            return False
         
            
    def show(self):
        os.system('clear')
        for y in range(0,5):
            for x in range(0,5):
                print("{}".format(self.get(x,y)),end='')
            print()
        for y in range(0,5):
            for x in range(0,5):
                print("{}".format(self.neighbours(x,y)),end='')
            print()

    def biodiversity(self):
        rating = 0
        multiplier = 1
        for y in range(0,5):
            for x in range(0,5):
                rating = rating + (self.bug(x,y) * multiplier)
                multiplier = multiplier * 2
        return rating
        
if __name__=='__main__':
    grid = Grid()
    y = 0
    for line in INPUT.strip().split("\n"):
        l = []
        x = 0
        for c in line:
            grid.put(x,y,c)
            x += 1
        y += 1
    grid.remember()
    gen = 0
    done = False
    while(not done):
        grid.show()
        print(gen)
        done = grid.step()
        gen += 1
    grid.show()
    print(grid.biodiversity())
