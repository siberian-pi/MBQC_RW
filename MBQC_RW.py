"""
MBQC rewritting program

INPUT: [[,gate,],nqubit]
OUTPUT: MBQC pattern

"""
def CircuitToPattern(circuit,n):#[[,gate_info,],nqubit]
	new_qubit=n
	pattern=[]
	logic_pos=[]
	for i in range(n):
		logic_pos.append(i)
	for gate in circuit:
		if(gate[0]=='E'):#['E',i,j]
			pos1=gate[1]
			pos2=gate[2]
			pattern.insert(0,['E',logic_pos[pos1],logic_pos[pos2]])
		if(gate[0]=='J'):#['J',i,angle]
			pos=gate[1]
			angle=gate[2]
			j=new_qubit
			i=logic_pos[pos]
			pattern.insert(0,['N',j])
			pattern.insert(0,['E',i,j])
			new_qubit+=1
			logic_pos[pos]=j
			pattern.insert(0,['M',i,-angle,[],[]])#X,Z dependency for [],[], none
			pattern.insert(0,['X',j,i])#correction,j,s_i
	return pattern

def IsValid(circuit,n):
	#only ['E',i,j],['J',i,angle]
	#index in range(0,n)
	for gate in circuit:
		if(len(gate)!=3 or (gate[0]!='E' and gate[0]!='J')):
			print("gate_info incorrect: ", gate)
			return -1
		if(gate[0]=='E'):
			if(not(gate[1]>-1 and gate[1]<n and gate[2]>0 and gate[2]<n)):
				print("gate index out of range: ", gate)
				return -1
		if(gate[0]=='J'):
			if(not(gate[1]>-1 and gate[1]<n)):
				print("gate index out of range: ", gate)
				return -1
	return 1
def Find(info,pattern):#'N','E',M','X','Z' return index of the rightest one
	m=len(pattern)
	for i in range(m-1,-1,-1):
		gate=pattern[i]
		if(gate[0]==info):
			return i
	return -1

def Standerdize(pattern):
	info_list=['N','E','M']
	m=len(pattern)
	process_index=m#unprocessed pattern[:process_index]


	for info in info_list:
		index=Find(info,pattern[:process_index])
		while(index!=-1):#completed of this type
			
			gate_curr=pattern[index]

			if(info=='N'):
				for i in range(index+1,process_index,1):
					del pattern[i-1]
					pattern.insert(i,gate_curr)
				process_index-=1
			#print('N completed***',pattern)
			if(info=='E'):
				Epos1=gate_curr[1]
				Epos2=gate_curr[2]
				while(index<process_index-1):
					gate_exch=pattern[index+1]
					Xpos=gate_exch[1]
					Xden=gate_exch[2]					
					if(gate_exch[0]=='X' and (Epos1==Xpos or Epos2==Xpos)):
						if(Epos1==Xpos or Epos2==Xpos):#only Eij Xis need special processing
							if(Epos1==Xpos):
								i=Epos1
								j=Epos2
							else:
								i=Epos2
								j=Epos1
							del pattern[index]
							pattern.insert(index+1,['Z',j,Xden])
							pattern.insert(index+2,['E',i,j])
							process_index+=1 #add a Z dependency
							index+=2
					else:#else exchange two gate
						del pattern[index]
						pattern.insert(index+1,gate_curr)
						index+=1
				process_index-=1
                #print("E completed***",pattern)
			if(info=='M'):
				while(index<process_index-1):
				
					gate_curr=pattern[index]
					gate_exch=pattern[index+1]
					
					Mpos=gate_curr[1]
					Mangle=gate_curr[2]
					MXden=gate_curr[3]
					MZden=gate_curr[4]	
					
					pos=gate_exch[1]
					den=gate_exch[2]
					if(pos==Mpos):
						if(gate_exch[0]=='X'):
							MXden.append(den)
						if(gate_exch[0]=='Z'):
							MZden.append(den)
						del pattern[index]
						pattern.insert(index,['M',Mpos,Mangle,MXden,MZden])
						del pattern[index+1]
						process_index-=1
					else:
						del pattern[index]
						pattern.insert(index+1,gate_curr)
						index+=1
				process_index-=1
			index=Find(info,pattern[:process_index])
			#print(info,index)
			#print(pattern)
	return pattern

def MBQCRewriting(circuit,n):
    IsValid(circuit,n)
    pattern=CircuitToPattern(circuit,n)
    pattern=Standerdize(pattern)
    return pattern

