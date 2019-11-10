
from migen import *

class And(Module):
    def __init__(self):
        self.i1=Signal(1)
        self.i2=Signal(1)
        self.o=Signal(1)
        self.comb+= self.o.eq(self.i1 & self.i2)

class Or(Module):
    def __init__(self):
        self.i1=Signal(1)
        self.i2=Signal(1)
        self.o=Signal(1)
        self.comb+= self.o.eq(self.i1 | self.i2)

class Xor(Module):
    def __init__(self):
        self.i1=Signal(1)
        self.i2=Signal(1)
        self.o=Signal(1)
        self.comb+= self.o.eq(self.i1 ^ self.i2)

class Not(Module):
    def __init__(self):
        self.i=Signal(1)
        self.o=Signal(1)
        self.com+=self.o.eq(~self.i)
