#MBQCRW

Implementatin of rewritting rules for Measurement-Based-Quantum-Computation(MBQC).  Based on the paper *Parallelizing quantum circuits, Anne Broadbent, Elham Kashefi, 2002, TCS*.

##General description
Given a sequence of gate description of a quantum circuit, the **MBQCRewriting(circuit,n)** return the corresponding MBQC pattern, which is in the standerd form. Notice that the pattern haven't be signal shifting yet.

##Function
**CircuitToPattern(circuit,n)**: Return the circuit pattern by a directly substitution.
**Standerdize(pattern)**: Transform a vild pattern to a standerd form
**MBQCRewriting(circuit,n)**: Use the previous two functions to output a standerd pattern.

##Description of INPUT and OUTPUT
**MBQCRewriting(circuit,n)** take a sequnce of circuit description and output the standerd circuit pattern. The circuit pattern should be a list of gate description. The order of gates should be the executing order of the quantum circuit and the gates should be decomposed to the universal set, namely {CZ,J(a)}. Specifically, the description for gate should be one of the following 
-(+*) ['E',pos1,pos2]  refer to a CZ gate on qubit pos1, pos2
-(+*) ['J',pos1,angle] refer to a J gate on qubit pos1, with corresponding angle

##General description
Given a sequence of gate description of a quantum circuit, the **MBQCRewriting(circuit,n)** return the corresponding MBQC pattern, which is in the standerd form. Notice that the pattern haven't be signal shifting yet.

##Function
**CircuitToPattern(circuit,n)**: Return the circuit pattern by a directly substi
tution.
**Standerdize(pattern)**: Transform a vild pattern to a standerd form
**MBQCRewriting(circuit,n)**: Use the previous two functions to output a standerd pattern.

##Description of INPUT and OUTPUT
**MBQCRewriting(circuit,n)** take a sequnce of circuit description and output the standerd circuit pattern. The circuit pattern should be a list of gate description. The order of gates should be the executing order of the quantum circuit and the gates should be decomposed to the universal set, namely {CZ,J(a)}. Specifically, the description for gate should be one of the following
-(+*) ['E',pos1,pos2]  refer to a CZ gate on qubit pos1, pos2
-(+*) ['J',pos1,angle] refer to a J gate on qubit pos1, with corresponding angle

The qubits are numbered as 0,1,... An example is a CNOT on qubit 0,1, which is depicted as followed



