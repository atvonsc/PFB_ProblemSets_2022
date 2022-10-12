#!/usr/bin/env python3
import math
import sys

#if else for seq
output1 = [] # define variable for the output list to keep on one line via append fxn
seq = 'ATGGTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
start_codon = sys.argv[1]
stop_codon = sys.argv[2]
if sys.argv[1] in seq: #does seq have start?
  output1.append('Sequence contains start codon')
  if sys.argv[2] in seq: #does seq also have stop?
    output1.append('Sequence also contains stop codon')
  else:
    output1.append('Sequence does not contain stop codon') #start, but no stop
elif sys.argv[2] in seq:
  output1.append('Sequence contains only stop codon') #stop but no start
else:
  output1.append('Sequence does not contain start or stop codon') #no start or stop

num = int(sys.argv[3])
output2 = []
if num > 0: #number positive or neg
	output2.append(str(num) + ' is positive')
elif num < 0:
  output2.append(str(num) + ' is negative')  
if num < 50: #number in relation to 50
  output2.append(',less than 50')
elif num > 50:
  output2.append(', greater than 50')
if (num % 2) == 0: #number odd or even
  output2.append(',even')
elif (num % 2) != 0:
  output2.append(',odd')      
if (num % 3) == 0:
  output2.append('and divisible by 3') #number divisible by 3
else:
  output2.append('and not divisible 3')
print("; ".join(output1))
print("; ".join(output2))
