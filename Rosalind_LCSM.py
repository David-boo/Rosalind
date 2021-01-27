# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Quite messy code but it works.

# Generate all possible substrings for the first string.

# Then trim this list by checking which don't occur in the second string, and repeat until no strings remain.

from Bio import SeqIO

f = open("./rosalind_lcsm.txt", "r")
seqs = SeqIO.parse(f, "fasta")
seqs = [str(s.seq) for s in seqs]

subs = [seqs[0][i:i + l] for l in range(1, len(seqs[0]) + 1) for i in range(0, len(seqs[0]) - l + 1)]
for seq in seqs[1:]:
    subs = [sub for sub in subs if sub in seq]
print(max(zip(map(len, subs), subs))[1])