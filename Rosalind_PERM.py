# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# A python library makes this problem really easy. Just import and use.
# Result will be saved to an output file

import itertools

n = 6
perm = list(itertools.permutations(range(1,n+1)))
f = open("Rosalind_PERM_Output.txt", "w")
f.write(str(len(perm)) + "\n")
for x in list(perm):
    f.write(str(x).strip("(").strip(")").replace(",", "") + "\n")
