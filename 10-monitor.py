import sys
import unittest
import math

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertEqual(calculate([".#..#",
                                ".....",
                                "#####",
                                "....#",
                                "...##"]),8)
    def test_two(self):
        self.assertEqual(calculate(["......#.#.",
                                        "#..#.#....",
                                        "..#######.",
                                        ".#.#.###..",
                                        ".#..#.....",
                                        "..#....#.#",
                                        "#..#....#.",
                                        ".##.#..###",
                                        "##...#..#.",
                                        ".#....####"]),33)
    def test_three(self):
        self.assertEqual(calculate([".#..##.###...#######",
                                        "##.############..##.",
                                        ".#.######.########.#",
                                        ".###.#######.####.#.",
                                        "#####.##.#.##.###.##",
                                        "..#####..#.#########",
                                        "####################",
                                        "#.####....###.#.#.##",
                                        "##.#################",
                                        "#####.##.###..####..",
                                        "..######..##.#######",
                                        "####.##.####...##..#",
                                        ".#####..#.######.###",
                                        "##...#.##########...",
                                        "#.##########.#######",
                                        ".####.#.###.###.#.##",
                                        "....##.##.###..#####",
                                        ".#.#.###########.###",
                                        "#.#.#.#####.####.###",
                                        "###.##.####.##.#..##"]),210)

def debug(arg):
    #pass
    print(arg)

def calculate(lines):
    points = []
    row = 0
    for line in lines:
        col = 0
        for ch in line:
            if ch == "#":
                points.append((row,col))
            col += 1
        row += 1
    maximum = 0
    for potential in points:
        angles = set()
        for point in points:
            if point != potential:
                x_delta = point[0] - potential[0]
                y_delta = point[1] - potential[1]
                angle = math.atan2(y_delta,x_delta)
                angles.add(angle)
        if len(angles) > maximum:
            maximum = len(angles)
    return maximum

if __name__=='__main__':
#    unittest.main()
    lines = []
    line = sys.stdin.readline()
    while line:
        lines.append(line)
        line = sys.stdin.readline()
    result = calculate(lines)
    print(result)
