# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Biopython motifs package makes this problem really easy. For more info on Biopython, check david-boo.github.io

from Bio import motifs
from Bio.Seq import Seq

with open('rosalind_subs.txt') as f:
    seq1,seq2= f.read().split()
f.close()

target_seq = Seq(seq1)
motif = motifs.create([Seq(seq2)])
for pos,seq in motif.instances.search(target_seq):
    print(str(pos+1),end = ' ')
