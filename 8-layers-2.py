import sys
import unittest

BLACK = '0'
WHITE = '1'
TRANS = '2'

WIDTH = 25
HEIGHT = 6

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertEqual(calculate("0222112222120000",2,2),"01\n10\n")
        
def debug(arg):
    #pass
    print(arg)


def render(layer,width,height):
    for y in range(0,height):
        for x in range(0,width):
            pixel = layer[y*width + x]
            print(pixel,end='')
        print()    

def calculate(line,width,height):
    result = ""
    message = []
    for i in range(0,height):
        message.append(['.'] * width)
    
    layers = []
    layer_length =  width * height
    count = 0
    while len(line) > 0:
        layer = line[:layer_length]
        layers.append(layer)
        line = line[layer_length:]
        print(count)
        render(layer,width,height)
        print()
        count += 1
    layers.reverse()
    for l in layers:
        for h in range(0,height):
            for w in range(0,width):
                char = l[h*width + w]
#                debug("{}.{} Char: {}".format(h,w,char))
                if (char == TRANS):
                    pass
                elif (char == BLACK):
                    message[h][w] = ' '#"#'0'
                elif (char == WHITE):
                    message[h][w] = "\u2588"#' '
                else:
                    print("XXX: {}".format(char))
        
    for i in range(0,height):
        for j in range(0,width):
            result+= (message[i][j])
        result += "\n"
    return result

if __name__=='__main__':
#    unittest.main()
    line = sys.stdin.readline().strip()
    debug(len(line))
    print(calculate(line,25,6))
