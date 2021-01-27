# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Read input as single-line array of characters, define the reverse complement

# Loop for all substrings and then check if palindrome

with open('../rosalind_revp.txt', 'r') as file:
    s = ''.join(x.strip() for x in file.readlines()[1:])
dic = {'G':'C','C':'G','A':'T','T':'A'}
for i in range(len(s)-3):
    for j in range(min(len(s), i+12), i+3, -1):
        current = s[i:j]
        revcomp = ''.join(dic[x] for x in current)[::-1]
        if current == revcomp:
            print(i+1, j-i)
