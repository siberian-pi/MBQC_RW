# MBQC_RW

Implementatin of rewritting rules for Measurement-Based-Quantum-Computation(MBQC).  Based on the paper *Parallelizing quantum circuits, Anne Broadbent, Elham Kashefi, 2002, TCS*.

## 1.General description
Given a sequence of gate description of a quantum circuit, the `MBQCRewriting(circuit,n)` return the corresponding MBQC pattern, which is in the standerd form. Notice that the output pattern haven't been signal shifting yet.

## 2.Detailed information
### 2.1 Function
`CircuitToPattern(circuit,n)`: Return the circuit pattern by a directly substitution.

`Standerdize(pattern)`: Transform a vild pattern to a standerd form

`MBQCRewriting(circuit,n)`: Use the previous two functions to output a standerd pattern.

### 2.2 Form of input and output
`MBQCRewriting(circuit,n)`: Take a sequence of circuit description and output the standard circuit pattern.
#### 2.2.1 Input
`n` is the number of qubits. `circuit` should be a list of gate description. The order of gates should be the executing order of the quantum circuit and the gates should be decomposed to the universal set, namely {CZ,J(a)}. Specifically, the description for gates should be one of the following 

- `['E',pos1,pos2] #A CZ gate on qubit pos1, pos2.`
- `['J',pos1,angle] #A J gate on qubit pos1, with corresponding angle.`

The position of qubits are numbered as 0,1,...  An example is a CNOT on qubit 0,1, which is depicted as followed

![A CNOT](https://github.com/siberian-pi/MBQC_RW/blob/master/pics/ACNOT.png)

The corresponding input is
```python
import math
a=2*math.pi
circuit=[['J',1,a],['E',0,1],['J',1,a]]
```
#### 2.2.2 Output

If we let  `pattern=MBQCRewriting(circuit,n)`
Then pattern should be a list whose elements are one of the following 5 kinds

- `['N',pos] #auxiliary qubit preparation on qubit pos.`
- `['E',pos1,pos2] #CZ gate on qubit pos1, pos2.`
- `['M',pos,angle,[...,X dependency,...],[...,Y dependency,...]]`
- `['X',pos,dependency]`
- `['Z',pos,dependency]`

For example, `['X',2,0]` means an X correction on qubit 2, where correction depends on the measurement outcome of qubit 0.
The output, namely the standerd pattern, looks like

`[...,['X',i,j] or ['Z',h,g],...,['M',k,a,[s_1,...,s_l],[t_1,...,t_h]],...['E',q,w]...,[N,r]...]`


