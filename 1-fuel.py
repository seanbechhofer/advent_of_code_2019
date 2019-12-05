import sys
import math

def debug(arg):
    pass
    #print arg

def fuel(mass):
    fuel = (math.floor(mass/3) - 2)
    return fuel
    
if __name__=='__main__':
    total = 0
    for line in sys.stdin:
        mass = int(line.strip())
        fuel = (math.floor(mass/3) - 2)
        total += fuel
print(total)
