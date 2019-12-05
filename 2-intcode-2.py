import sys
import math


ADD = 1
MULTIPLY = 2
HALT = 99

def debug(arg):
    pass
    #print arg

def execute_instruction(data,location):
    instruction = data[location]
    if instruction == HALT:
        return False
    arg1 = data[data[location+1]]
    arg2 = data[data[location+2]]

    if instruction == ADD:
        data[data[location+3]] = arg1 + arg2
    if instruction == MULTIPLY:
        data[data[location+3]] = arg1 * arg2
    return True
    
if __name__=='__main__':
    prog = [int(s) for s in sys.stdin.readline().strip().split(",")]
    for noun in range(0,100):
        for verb in range(0,100):
            test_prog = prog.copy()
            test_prog[1] = noun
            test_prog[2] = verb
            counter = 0
            while (execute_instruction(test_prog,counter)):
                counter += 4
            if (test_prog[0] == 19690720):
                print("noun: {}, verb: {}, result: {}".format(noun,verb,test_prog[0]))
                print("submit: {}".format(100*noun + verb))
