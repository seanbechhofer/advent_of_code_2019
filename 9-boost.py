import sys
import unittest
from intcode import Machine

# Steps to increment for each code
def debug(arg):
    #pass
    print(arg)

if __name__=='__main__':
#    unittest.main()
    program = [int(s) for s in sys.stdin.readline().strip().split(",")]
    machine = Machine()
    machine.memory = program.copy()
    machine.counter = 0
    machine.io = {'input': [1], 'output': []}
    while (machine.execute_instruction()):
        pass
    print(machine.io)
