
from migen import *

class And(Module):
    def __init__(self):
        self.i1=Signal(1)
        self.i2=Signal(1)
        self.o=Signal(1)
        self.comb+= self.o.eq(self.i1 & self.i2)

dut = And()

def testbench():
    test_vectors={
        (0,0)  : 0,
        (0,1)  : 0,
        (1,0)  : 0,
        (1,1)  : 1,
    }
    s="i2 i1  o | expected | status "
    print(s)
    print("-"*len(s))
    for stim in test_vectors:
        i2,i1,=stim
        expected=test_vectors[stim]
        yield dut.i1.eq(i1)
        yield dut.i2.eq(i2)
        yield
        result=yield dut.o
        if (result==expected):
            msg="ok"
        else:
            msg="nok"
        print("% 2d % 2d % 2d | % 8d | %s" % (i2,i1,result,expected,msg))


run_simulation(dut, testbench(),vcd_name="and.vcd")

import os
os.system("gtkwave and.vcd")
