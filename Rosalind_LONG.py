# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Quite tricky solution. The best approach would be merging any 2 strings that overlap by more than 500 symbols

# After all these merges there'll be only one string left, our superstring

from Bio import SeqIO

with open("rosalind_long.txt", "r") as handle:
    lst,l = [],0
    for record in SeqIO.parse(handle, "fasta"):
        lst.append(str(record.seq))
        l+=len(str(record.seq))

mid = int(l/len(lst)//2)
for a in range(len(lst)):
    for sub in lst:
        for s in lst:
            if sub != s:
                for i in reversed(range(len(sub))):
                    if sub[:i] == s[-i:] and i >= mid-1:
                        lst.append(s+sub[i:])
                        if sub in lst:
                            lst.remove(sub)
                        if s in lst:
                            lst.remove(s)
print(max(lst,key=len))
