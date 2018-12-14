"""
Test case. Results are verified by hand.

#circuit to pattern, test case 1

circuit=[['J',1,a],['E',0,1],['J',1,a],['J',0,a],['E',0,1],['J',0,a]]
n=2
pattern=CircuitToPattern(circuit,n)
pattern=Standerdize(pattern)

#standerdize case 1
pattern=[['E',1,2],['X',1,2]]
pattern=Standerdize(pattern)
print(pattern)


#standerdize case 2
pattern=[['M',1,0.5,[],[]],['Z',1,3]]
pattern=Standerdize(pattern)

#circuit to pattern, test case 2
circuit=[['J',1,a],['E',0,1],['J',2,a],['J',1,a],['E',1,2],['J',1,a],['J',2,a],['E',1,2],['E',0,1],['J',1,a]]
pattern=CircuitToPattern(circuit,3)#right
pattern=Standerdize(pattern)#right see E -1


circuit=[['J',1,a],['E',0,1],['J',0,a],['J',1,a],['E',0,1],['J',0,a]]
pattern=CircuitToPattern(circuit,2)
pattern=Standerdize(pattern)
"""
import math
from MBQC_RW import *

a=2*math.pi
circuit=[['J',1,a],['E',0,1],['J',1,a],['J',0,a],['E',0,1],['J',0,a]]
n=2
pattern=MBQCRewriting(circuit,n)

print(pattern)