
from migen import *

class Counter(Module):
    def __init__(self):
        self.sreset =Signal(1)
        self.enable =Signal(1)
        self.datain =Signal(1)
        self.dataout=Signal(8)

        count=Signal(8)
        
        self.sync+=[
            If(self.sreset==1,
               count.eq(0)
            )  
            .Elif(self.enable==1,
                  count.eq(count+self.datain)
            )
        ]

        self.comb+=[
            self.dataout.eq(count)
        ]
        
if __name__ == '__main__':
    dut = Counter()
    
    
    from migen.fhdl.verilog import convert
    convert(dut, name="counter").write("counter.v")
