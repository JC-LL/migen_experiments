
from migen import *

from logic_gates import *

class HalfAdder(Module):
    def __init__(self):
        self.i1=Signal(1)
        self.i2=Signal(1)
        self.sum=Signal(1)
        self.cout=Signal(1)

        g1 = And()
        g2 = Xor()
        self.submodules+=[g1,g2]

        self.comb+=[
            g1.i1.eq(self.i1),
            g1.i2.eq(self.i2),
            g2.i1.eq(self.i1),
            g2.i2.eq(self.i2),
            self.sum.eq(g2.o),
            self.cout.eq(g1.o),
        ]


if __name__ == '__main__':

    dut = HalfAdder()

    def testbench():
        test_vectors={
            #a,b   sum,cout
            (0,0) : (0,0),
            (0,1) : (1,0),
            (1,0) : (1,0),
            (1,1) : (0,1),
        }
        s="      |  actual  | expected |  status  "
        print(s)
        s="i2 i1 | sum cout | sum cout | sum cout "
        print(s)
        print("-"*len(s))
        errors=0
        for stim in test_vectors:
            i2,i1=stim
            expected=test_vectors[stim]
            yield dut.i1.eq(i1)
            yield dut.i2.eq(i2)
            yield
            sum=yield dut.sum
            cout=yield dut.cout
            expected_sum,expected_cout=expected
            if (sum==expected_sum):
                msg1="-"
            else:
                msg1="?"
                errors+=1
            if (cout==expected_cout):
                msg2="-"
            else:
                msg2="?"
                errors+=1

            print("% 2d % 2d | % 3d % 4d | % 3d % 4d | %3s %4s " % (i2,i1,sum,cout,expected_sum,expected_cout,msg1,msg2))
        print("#total errors : % d" % errors)

    run_simulation(dut, testbench(),vcd_name="ha.vcd")

# import os
# os.system("gtkwave fa.vcd")
