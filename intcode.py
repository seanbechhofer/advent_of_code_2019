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
ADJUST = 9
HALT = 99

# Argument counts for operators
LANG = {
    ADD: {"args": 3},
    MULTIPLY: {"args": 3},
    WRITE: {"args": 1},
    OUTPUT: {"args": 1},
    JUMP_TRUE: {"args": 2},
    JUMP_FALSE: {"args": 2},
    LESS_THAN: {"args": 3},
    EQUALS: {"args": 3},
    ADJUST: {"args": 1},
    HALT: {}
}

# Modes
POSITION = 0
IMMEDIATE = 1
RELATIVE = 2


class TestStuff(unittest.TestCase):
    def test_1(self):
        prog = "1,9,10,3,2,3,11,0,99,30,40,50"
        program = [int(s) for s in prog.split(",")]
        machine = Machine()
        machine.memory = program.copy()
        machine.counter = 0
        machine.io = {'input': [], 'output': []}
        while (machine.execute_instruction()):
            pass
        self.assertEqual(machine.memory[0],3500)

    def test_2(self):
        prog = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0"
        program = [int(s) for s in prog.split(",")]
        program[1] = 12
        program[2] = 2
        machine = Machine()
        machine.memory = program.copy()
        machine.counter = 0
        machine.io = {'input': [], 'output': []}
        while (machine.execute_instruction()):
            pass
        self.assertEqual(machine.memory[0],3085697)

    def test_3(self):
        prog = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
        program = [int(s) for s in prog.split(",")]
        machine = Machine()
        machine.memory = program.copy()
        machine.counter = 0
        machine.io = {'input': [], 'output': []}
        while (machine.execute_instruction()):
            pass
        self.assertEqual(prog,",".join([str(o) for o in machine.io['output']]))

    def test_4(self):
        prog = "104,1125899906842624,99"
        program = [int(s) for s in prog.split(",")]
        machine = Machine()
        machine.memory = program.copy()
        machine.counter = 0
        machine.io = {'input': [], 'output': []}
        while (machine.execute_instruction()):
            pass
        self.assertEqual(machine.io['output'][0],1125899906842624)

    def test_5(self):
        prog = "109,1,203,11,209,8,204,1,99,10,0,42,0"
        program = [int(s) for s in prog.split(",")]
        machine = Machine()
        machine.memory = program.copy()
        machine.counter = 0
        machine.io = {'input': [77], 'output': []}
        while (machine.execute_instruction()):
            pass
        self.assertEqual(machine.io['output'][0],77)

        
                
# Steps to increment for each code
def debug(arg):
    #pass
    print(arg)

class Machine:

    def debug(self,arg):
        if self.trace:
            print(arg)

    def dump(self):
        self.debug(self.memory)
        self.debug("pc: {}".format(self.counter))
        self.debug("rb: {}".format(self.base))
    
    def __init__(self):
        # Memory. Array of ints
        self.memory = []
        # Program counter
        self.counter = 0
        # Relative base for offsetting some instructions
        self.base = 0
        # Debugging info
        self.trace = True
        # Input/output
        self.io = {'input': [], 'output': []}


    # Haven't actually used these, just explicit setting. 
    def set_counter(self,c):
        self.counter = c

    def set_memory(self,m):
        self.memory = m
        
    def set_base(self,b):
        self.base = b

    def set_io(self,i):
        self.io = i

    # Memory read/write extends memory if necessary
    def read(self,location):
        while(location >= len(self.memory)):
              self.memory.append(0)
        return self.memory[location]

    def write(self,location,val):
        while(location >= len(self.memory)):
              self.memory.append(0)
        self.memory[location] = val

    # Decipher the code and modes
    def split_instruction(self,opcode):
        instruction = opcode % 100
        parameter_modes = int(opcode / 100)
        modes = []
        # Operands have no more that two referenceable arguments. Might be more!
        for i in range(0,3):
            modes.append(parameter_modes % 10)
            parameter_modes = int(parameter_modes / 10)
        return (instruction,modes)

    # Get the value given the counter, offset and access mode.
    def get_parameter(self,offset,mode,write=False):
        val = self.read(self.counter+offset)
        if mode == POSITION:
            if write:
                return val
            else:
                return self.read(val)
        elif mode == IMMEDIATE:
            return val
        elif mode == RELATIVE:
            if write:
                return self.base + val
            else:
                return self.read(self.base + val)
    
    # Execute the instruction according to the given state Lot of
    # duplication here. Could be much better! We should really be able
    # to do something general that counts arguments, but would also
    # need tohandle the read/write nature.
    def execute_instruction(self):
        opcode = self.read(self.counter)

        increment = True
        (instruction,modes) = self.split_instruction(opcode)
        if instruction == HALT:
            return False
    
        if instruction == ADD or instruction == MULTIPLY or instruction == LESS_THAN or instruction == EQUALS:
            arg1 = self.get_parameter(1,modes[0])
            arg2 = self.get_parameter(2,modes[1])
            arg3 = self.get_parameter(3,modes[2],write=True)

            if instruction == ADD:
                self.write(arg3,arg1 + arg2)
            if instruction == MULTIPLY:
                self.write(arg3,arg1 * arg2)
            if instruction == LESS_THAN:
                if arg1 < arg2:
                    self.write(arg3,1)
                else:
                    self.write(arg3,0)
            if instruction == EQUALS:
                if arg1 == arg2:
                    self.write(arg3,1)
                else:
                    self.write(arg3,0)

        if instruction == WRITE:
            arg1 = self.get_parameter(1,modes[0],write=True)
            arg2 = self.io['input'][0]

            # Take the first input value
            self.write(arg1,arg2)
            # Pop the stack
            self.io['input'] = self.io['input'][1:]

        if instruction == ADJUST:
            arg1 = self.get_parameter(1,modes[0])
            self.base = self.base + arg1
                    
        if instruction == OUTPUT:
            arg1 = self.get_parameter(1,modes[0])
            self.io['output'].append(arg1)

        if instruction == JUMP_TRUE or instruction == JUMP_FALSE:
            arg1 = self.get_parameter(1,modes[0])
            arg2 = self.get_parameter(2,modes[1])
            
            if instruction == JUMP_TRUE:
                if arg1 != 0:
                    self.counter = arg2
                    increment = False
            if instruction == JUMP_FALSE:
                if arg1 == 0:
                    self.counter = arg2
                    increment = False

        if increment:
            self.counter = self.counter + LANG[instruction]['args'] + 1
        return True

if __name__=='__main__':
    unittest.main()
