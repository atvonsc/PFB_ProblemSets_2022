#!/usr/bin/env python

import os, sys



## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]
    
def seq_list_from_fastq_file(fastq_filename):

  seq_list = list()

    ## begin your code

  line_counter = 0 # set line counter to zer
  with open(fastq_filename, 'r') as fastq_read: #open and read sequence file
    for line in fastq_read:
      line_counter += 1 # read lines iteratively
      if line_counter % 4 == 2: #use the modulus fxn to give the line location you want, type the number of the line you want (2nd line is sequence in fastq files, so 2) then modulus (%) then the total lines for the entry (4 total lines in fastq) into python and get return. The return = 2, so you now if you define the if statement around only when counter % 4 = 2, you will always pull from the second line in the entry
        seq_list.append(line) # fill in list
                



    
    
    ## end your code

    return seq_list



def main():

    progname = sys.argv[0]
    
    usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)
    
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    num_seqs_show = int(sys.argv[2])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    print(seq_list[0:num_seqs_show])

    sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
    main()
    
