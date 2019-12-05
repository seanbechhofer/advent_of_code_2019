import sys
import unittest

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertEqual(calculate([]),0)
    def test_two(self):
        self.assertEqual(calculate([]),0)

ADD = 1
MULTIPLY = 2
WRITE = 3
OUTPUT = 4
HALT = 99

STEPS = [0,4,4,2,2]

def debug(arg):
    pass
    #print arg

def split_instruction(opcode):
    instruction = opcode % 100
    parameter_modes = opcode / 100
    modes = [0,0,0]
    modes[0] = parameter_modes % 10
    parameter_modes = parameter_modes / 10
    modes[1] = parameter_modes % 10
    parameter_modes = parameter_modes / 10
    modes[2] = parameter_modes % 10
    parameter_modes = parameter_modes / 10
    return (instruction,modes)

def execute_instruction(state):
    prog = state[0]
    counter = state[1]
    opcode = prog[counter]
    (instruction,modes) = split_instruction(opcode)
    if instruction == HALT:
        return False
    if instruction == ADD or instruction == MULTIPLY:
        arg1 = prog[counter+1]
        arg2 = prog[counter+2]
        arg3 = prog[counter+3]

        if modes[0] != 0:
            val1 = arg1
        else:
            val1 = prog[arg1]
                    
        if modes[1] != 0:
            val2 = arg2
        else:
            val2 = prog[arg2]

        if instruction == ADD:
            prog[arg3] = val1 + val2
        if instruction == MULTIPLY:
            prog[arg3] = val1 * val2
    if instruction == WRITE:
        prog[prog[counter+1]] = 1
    if instruction == OUTPUT:
        arg1 = prog[counter+1]
        val1 = prog[arg1]
        if modes[0] != 0:
            val1 = arg1
        print(val1)
    state[1] = counter + STEPS[instruction]
    return True
        

def calculate(lines):
    # Do some stuff
    return 0

if __name__=='__main__':
#    unittest.main()
    prog = [int(s) for s in sys.stdin.readline().strip().split(",")]
    counter = 0
    state = [prog,counter]
    while (execute_instruction(state)):
        pass
