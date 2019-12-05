import sys
import math

def debug(arg):
    pass
    #print arg

def fuel_for_mass(mass):
    fuel = (math.floor(mass/3) - 2)
    return int(fuel)
    
if __name__=='__main__':
    total = 0
    for line in sys.stdin:
        mass = int(line.strip())
        fuel = fuel_for_mass(mass)
        while (fuel > 0):
            total += fuel
            fuel = fuel_for_mass(fuel)
print(total)
