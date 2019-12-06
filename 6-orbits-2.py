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
                                    "K)L",
                                    "K)YOU",
                                    "I)SAN"]),4)

def debug(arg):
    #pass
    print(arg)


def path(graph,node):
    path = []
    path.append(node)
    current = node
    while node in graph:
        path.append(graph[node])
        node = graph[node]
    return path

def calculate(lines):
    graph = {}
    for line in lines:
        planets = line.split(")")
        inner = planets[0].strip()
        outer = planets[1].strip()
        if outer in graph:
            debug("Duplicate")
        graph[outer] = inner
    # Hard coded
    santa = path(graph,"SAN")
    you = path(graph,"YOU")

    # Common points in the path
    common = set(santa).intersection(set(you))
    subgraph = graph.copy()

    # Grab subgraph of common points
    for k in graph:
        if k not in common:
            del subgraph[k]

    # Find the common point that isn't a value in the subgraph
    (meeting_point,) = common.difference(set(subgraph.values()))
    debug(meeting_point)
    # Hops is the length of the two paths to the meeting point minus 2. 
    hops = santa.index(meeting_point) + you.index(meeting_point) - 2
                                      
    return hops
        
if __name__=='__main__':
#    unittest.main()
    lines = []
    line = sys.stdin.readline().strip()
    while line:
        lines.append(line)
        line = sys.stdin.readline()
    result = calculate(lines)
    print(result)
