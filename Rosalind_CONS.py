# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Numpy package will be very useful to store each of the DNA strings as a row object in an array. 

# Then just count the number of each nucleotide at each position and use this to create another "matrix" for the final profile.

from Bio import SeqIO
from collections import Counter
import numpy as np

sequence_array = np.array([record.seq for record in SeqIO.parse("rosalind_cons.txt","fasta")])
counters = [Counter(column) for column in sequence_array.T]
profile_matrix = np.array([[counter.get(char,0) for char in "ACGT"] for counter in counters])
print("".join([counter.most_common(1)[0][0] for counter in counters]))

print(*(f"{nt}: {' '.join([str(n) for n in profile_matrix.T[i]])}" for i,nt in enumerate("ACGT")),sep='\n')
