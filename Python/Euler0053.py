"""
Combinatoric selections
Problem 53
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n! / (r!(n-r)!), where r <= n, n! = n x (n-1) x ... x 3 x 2 x 1, and 0! = 1.
It is not until n = 23, that a value exceeds one million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

"""


import math


def ncr(n, r):
    n_fac = math.factorial(n)
    r_fac = math.factorial(r)
    n_minus_r_fac = math.factorial(n - r)
    
    return n_fac / (r_fac * n_minus_r_fac)
     

c = 0

for n in range(1,101):
    for r in range(0, n + 1):
        if(ncr(n , r) > 1000000):
            c += 1

print c