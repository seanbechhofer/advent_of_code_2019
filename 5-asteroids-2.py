import sys
import unittest

# Codes

ADD = 1
MULTIPLY = 2
WRITE = 3
OUTPUT = 4
JUMP_TRUE = 5
JUMP_FALSE = 6
LESS_THAN = 7
EQUALS = 8
HALT = 99

# Steps to increment for each code
STEPS = [0,4,4,2,2,3,3,4,4]
ARGS = [0,3,3,1,1,2,2,3,3]

def debug(arg):
    pass
    #print arg

# Decipher the code and modes
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

# Execute the instruction according to the given state
# Lot of duplication here. Could be much better!
def execute_instruction(state):
    prog = state[0]
    counter = state[1]
    opcode = prog[counter]
    increment = True
    (instruction,modes) = split_instruction(opcode)
    if instruction == HALT:
        return False
    
    if instruction == ADD or instruction == MULTIPLY or instruction == LESS_THAN or instruction == EQUALS:
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
        if instruction == LESS_THAN:
            prog[arg3] = 1 if val1 < val2 else 0
        if instruction == EQUALS:
            prog[arg3] = 1 if val1 == val2 else 0

    if instruction == WRITE:
        # Hard coded input!
        arg1 = prog[counter+1]

        prog[arg1] = 5
    if instruction == OUTPUT:
        arg1 = prog[counter+1]
        val1 = prog[arg1]
        if modes[0] != 0:
            val1 = arg1
        print(val1)

    if instruction == JUMP_TRUE or instruction == JUMP_FALSE:
        arg1 = prog[counter+1]
        arg2 = prog[counter+2]
        if modes[0] != 0:
            val1 = arg1
        else:
            val1 = prog[arg1]
                    
        if modes[1] != 0:
            val2 = arg2
        else:
            val2 = prog[arg2]
        if instruction == JUMP_TRUE:
            if val1 != 0:
                state[1] = val2
                increment = False
        if instruction == JUMP_FALSE:
            if val1 == 0:
                state[1] = val2
                increment = False

    if increment:
        state[1] = counter + STEPS[instruction]
    return True
        

if __name__=='__main__':
#    unittest.main()
    prog = [int(s) for s in sys.stdin.readline().strip().split(",")]
    counter = 0
    state = [prog,counter]
    while (execute_instruction(state)):
        pass
