# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 


# In this code I'll use SeqIO, the standard sequence input/output interface for BioPython. You can find more information about BioPython on david-boo.github.io, be sure to check it out. 

# Using Bio.SeqUtils package aswell, which contains a G+C content function that really simplifies this problem. 

# Importing both of them

from Bio import SeqIO
from Bio.SeqUtils import GC

# Opening the DNA strings, creating a GCcont and a GCsequence variable to print result later.

GCcont=0
GCseq=""
file=open("rosalind_GC.txt", "r")

# Small loop that checks the GC content of every sequence and stores the highest value + seq id.

for record in SeqIO.parse(file, "fasta"):
    if GCcont < GC(record.seq):
        GCcont = GC(record.seq)
        GCseq = record.id

# Printing answer on  % 
        print(GCseq,round(GCcont,2),"%")
