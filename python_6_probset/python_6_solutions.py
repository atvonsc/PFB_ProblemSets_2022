#!/usr/bin/python3

import sys
import math
import statistics

#avs 10/14/22 python problem set 6 solutions

mySet = set('ATGTGGG') # prints as unique characters in set
mySet2 = {'ATGTGGG'} # prints whole set as a string

print(mySet)
print(mySet2)

setA = {'3','14','15','9','26','5','35','9'}
setB = {'60','22','14','0','9'}

#find intersection, chars in both A and B
print(setA & setB)

#find difference, chars unique to A and B
print(setA - setB)

#find the union, all chars in A and B
print(setA|setB)

#find the symmetrical difference, chars unique to both A and B
print(setA^setB)

#If you create a set using a DNA sequence, what will you get back?

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC'

#Nucleotide Composition. Write a script that: determines the unique characters in this sequence

nt_count = {} #create empty dictionary

uniq = set(dna) #get unique chars in dna

print('Unique nts in dna:', uniq) #print unique chars

for nt in uniq: 
  count = dna.count(nt) # count the nts in dna iteratively
  nt_count[nt] = count #add the count to the empty dictionary

print('nt count:', nt_count) #print dictionary

#determine GC content

GC = (nt_count['G'] + nt_count['C']) / len(dna)

print(GC * 100,'%')

#Write a script to do the following to Python_06.txt

#Open and read the contents.

with open('/Users/student/pfb2022/files/Python_06.txt', 'r') as python_06: # use absolute path, can find in unix via find. -name "filename.ext", then go to file and use pwd to get full path

  for line in python_06:
    line = line.upper().rstrip()
    print(line)

# write to a new file
with open('/Users/student/pfb2022/files/Python_06.txt', 'r') as lyrics_read, open('Python_06_uc.txt', 'w') as lyrics_write:
    for line in  lyrics_read:
        line = line.upper().rstrip()
        lyrics_write.write(str(line))

print('Wrote running.on.a.dream.txt')

genes = {}

with open('/Users/student/pfb2022/files/Python_06.seq.txt', 'r') as seq_read:
    for lines in seq_read:
        lines = lines.rstrip()
        gene,seq = lines.split()
        genes[gene] = seq

genes_rc = {}

#get reverse complement
for seq in genes:
    dna = genes[seq]
    t = dna.replace('T', 'a')
    a = dna.replace('A', 't')
    c = dna.replace('C', 'g')
    g = dna.replace('G', 'c')

    compdna = dna.upper()
    rcdna = compdna[::-1]

    genes_rc[seq] = rcdna

#write new file with rc
with open('Python_06.fastq', 'w') as seq_write:
  for seq in genes_rc:
      print('>'+gene+'\n'+genes_rc[seq]+'\n')
      seq_write.write(str(('>'+gene+'\n'+genes_rc[seq]+'\n')))

print('Wrote python_06.fastq, these sequences are in the reverse complement')

line_c = 0 #have to define accounting ints for the counts occuring below
char_c = 0

#count lines, chars and avg len
with open('/Users/student/pfb2022/files/Python_06.fastq', 'r') as rc_read:
    for lines1 in rc_read:
        lines1 = lines1.rstrip()
        line_c += 1 #keeps total tally through each iteration
        char_c += len(lines1) #keeps char tally as it iterates through each line
        
avg_len = char_c / line_c # avg needs to be done at the end of the loop, so needs to move back outward

print(f'''Line count: {line_c}
        Character count: {char_c}
        Average Length: {avg_len}''')

# Write your first FASTA parser script. This is a script that reads in a FASTA file and stores each FASTA record separately for easy access for future analysis.

fasta_filename = sys.argv[1] #read file via command line

fasta_fileobj = open(fasta_filename, 'r') #create file obj from the file of interest

# define strings to put into the file obj (need empty dictionary to have key pairs)
seq_name = ''
seq_desc = ''
seq_str = ''
fasta_dict = {}

for lines_fas in fasta_fileobj:
    lines_fas = lines_fas.rstrip()

    if line_fas.startswith('>'):
        line_fas = line_fas.lstrip('>')
        seq_info = line_fas.split(maxsplit=1)

        if len(seq_info) > 1:
            seq_desc = seq_info[1]

        else:
            seq_desc = ''

        if len(seq_str) > 0:
            fasta_dict[seq_name] = seq_str
            seq_str = ''

        seq_name = seq_info[0]

        if len(seq_info) > 1:
            seq_desc = seq_info[1]
        else:
            seq_desc = ''

    else:
        seq_str += line_fas

if len(seq_str        

