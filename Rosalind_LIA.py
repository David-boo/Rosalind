# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Code is quite easy if you spot the formula.

# Any combination of any genotype of egg with sperm from a heterozygous will result in a probability of obtaining an AaBb offspring in any generation of 0.25.

# The probability of there being n or more successes (AaBb) is equivalent to the probability of there being (2k)−n or less failures (everything not AaBb) (There are 2k 'trials')

# This forms a binomial distribution and we can apply formula using our data.

from math import factorial as f

n,k=7,5

print(sum([(f(2**k)/(f(2**k-n)*f(n)) * 0.25**n * 0.75**(2**k-n)) for n in range(n,2**k+1)]))