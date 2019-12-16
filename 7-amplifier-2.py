import sys
import unittest
import itertools
from intcode_threaded import Machine
from queue import Queue
import threading
import os
import time

class TestStuff(unittest.TestCase):
    def test_one(self):
        source =  "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
        program = [int(s) for s in source.split(",")]
        self.assertEqual(run_program(program,[9,8,7,6,5]),139629729)
        
    def test_two(self):
         source = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
         program = [int(s) for s in source.split(",")]
         self.assertEqual(run_program(program,[9,7,8,5,6]),18216)

            
# Steps to increment for each code
def debug(arg):
    #pass
    print(arg)

# Connect the machines up

def connect(machines,box):
    machineCount = len(machines)
    running = True
    while(running):
        for index in range(0,machineCount-1):
            if not machines[index].io['output'].empty():
                output = machines[index].io['output'].get()
                machines[index].io['output'].task_done()
#                debug("Passing {} from {} to {}".format(output,index,index+1))
                machines[index+1].io['input'].put(output)
        if not machines[machineCount-1].io['output'].empty():
            output = machines[machineCount-1].io['output'].get()
            machines[machineCount-1].io['output'].task_done()
#            debug("Passing {} from {} to {}".format(output,machineCount-1,0))
#            debug("Putting {} in the box".format(output))
            box['contents'] = output
            machines[0].io['input'].put(output)
            if machines[0].halted:
                running = False
    
def run_program(program,input_values):
    debug(input_values)
    machines = []
    # Set up five machines and set them running
    for i in range(0,4):
        machine = Machine()
        machine.memory = program.copy()
        machine.counter = 0
        machine.io = {'input': Queue(), 'output': Queue()}
        machine.io['input'].put(input_values[i])
        machines.append(machine)
        t = threading.Thread(target=machine.run)
        t.start()
    # Fourth machine. We need to wait for this one to finish.
    last_machine = Machine()
    last_machine.memory = program.copy()
    last_machine.counter = 0
    last_machine.io = {'input': Queue(), 'output': Queue()}
    last_machine.io['input'].put(input_values[-1])
    machines.append(last_machine)
    thread = threading.Thread(target=last_machine.run)
    thread.start()
        
    # Now connect the machines. 
    box = {'contents': None}
    connect_thread = threading.Thread(target=connect,args=(machines,box))
    connect_thread.setDaemon(True)
    connect_thread.start()
#    debug(connect_thread)
    machines[0].io['input'].put(0)
    # Wait for the last machine to finish.
    thread.join()
    # Wait for the communication thread to finish
    connect_thread.join()
    
    while(not last_machine.halted):
        pass
    
#    debug("Returning")
    return box['contents']

def calculate(program):
    values = list(range(5,10))
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
    source = "3,8,1001,8,10,8,105,1,0,0,21,42,63,76,101,114,195,276,357,438,99999,3,9,101,2,9,9,102,5,9,9,1001,9,3,9,1002,9,5,9,4,9,99,3,9,101,4,9,9,102,5,9,9,1001,9,5,9,102,2,9,9,4,9,99,3,9,1001,9,3,9,1002,9,5,9,4,9,99,3,9,1002,9,2,9,101,5,9,9,102,3,9,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,3,9,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99"
    program = [int(s) for s in source.split(",")]
    print(calculate(program))
