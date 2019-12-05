import sys
import unittest

class TestStuff(unittest.TestCase):

    def test_one(self):
        self.assertEqual(calculate(["R8,U5,L5,D3","U7,R6,D4,L4"]),6)

    def test_two(self):
        self.assertEqual(calculate(["R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83"]),159)

DIRECTIONS = {
    'U': (0,1),
    'D': (0,-1),
    'R': (1,0),
    'L': (-1,0)
    }

def manhattan(c1,c2):
    result = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
    return result
    
def add_coords(c1,c2):
    return (c1[0]+c2[0],c1[1]+c2[1])

def debug(arg):
    pass
    #print arg

def calculate(input):
    result = 0
    return result

def run_test(input,expected):
    return (calculate(input) == expected)

def add_to_coords(coords,spec):
    last = coords[-1]
    increment = DIRECTIONS[spec[0]]
    length = int(spec[1:])
    
    for i in range(0,length):
        last = add_coords(last,increment)
        coords.append(last)

def calculate(lines):
    wire1 = lines[0].split(",")
    wire2 = lines[1].split(",")

    wire1_coords = [(0,0)]
    wire2_coords = [(0,0)]

    for spec in wire1:
        add_to_coords(wire1_coords,spec)

    for spec in wire2:
        add_to_coords(wire2_coords,spec)
    
    debug(wire1_coords)
    debug(wire2_coords)

    wire1_set = set(wire1_coords)
    wire2_set = set(wire2_coords)

    crossing_points = wire1_set.intersection(wire2_set)

    debug(crossing_points)
    minimum = 1000000
    for c in crossing_points:
        if (c[0]!=0 and c[1]!=0):
            distance = manhattan((0,0),c)
            minimum = minimum if distance > minimum else distance
    debug(minimum)
    return minimum

if __name__=='__main__':
    unittest.main()
    lines = []
    lines.append(sys.stdin.readline())
    lines.append(sys.stdin.readline())
    result = calculate(lines)
    print(result)
