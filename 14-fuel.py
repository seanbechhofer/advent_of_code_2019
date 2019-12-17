import sys
import unittest

INPUT = """4 ZDGD, 1 HTRQV => 3 VRKNQ
15 XKZQZ, 1 MWZQ => 4 LHWX
1 WVPKL => 2 HJLX
1 LFDGN => 7 DMPX
14 HJLX, 3 KGKVK, 1 XQSVS => 6 HGSM
8 FKQS, 8 MWVCW => 3 MVSK
2 HGZLR, 2 WVPKL, 29 VRKNQ => 2 MDKZ
1 RLGBD, 22 VWFV => 6 MSGJ
24 PHLTR, 2 MWVCW => 8 JZMS
5 XSJLQ, 2 PFTM => 1 NCRJ
3 QNBK => 8 LKWK
16 HGSM => 3 BKHV
138 ORE => 5 SBXDS
3 KGKVK => 8 MTCZW
1 MDKZ, 8 HGNB => 5 HLDW
9 BKHV, 5 WDVS, 1 HGSM => 4 PFTM
1 PFNM, 14 MVSK => 3 VQCQ
16 LTXF => 4 TSKNX
5 VQCQ, 16 NFSVL, 5 HJLX, 1 TSKNX, 16 DMPX, 1 MSGJ, 3 BKHV => 7 CTHPF
8 WVPKL, 5 LHWX => 4 KGKVK
2 HLDW, 21 KSCS, 4 MTCZW, 1 DMPX, 1 LKWK, 7 NGVH, 12 HJLX, 18 MVSK => 9 VLGFJ
195 ORE => 3 NTZKP
6 FKQS => 1 GMJRS
6 LSLR, 8 HJLX => 4 NFSVL
16 NTZKP, 3 ZDGD => 8 XKZQZ
20 HLDW, 1 WDVS, 6 KGKVK => 7 PFNM
9 LHWX, 2 HLDW, 2 JZMS => 4 QNBK
1 RLGBD, 8 CKSPZ => 7 WDVS
3 RLGBD => 9 LTXF
14 SBXDS, 1 NTZKP => 7 FZBGM
14 CKSPZ, 1 MWZQ, 4 RLGBD => 8 NGVH
1 FKQS => 1 QWVC
6 MWZQ => 4 PBWF
4 ZDGD, 5 WVPKL => 4 FLWK
5 HLDW, 6 FKQS, 35 VLGFJ, 20 MVSK, 13 QKVZ, 5 CTHPF => 1 FUEL
5 QWVC, 10 LFDGN => 5 CKSPZ
4 QWVC, 4 FKQS, 1 MWVCW => 9 VWFV
1 SBXDS => 2 XQSVS
160 ORE => 9 HGZLR
1 KGKVK, 3 HJLX, 2 HGNB => 8 KSCS
6 GMJRS => 9 PHLTR
1 LFDGN, 9 XQSVS, 37 PBWF => 3 LSLR
7 FZBGM, 4 FNJX => 7 KFHFS
4 MVSK, 1 NFSVL, 2 NCRJ, 24 BKHV, 5 RLGBD, 5 NGVH => 9 QKVZ
4 VWFV, 1 RLGBD => 3 CMZQF
102 ORE => 4 ZDGD
1 SBXDS => 2 WVPKL
2 HTRQV => 1 HGNB
2 KFHFS, 7 FLWK, 5 WVPKL => 9 FKQS
5 GMJRS, 10 LHWX => 4 RLGBD
8 BKHV, 8 CMZQF => 3 XSJLQ
2 XQSVS => 6 LFDGN
103 ORE => 5 HTRQV
28 HGZLR, 2 ZDGD => 5 FNJX
6 VRKNQ, 1 XKZQZ => 7 MWZQ
10 ZDGD => 8 MWVCW"""

class TestStuff(unittest.TestCase):
    def test_one(self):
        self.assertEqual(calculate("""10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""),31)

    def test_two(self):
        self.assertEqual(calculate("""9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""),165)

    def test_three(self):
        self.assertEqual(calculate("""157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""),13312)

    def test_four(self):
        self.assertEqual(calculate("""2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""),180697)

    def test_five(self):
        self.assertEqual(calculate("""171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX"""),2210736)

class RuleElement():
    def __init__(self,n,element):
        self.n = n
        self.element = element

    def __str__(self):
        return "{} {}".format(self.n,self.element)
    
class Rule():
    def __init__(self,head,body):
        self.head = head
        self.body = body

    def __str__(self):
        return "{} => {}".format(", ".join([str(b) for b in self.body]),self.head)

class Rules():
    
    def __init__(self,spec):
        self.rules = []
        for line in spec.split("\n"):
            pieces = line.split(" => ")
            (n,element) = pieces[1].split(" ")
            head = RuleElement(int(n),element)
            body = []
            for lh in pieces[0].split(", "):
                (n,element) = lh.split(" ")
                body.append(RuleElement(int(n),element))
            self.rules.append(Rule(head,body))

    def __str__(self):
        return "\n".join(["============"] + [str(r) for r in self.rules] + ["============"])

        
def debug(arg):
    #pass
    print(arg)

def calculate(spec):
    rules = Rules(spec)
    print(rules)
    return 0

if __name__=='__main__':
    unittest.main()
