# Code on Python 3.7.4
# Working @ Dec, 2020
# david-boo.github.io 

# We have k organisms of type AA, m organisms of type Aa and n organisms of type aa. We want to calculate the probability of production of an organism of type AA or Aa

# If we sum all the possible cases we obtain a formula for the desired answer

k,m,n=29,15,22

def prob(k,m,n):
    Q=k+m+n
    D=float(Q*(Q-1))
    return(1 - (n*(m+n-1)/D + m*(m-1)/(4*D)))

print(prob(k,m,n))
