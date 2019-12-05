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

# Probably don't need args.
LANG = {
    ADD: {"steps": 4, "args": 3},
    MULTIPLY: {"steps": 4, "args": 3},
    WRITE: {"steps": 2, "args": 1},
    OUTPUT: {"steps": 2, "args": 1},
    JUMP_TRUE: {"steps": 3, "args": 2},
    JUMP_FALSE: {"steps": 3, "args": 2},
    LESS_THAN: {"steps": 4, "args": 3},
    EQUALS: {"steps": 4, "args": 3},
    HALT: {}
}
    
# Steps to increment for each code
def debug(arg):
    pass
    #print(arg)

# Decipher the code and modes
def split_instruction(opcode):
    instruction = opcode % 100
    parameter_modes = int(opcode / 100)
    modes = []
    # Operands have no more that two referenceable arguments. 
    for i in range(0,2):
        modes.append(parameter_modes % 10)
        parameter_modes = int(parameter_modes / 10)
    return (instruction,modes)

# Get the value given the counter, offset and access mode.
def get_parameter(memory,counter,offset,mode):
    val = memory[counter+offset]
    if mode == 0:
        return memory[val]
    else:
        return val
    
# Execute the instruction according to the given state
# Lot of duplication here. Could be much better!
def execute_instruction(state):
    memory = state[0]
    counter = state[1]
    opcode = memory[counter]

    increment = True
    (instruction,modes) = split_instruction(opcode)
    if instruction == HALT:
        return False
    
    if instruction == ADD or instruction == MULTIPLY or instruction == LESS_THAN or instruction == EQUALS:
        arg1 = get_parameter(memory,counter,1,modes[0])
        arg2 = get_parameter(memory,counter,2,modes[1])
        arg3 = get_parameter(memory,counter,3,1)

        if instruction == ADD:
            memory[arg3] = arg1 + arg2
        if instruction == MULTIPLY:
            memory[arg3] = arg1 * arg2
        if instruction == LESS_THAN:
            memory[arg3] = 1 if arg1 < arg2 else 0
        if instruction == EQUALS:
            memory[arg3] = 1 if arg1 == arg2 else 0

    if instruction == WRITE:
        # Hard coded input!
        arg1 = memory[counter+1]
        memory[arg1] = 5
        
    if instruction == OUTPUT:
        arg1 = get_parameter(memory,counter,1,modes[0])
        print(arg1)

    if instruction == JUMP_TRUE or instruction == JUMP_FALSE:
        arg1 = get_parameter(memory,counter,1,modes[0])
        arg2 = get_parameter(memory,counter,2,modes[1])
            
        if instruction == JUMP_TRUE:
            if arg1 != 0:
                state[1] = arg2
                increment = False
        if instruction == JUMP_FALSE:
            if arg1 == 0:
                state[1] = arg2
                increment = False

    if increment:
        state[1] = counter + LANG[instruction]['steps']
    return True
        
if __name__=='__main__':
#    unittest.main()
    memory = [int(s) for s in sys.stdin.readline().strip().split(",")]
    counter = 0
    state = [memory,counter]
    while (execute_instruction(state)):
        pass
