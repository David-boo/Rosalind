# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io

# Calculates Fibonacci sequence with mortality rate and returns total offspring, assuming each rabbit pair produces exactly 1 rabbit pair after 1 month lifetime till death

def rabbits(n, k):
  ls=[0] * k
  ls[0] = 1
  fib = [ls[0]]
  for i in range(n):
    ls.insert(0, sum(ls[1:]))
    ls.pop()
    fib.append(sum(ls))

  return fib[n-1]

print(rabbits(93,20))
