
from migen import *

from half_adder import *

class FullAdder(Module):
    def __init__(self):
        self.i1=Signal(1)
        self.i2=Signal(1)
        self.cin=Signal(1)
        self.sum=Signal(1)
        self.cout=Signal(1)

        ha1=HalfAdder()
        ha2=HalfAdder()

        self.submodules+=[ha1,ha2]

        self.comb+=[
            ha1.i1.eq(self.i1),
            ha1.i2.eq(self.i2),

            ha2.i1.eq(self.cin),
            ha2.i2.eq(ha1.sum),

            self.sum.eq(ha2.sum),
            self.cout.eq(ha1.cout | ha2.cout)
        ]
if __name__ == '__main__':
    dut = FullAdder()

    def testbench():
        test_vectors={
            #a,b,cin  sum,cout
            (0,0,0) : (0,0),
            (0,0,1) : (1,0),
            (0,1,0) : (1,0),
            (0,1,1) : (0,1),
            (1,0,0) : (1,0),
            (1,0,1) : (0,1),
            (1,1,0) : (0,1),
            (1,1,1) : (1,1),
        }
        s="          |  actual  | expected |  status  "
        print(s)
        s="i2 i1 cin | sum cout | sum cout | sum cout "
        print(s)
        print("-"*len(s))
        errors=0
        for stim in test_vectors:
            i2,i1,cin=stim
            expected=test_vectors[stim]
            yield dut.i1.eq(i1)
            yield dut.i2.eq(i2)
            yield dut.cin.eq(cin)
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

            print("% 2d % 2d % 3d | % 3d % 4d | % 3d % 4d | %3s %4s " % (i2,i1,cin,sum,cout,expected_sum,expected_cout,msg1,msg2))
        print("#total errors : % d" % errors)


    run_simulation(dut, testbench(),vcd_name="fa.vcd")
    
    from migen.fhdl.verilog import convert
    convert(FullAdder(), name="full_adder").write("full_adder.v")
# import os
# os.system("gtkwave fa.vcd")
