# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Declare parameters and just multiply the number of permutations

# Do mod 1000000 and remember that the number of permutations of zero objects is 1 (only 1 arrangement)

n, k, r = 86, 9, 1
for i in range(n-k+1,n+1): r*=i

print(r%1000000)


