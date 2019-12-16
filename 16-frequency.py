import sys
import unittest

INPUT = "59767332893712499303507927392492799842280949032647447943708128134759829623432979665638627748828769901459920331809324277257783559980682773005090812015194705678044494427656694450683470894204458322512685463108677297931475224644120088044241514984501801055776621459006306355191173838028818541852472766531691447716699929369254367590657434009446852446382913299030985023252085192396763168288943696868044543275244584834495762182333696287306000879305760028716584659188511036134905935090284404044065551054821920696749822628998776535580685208350672371545812292776910208462128008216282210434666822690603370151291219895209312686939242854295497457769408869210686246"


BASE = [0,1,0,-1]

class TestStuff(unittest.TestCase):
    def test_one(self):
        signal = "12345678"
        self.assertEqual(calculate(signal,BASE,1),"48226158")

    def test_two(self):
        signal = "12345678"
        self.assertEqual(calculate(signal,BASE,2),"34040438")

    def test_three(self):
        signal = "12345678"
        self.assertEqual(calculate(signal,BASE,3),"03415518")

    def test_four(self):
        signal = "12345678"
        self.assertEqual(calculate(signal,BASE,4),"01029498")

    def test_five(self):
        signal = "80871224585914546619083218645595"
        self.assertEqual(calculate(signal,BASE,100)[:8],"24176176")

    def test_six(self):
        signal = "19617804207202209144916044189917"
        self.assertEqual(calculate(signal,BASE,100)[:8],"73745418")
        
    def test_seven(self):
        signal = "69317163492948606335995924319873"
        self.assertEqual(calculate(signal,BASE,100)[:8],"52432133")
        

def multiply_base(base,index):
    result = []
    for v in base:
        for i in range(0,index):
            result.append(v)
    return result

def debug(arg):
    #pass
    print(arg)

def iterate(signal,base_pattern):
    result = ""
    for i in range(0,len(signal)):
        pattern = multiply_base(base_pattern,i+1)
        repeated_pattern = pattern[1:]
        while len(repeated_pattern) < len(signal):
            repeated_pattern = repeated_pattern + pattern

        val_at_i = 0
        for j in range(0,len(signal)):
            val_at_i = val_at_i + (int(signal[j]) * repeated_pattern[j])
        val_at_i = abs(val_at_i) % 10
        result = result + str(val_at_i)
    return result

def calculate(signal,base,iterations):
    result = signal
    for i in range(0,iterations):
        debug(i)
        result = iterate(result,base)
    return result
        
if __name__=='__main__':
#    unittest.main()
    print(calculate(INPUT,BASE,100)[:8])
