# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Intertools package makes this easier. Load characters and n and iterate using product to get n length

# Order answer before printing

import itertools

text = 'A B C D E F G H I J'
n=2

string = text.replace(' ','').strip('\n')
ans = [''.join(l) for l in itertools.product(string,repeat = n)]
ans = sorted(ans)
for a in ans:
    print(a)