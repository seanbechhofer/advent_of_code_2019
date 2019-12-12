import sys
import unittest


INPUT = """<x=-3, y=15, z=-11>
<x=3, y=13, z=-19>
<x=-13, y=18, z=-2>
<x=6, y=0, z=-1>"""

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertEqual(calculate(state("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""),10),179)

    def test_two(self):
        self.assertEqual(calculate(state("""<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""),100),1940)


class Moons():

    def __init__(self,spec):
        self.moons = {}
        count = 0
        for line in spec.split("\n"):
            pieces = [p.strip() for p in line.strip()[1:-1].split(",")]
#            debug(pieces)
            x = int(pieces[0][2:])
            y = int(pieces[1][2:])
            z = int(pieces[2][2:])
            self.moons[count] = {
                'position': {
                    'x': x,
                    'y': y,
                    'z': z},
                'velocity': {
                    'x': 0,
                    'y': 0,
                    'z': 0},
                }
            count += 1

    def apply_gravity(self):
        for moon_key in range(0,len(self.moons)):
            for other_moon_key in range(moon_key+1,len(self.moons)):
#                debug("{} {}".format(moon_key,other_moon_key))
                moon = self.moons[moon_key]
                other_moon = self.moons[other_moon_key]
                for dimension in ['x','y','z']:
                    moon_position = moon['position'][dimension]
                    other_moon_position = other_moon['position'][dimension]
                    if moon_position < other_moon_position:
                        moon['velocity'][dimension] += 1
                        other_moon['velocity'][dimension] -= 1
                    if moon_position > other_moon_position:
                        moon['velocity'][dimension] -= 1
                        other_moon['velocity'][dimension] += 1

    def apply_velocity(self):
        for moon in self.moons.values():
            for dimension in ['x','y','z']:
                moon['position'][dimension] += moon['velocity'][dimension]

    def calculate_energy(self):
        energy = 0
        for moon in self.moons.values():
            potential = 0
            kinetic = 0
            for dimension in ['x','y','z']:
                potential += abs(moon['position'][dimension])
                kinetic += abs(moon['velocity'][dimension])
            energy += potential*kinetic
        return energy
    
    def do_step(self):
        self.apply_gravity()
        self.apply_velocity()
                    
def state(str):
    moons = Moons(str)
    return moons
    
        
def debug(arg):
    #pass
    print(arg)

def calculate(state,iterations):
    debug(state.moons)
    for x in range(0,iterations):
        state.do_step()
    debug(state.moons)
    return state.calculate_energy()

if __name__=='__main__':
#    unittest.main()
    result = calculate(state(INPUT),1000)
    print(result)
