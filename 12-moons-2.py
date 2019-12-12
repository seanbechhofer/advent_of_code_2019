import sys
import unittest
import hashlib
import numpy as np
from functools import reduce

INPUT = """<x=-3, y=15, z=-11>
<x=3, y=13, z=-19>
<x=-13, y=18, z=-2>
<x=6, y=0, z=-1>"""

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertEqual(calculate("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""),2772)

    def test_two(self):
        self.assertEqual(calculate("""<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""),4686774924)


        
class Moons():

    def __init__(self,spec,index):
        self.moons = {}
        count = 0
        for line in spec.split("\n"):
            pieces = [p.strip() for p in line.strip()[1:-1].split(",")]
#            debug(pieces)
            w = int(pieces[index][2:])
            self.moons[count] = {
                'position': w,
                'velocity': 0}
            count += 1

    def apply_gravity(self):
        for moon_key in range(0,len(self.moons)):
            for other_moon_key in range(moon_key+1,len(self.moons)):
                moon = self.moons[moon_key]
                other_moon = self.moons[other_moon_key]
                moon_position = moon['position']
                other_moon_position = other_moon['position']
                if moon_position < other_moon_position:
                    moon['velocity'] += 1
                    other_moon['velocity'] -= 1
                if moon_position > other_moon_position:
                    moon['velocity'] -= 1
                    other_moon['velocity'] += 1

    def apply_velocity(self):
        for moon in self.moons.values():
            moon['position'] += moon['velocity']

    def do_step(self):
        self.apply_gravity()
        self.apply_velocity()

    def render(self):
        result = ""
        for moon in self.moons.values():
            result = result + "p:{}v:{}".format(moon['position'],moon['velocity'])
        return result
        
def state(str,index):
    moons = Moons(str,index)
    return moons
    
        
def debug(arg):
    #pass
    print(arg)

def calculate(input):
    fixed_points = {}
    for index in [0,1,2]:
        new_state = state(input,index)
        states = {}
        steps = 0
        debug(new_state.render())
        states[new_state.render()] = steps
        while (True):
            new_state.do_step()
            steps = steps + 1
            code = new_state.render()
            if code in states.keys():
                first = states[code]
                fixed_points[index] = steps - first
                break
    fps = list(fixed_points.values())
    result = np.lcm.reduce(fps)
    return result
            
if __name__=='__main__':
#    unittest.main()
    print(calculate(INPUT))
