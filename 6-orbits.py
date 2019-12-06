import sys
import unittest

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertEqual(calculate(["COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L"]),42)

def debug(arg):
    #pass
    print(arg)


def calculate(lines):
#    graph = {}
    reverse = {}
    for line in lines:
        planets = line.split(")")
        inner = planets[0].strip()
        outer = planets[1].strip()
        if outer in reverse:
            debug("Duplicate")
        reverse[outer] = inner
#        reverse[outer].append(inner)
#    debug(graph)
#    debug(reverse)
    count = 0
    for x in reverse.keys():
#        debug("x: {}".format(x))
        y = x
        while (y in reverse):
#            debug("y: {}".format(y))
            y = reverse[y]
            count += 1
    return count
        
if __name__=='__main__':
#    unittest.main()
    lines = []
    line = sys.stdin.readline()
    while line:
        lines.append(line)
        line = sys.stdin.readline()
    result = calculate(lines)
    print(result)
