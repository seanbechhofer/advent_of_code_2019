import sys
import unittest

def debug(arg):
    #pass
    print(arg)

def calculate(lines):
    layer_length = 25 * 6
    index = 0
    minimum = 25*6 + 1
    result = 0
    while index < len(lines):
        layer = lines[:layer_length]
        debug(len(layer))
        debug(layer.count('0'))
        debug(layer.count('1'))
        debug(layer.count('2'))
        zeros = layer.count('0')
        if zeros < minimum:
            result = layer.count('1') * layer.count('2')
            minimum = zeros
        lines = lines[layer_length:]
    debug(minimum)
    return result

if __name__=='__main__':
    line = sys.stdin.readline().strip()
    debug(len(line))
    print(calculate(line))
