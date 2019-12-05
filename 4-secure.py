import sys
import unittest

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertTrue(calculate(111111))
    def test_two(self):
        self.assertFalse(calculate(223450))
    def test_three(self):
        self.assertFalse(calculate(123789))
    def test_four(self):
        self.assertTrue(calculate(122389))
    def test_five(self):
        self.assertFalse(calculate(1223))
    def test_six(self):
        self.assertFalse(calculate(122398))
        
def debug(arg):
    pass
    #print arg

def calculate(password):
    pass_str = str(password)
    if len(pass_str) != 6:
        return False
    for i in range(0,5):
        if pass_str[i] > pass_str[i+1]:
            return False;
    double_present = False;
    for i in range(0,5):
        if pass_str[i] == pass_str[i+1]:
            double_present = True
            break
    return double_present

if __name__=='__main__':
#    unittest.main()
    passwords = []
    for p in range(134564,585159):
        if calculate(p):
            passwords.append(p)
    print(len(passwords))
