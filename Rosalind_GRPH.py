# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Using Biopython to parse multifasta, define n=3

# Check every suffix (3mer) from each sequence and check for matching prefixes (3mer) in every other sequence.

# Then, get ID that match.

from Bio import SeqIO
data = "./rosalind_grph.txt"
n = 3

seq_name, seq_string = [], []
with open (data,'r') as fa:
    for seq_record  in SeqIO.parse(fa,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))

for i in range(len(seq_string)):
    for j in range(len(seq_string)):
        if i != j:
            if seq_string[i][-n:] == seq_string[j][:n]:
                print(seq_name[i], seq_name[j])
