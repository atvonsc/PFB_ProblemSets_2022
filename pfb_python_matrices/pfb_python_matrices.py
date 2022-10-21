#!/usr/bin/env python3

import sys
import math

#Your goal this afternoon will be to write a script that reads each of the sets of data from either the SSEARCH or BLASTP outputs and produces a table with each of the scoring matrices as row, and the percent identity, alignment length, and E()-values for columns, for the top hit from each of the searches.

#To do this, you will need to:

#Download a set of SSEARCH or BLASTP results.

#Download from https://fasta.bioch.virginia.edu/mol_evol/data/ using the curl fxn in CLI

#Write a program that will take take an argument from the command line, which you can use to specify either rand5-200 or rand5-800, and concatenate it with a scoring matrix name (BL50, BP62, etc. for SSEARCH, BLOSUM62, BLOSUM80, etc. for BLASTP, so that you can open and each result file and associate the results with a scoring matrix.

file_name = sys.argv[1]
residue_count = sys.argv[2]
matrix_score = sys.argv[3]

this_data = {}
field_names = ['qseqid','sseqid','percid','alen','mismat','gaps','q_start','q_end','s_start','s_end','evalue','bits']

with open(file_name, 'r') as blastp_results:
    for line in blastp_results:
        line = line.rstrip()
        if not line.startswith('#'):
            this_data=dict(zip(field_names, line.split('\t')))
            #need to append 
    print(this_data)

#To parse the BLASTP tabular output file, you must:
#remove the newline character
#skip lines beginning with "#"
#use line.split('\t') to break each result line into its parts, which are: qseqid, sseqid, percid, alen, mismat, gaps, q_start, q_end, s_start, s_end, evalue, bits
#consider breaking the line up and saving the results to a dictionary with:
#this_data=dict(zip(field_names, line.split('\t')))
#As soon as you have a result line, save this_data, close the file, and move to the next result file.
#Save the results in a dictionary using the matrix name as the key, and then print out the values you want ('percid', 'alen', and 'evalue').
#Does the alignment length, percent identity, or evalue depend on the query sequence length?
#Compare the SSEARCH results with the BLAST results. Which program gives a better range of alignment lengths and percent identities?
