# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Packages make this straightforward. Permutations generates every single permutation

# itertools.product generates the Cartesian product (ie: making every combination for all permutations available)

from itertools import permutations, product

n=5
def signPermutations(n):
    for perm in permutations(xrange(1, n + 1)):
        for sign_perm in product(*[(-element, element) for element in perm]):
        # With * we can use them in product
            yield sign_perm