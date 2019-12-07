import sys
import unittest
import itertools

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

class TestStuff(unittest.TestCase):
    def test_one(self):
        program = [int(s) for s in "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(",")]
        self.assertEqual(calculate(program),43210)
    def test_two(self):
        program = [int(s) for s in "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(",")]
        self.assertEqual(calculate(program),54321)
    def test_three(self):
        program = [int(s) for s in "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(",")]
        self.assertEqual(calculate(program),65210)
        
# Steps to increment for each code
def debug(arg):
    #pass
    print(arg)

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
# Added io object to allow passing of multiple parameters and output
def execute_instruction(state,io):
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
        arg1 = memory[counter+1]
        # Take the first input value
        memory[arg1] = io['input'][0]
        # Pop the stack
        io['input'] = io['input'][1:]
        
    if instruction == OUTPUT:
        arg1 = get_parameter(memory,counter,1,modes[0])
        io['output'] = arg1

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

def run_program(program,input_values):
    current_value = 0
    for i in input_values:
        memory = program.copy()
        io = {'input': [i,current_value]}
        state = [memory,0]
        while (execute_instruction(state,io)):
            pass
        current_value = io['output']
    return current_value

def calculate(program):
    values = list(range(0,5))
    fives = [f for f in list(itertools.permutations(values)) if len(f) ==5]
    maximum = 0
    settings = None
    for params in fives:
        value = run_program(program,params)
        if value > maximum:
            maximum = value
            settings = params
    return maximum
        
if __name__=='__main__':
#    unittest.main()
    program = [int(s) for s in sys.stdin.readline().strip().split(",")]
    print(calculate(program))
