# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# Remember Fibonacci sequence: k(n-1)-1=k*n-k-1

n,k=34,2

def fibonacci(n, k):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1,k) + k * fibonacci(n-2,k)

print(fibonacci(n,k))

