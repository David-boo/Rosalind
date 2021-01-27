# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Code is quite simple. Punnett square is the key to resolve the problem.

# Any couple with a homozygous dominant member will produce offspring with at least one dominant allele. The probability of passing a dominant allele for the next two is found using Punnet squares (3/4 and 1/2). 

# Answer is, then, ans=(a+b+c)*2 + 3/2∗e + f

data=open('rosalind_iev.txt','r').readline().replace(' ',',').split(',')

a,b,c,d,e,f = float(data[0]),float(data[1]),float(data[2]),float(data[3]),float(data[4]),float(data[5])

print((a+b+c)*2+d*3/2+e*1+f*0)