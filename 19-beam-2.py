import sys
import unittest
from intcode_threaded import Machine
from queue import Queue
import threading
import os
import time
import numpy as np

INPUT = "109,424,203,1,21102,1,11,0,1106,0,282,21101,0,18,0,1105,1,259,2102,1,1,221,203,1,21102,31,1,0,1106,0,282,21101,38,0,0,1106,0,259,21002,23,1,2,21202,1,1,3,21102,1,1,1,21102,57,1,0,1106,0,303,2102,1,1,222,21001,221,0,3,21002,221,1,2,21101,0,259,1,21102,1,80,0,1106,0,225,21102,1,93,2,21102,1,91,0,1106,0,303,2101,0,1,223,21001,222,0,4,21102,1,259,3,21101,225,0,2,21101,225,0,1,21101,118,0,0,1106,0,225,20101,0,222,3,21102,1,120,2,21102,1,133,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1106,0,259,2102,1,1,223,21001,221,0,4,20102,1,222,3,21102,1,23,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,195,1,0,106,0,108,20207,1,223,2,20101,0,23,1,21101,-1,0,3,21102,1,214,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,21201,-3,0,1,21201,-2,0,2,21202,-1,1,3,21101,0,250,0,1105,1,225,21202,1,1,-4,109,-5,2106,0,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21102,343,1,0,1106,0,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21101,0,384,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21202,1,1,-4,109,-5,2106,0,0"

STATIONARY = 0
PULLED = 1

def probe(program,x,y):
    machine = Machine()
    machine.memory = program.copy()
    machine.counter = 0
    machine.trace = False
    machine.io = {'input': Queue(), 'output': Queue()}
    machine.io['input'].put(x)
    machine.io['input'].put(y)
    machine.run()
    answer = machine.io['output'].get()
    machine.io['output'].task_done()
    return (answer == PULLED)

def probe_square(program,x,y):
    return (probe(program,x,y) and probe(program,x+99,y) and probe(program,x,y+99) and probe(program,x+99,y+99))

if __name__=='__main__':
    program = [int(s) for s in INPUT.split(",")]
    # Initial course grain probing. 
    hits = []
    for x in range(0,2000,100):
        for y in range(0,2000,100):
            if probe_square(program,x,y):
                hits.append((x,y))
        if x % 1000 == 0:
                print(".")
    closest = hits[0]
    for h in hits:
        if h[0] + h[1] < closest[0] + closest[1]:
            closest = h
    x = closest[0]
    y = closest[1]
    print("{},{}".format(x,y))

    # Now we move closer and closer to the origin until the square no longer fits in the beam. 
    run = True
    while (run):
        print("{},{}".format(x,y))
        # If moving in one square in any direction results in failure, we're done.
        if (not probe_square(program,x,y-1) and
            (not probe_square(program,x-1,y)) and
            (not probe_square(program,x-1,y-1))):
            run = False
        # Otherwise, try shuffling in y, x and diagonal.
        else:
            changed = False
            while (probe_square(program,x,y)):
                y = y - 1
                changed = True
            # We've now moved out of the beam. Shuffle back
            if changed:
                y = y + 1
            change = False
            while (probe_square(program,x,y)):
                x = x - 1
                change = True
            # We've now moved out of the beam. Shuffle back
            if changed:
                x = x + 1
            changed = False
            while (probe_square(program,x-1,y-1)):
                x = x - 1
                y = y - 1
            # We've now moved out of the beam. Shuffle back
            if changed:
                x = x + 1
                y = y + 1
                        
    print("{},{}".format(x,y))
    print(x * 10000 + y)
