# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Generate table to produce a mapping from protein to a number of possible codons.

# Iterate across the protein string. For each character in the string, we multiply by the value found in the table

# Finally reduce by taking the result mod 10^6.

aa = open('rosalind_mrna.txt', 'r').read().strip()
dic = {'A': 4, 'R': 6, 'N': 2, 'D': 2, 'C': 2, 'Q': 2, 'E': 2, 'G': 4, 'H': 2, 'I': 3,
       'L': 6, 'K': 2, 'M': 1, 'F': 2, 'P': 4, 'S': 6, 'T': 4, 'W': 1, 'Y': 2, 'V': 4}
n = 3
for i in aa:
    n *= dic[i]
    # We multiply by 3 for the stop codon
print(n % 1000000)
