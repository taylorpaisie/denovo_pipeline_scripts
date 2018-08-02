#filtering out contigs less than 500 nucleotides long

import sys
from Bio import SeqIO

handle = open(sys.argv[1], 'rU')
contigs = SeqIO.parse(handle, 'fasta')

counter = 0

filtered_fasta = open(sys.argv[2], 'w')

good_contigs = []

for record in contigs:
    if len(record.seq) >= 500:
        good_contigs.append(record)
        counter += 1
SeqIO.write(good_contigs, filtered_fasta, 'fasta')
