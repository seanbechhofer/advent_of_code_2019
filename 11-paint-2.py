import sys
import unittest
from intcode import Machine

class TestStuff(unittest.TestCase):
    def test_1(self):
        start = (0,0)
        self.assertEqual(move(start,WEST),(-1,0))
    def test_2(self):
        start = (0,0)
        self.assertEqual(move(start,EAST),(1,0))
    def test_3(self):
        start = (0,0)
        self.assertEqual(move(start,NORTH),(0,1))
    def test_4(self):
        start = (0,0)
        self.assertEqual(move(start,SOUTH),(0,-1))

    def test_5(self):
        start = (0,0)
        direction = turn(LEFT,NORTH)
        self.assertEqual(direction,WEST)
    def test_6(self):
        start = (0,0)
        direction = turn(LEFT,WEST)
        self.assertEqual(direction,SOUTH)
    def test_7(self):
        start = (0,0)
        direction = turn(RIGHT,EAST)
        self.assertEqual(direction,SOUTH)
    def test_8(self):
        start = (0,0)
        direction = turn(RIGHT,SOUTH)
        self.assertEqual(direction,WEST)


BLACK = 0
WHITE = 1

LEFT = 0
RIGHT = 1

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

DELTA = {
    NORTH: (0,1),
    EAST: (1,0),
    SOUTH: (0,-1),
    WEST: (-1,0)
    }


# Steps to increment for each code
def debug(arg):
    pass
    #print(arg)

def turn(rotation,direction):
    if rotation == LEFT:
        return (direction - 1) % 4
    else:
        return (direction + 1) % 4

def move(position,direction):
    return (position[0] + DELTA[direction][0],
            position[1] + DELTA[direction][1])

def get_colour(position,hull):
    if position in hull:
        return hull[position]
    else:
        return BLACK

def paint_panel(position,colour,hull):
    painted = 0
    if not position in hull:
        painted = 1
    hull[position] = colour
    return painted

if __name__=='__main__':
#    unittest.main()
    program_source = "3,8,1005,8,325,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,29,1006,0,41,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,54,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,76,1,9,11,10,2,5,2,10,2,1107,19,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,110,2,1007,10,10,2,1103,13,10,1006,0,34,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,142,1006,0,32,1,101,0,10,2,9,5,10,1006,0,50,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,179,1,1005,11,10,2,1108,11,10,1006,0,10,1,1004,3,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,216,1,1002,12,10,2,1102,3,10,1,1007,4,10,2,101,7,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,253,2,104,3,10,1006,0,70,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,282,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,305,101,1,9,9,1007,9,962,10,1005,10,15,99,109,647,104,0,104,1,21102,838211572492,1,1,21102,342,1,0,1105,1,446,21102,825326674840,1,1,21101,0,353,0,1106,0,446,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,29086686211,1,21102,1,400,0,1106,0,446,21102,209420786919,1,1,21101,0,411,0,1105,1,446,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,838337298792,1,21101,434,0,0,1105,1,446,21101,988661154660,0,1,21102,1,445,0,1106,0,446,99,109,2,21201,-1,0,1,21101,40,0,2,21101,0,477,3,21101,0,467,0,1105,1,510,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,472,473,488,4,0,1001,472,1,472,108,4,472,10,1006,10,504,1101,0,0,472,109,-2,2106,0,0,0,109,4,1201,-1,0,509,1207,-3,0,10,1006,10,527,21102,0,1,-3,22102,1,-3,1,22102,1,-2,2,21101,0,1,3,21101,546,0,0,1105,1,551,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,574,2207,-4,-2,10,1006,10,574,21201,-4,0,-4,1105,1,642,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,593,0,1105,1,551,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,612,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,634,21202,-1,1,1,21102,1,634,0,105,1,509,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0"
    program = [int(s) for s in program_source.split(",")]
    current_position = (0,0)
    current_direction = NORTH
    hull = {
        (0,0): WHITE
        }
    painted = 0
    machine = Machine()
    machine.memory = program.copy()
    machine.counter = 0
    machine.io = {'input': [WHITE], 'output': []}
    run = True
    while (run):
        while (machine.execute_instruction() and len(machine.io['output']) != 2):
            pass
        if len(machine.io['output'])!=2:
            run = False
        else:    
            debug(machine.io)
            colour = machine.io['output'][0]
            rotation = machine.io['output'][1]
            painted = painted + paint_panel(current_position,colour,hull)
            current_direction = turn(rotation,current_direction)
            current_position = move(current_position,current_direction)
            current_colour = get_colour(current_position,hull)
            debug("Now at: {}".format(current_position))
            debug("Colour is: {}".format(current_colour))
            debug("Painted: {}".format(painted))
            # Need to move and then check to see what colour the square is. 
            machine.io = {'input': [current_colour], 'output': []}
    whites = set([point for point in hull.keys() if hull[point] == WHITE])
    x_s = [point[0] for point in hull.keys()]
    y_s = [point[1] for point in hull.keys()]
    min_x = min(x_s)
    max_x = max(x_s)
    min_y = min(y_s)
    max_y = max(y_s)

    print()
    for y in range(max_y,min_y-1,-1):
        line = []
        for x in range(min_x,max_x+1):
            if (x,y) in whites:
                line.append("X")
            else:
                line.append(" ")
        print("".join(line))
    print()
            
