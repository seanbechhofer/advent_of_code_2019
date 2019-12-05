import sys

DIRECTIONS = {
    'U': (0,1),
    'D': (0,-1),
    'R': (1,0),
    'L': (-1,0)
    }

def manhattan(c1,c2):
#    print(abs(c1[0]-c2[0]))
#    print(abs(c1[1]-c2[1]))
    result = abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])
#    print(result)
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

if __name__=='__main__':
    wire1 = sys.stdin.readline().split(",")
    wire2 = sys.stdin.readline().split(",")

    wire1_coords = [(0,0)]
    wire2_coords = [(0,0)]

    for spec in wire1:
        add_to_coords(wire1_coords,spec)

    for spec in wire2:
        add_to_coords(wire2_coords,spec)
    
    print(wire1_coords)
    print(wire2_coords)

    wire1_set = set(wire1_coords)
    wire2_set = set(wire2_coords)

    crossing_points = wire1_set.intersection(wire2_set)

    print(crossing_points)
    minimum = 1000000
    for c in crossing_points:
        if (c[0]!=0 and c[1]!=0):
            wire_1_distance = wire1_coords.index(c)
            wire_2_distance = wire2_coords.index(c)
            print(wire_1_distance)
            print(wire_2_distance)
            distance = wire_1_distance + wire_2_distance
            minimum = minimum if distance > minimum else distance
    print(minimum)
