import sys
import unittest

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertTrue(calculate(112233))
    def test_two(self):
        self.assertTrue(calculate(111122))
    def test_three(self):
        self.assertFalse(calculate(123444))
    def test_four(self):
        self.assertTrue(calculate(122389))
    def test_five(self):
        self.assertFalse(calculate(1223))
    def test_six(self):
        self.assertFalse(calculate(122398))
        
def debug(arg):
    #pass
    print(arg)

def calculate(password):
    pass_str = str(password)

    if len(pass_str) != 6:
        return False
    for i in range(0,5):
        if pass_str[i] > pass_str[i+1]:
            return False;

    double_present = False;

    i = 0
    while (i<5):
        j = i
        while (j <=5 and pass_str[j] == pass_str[i]):
            j += 1
        if ((j-i) == 2):
            double_present = True
            break
        i = j
    return double_present

if __name__=='__main__':
#    unittest.main()
    passwords = []
    for p in range(134564,585159):
        if calculate(p):
            passwords.append(p)
    print(len(passwords))
