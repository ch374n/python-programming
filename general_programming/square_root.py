question : 

START 100 						
A 	DC 	10 							
	MOVER AREG, B 					
	MOVEM BREG, ='1'  				
	ADD	AREG, ='2'					
	SUB BREG, ='1'					
B 	EQU	A + 20					    
	LTORG							
	STORE	AREG,	NUM				
	MOVER	CREG,	LOOP			
	ADD	BREG, ='1'					
NUM	DS	5						    
LOOP DC 10							
	END								


machine code : 

100	 00	 00	 001
101	 04	 01  105			
102	 05  01  106		
103	 02  02  107		 	
104	 00  00	 108		
105  00  00  000	 	
106	 00  00  000
107	 00  00  000
108	 00  00  000		
109	 00  01  112		
114	 04  03  113				
115	 01  02	 114 
116	 00  00  000		
117  00  00  000
118  00  00  000


symbol table :						literal table : 		pool table:

symbol address	length      	literal 	address			literal no
A      100    	1				  ='1'		106				1
B 	   105   	1				  ='2'		107
NUM    116  	5				  ='1'		108
LOOP   117		1

MDT
1		M1 &N, &A1 =, &R = AREG
2		MOVEM	&R,	&N 	
3		SUB		&R,	&A1 
4		ADD 	&R,	&N 	
5		MEND
6		M2	&P,	&Q = B,	&OPR = DIV
7		MOVER	AREG, &P 
8		&OPR	AREG, &Q 
9		MOVEM	BREG, &P 


MNT
M1	
M2

MACRO
	M1 &N, &A1 =, &R = AREG
	MOVEM	&R,	&N 	
	SUB		&R,	&A1 
	ADD 	&R,	&N 	
MEND

MACRO
	M2	&P,	&Q = B,	&OPR = DIV
	MOVER	AREG, &P 
	&OPR	AREG, &Q 
	MOVEM	BREG, &P 
MEND

	START 100
	READ 	VAR
	M2	A, OPR = SUB
	ADD		AREG,	VAR
	LDA	CREG, BREG
	SUB	CREG, A
	M1	C,	R = BREG, A1 = A
A 	DS	1
VAR DC	2
C 	DS	3
	END


	START 100
	READ 	VAR
	MOVER AREG, A 
	DIV  AREG, B
	MOVEM BREG, A 
	ADD		AREG,	VAR
	LDA	CREG, BREG
	SUB	CREG, A
	MOVEM	BREG, C
	SUB	 BREG, A
	ADD  BREG, 
A 	DS	1
VAR DC	2
C 	DS	3
	END