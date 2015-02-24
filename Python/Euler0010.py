"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

def find_factors(n):
    factors = []
    max = int(math.floor(math.sqrt(n)))
    for x in range(1, max + 1):
        if n % x == 0:
            factors.append(x)
            
            if n != x:
                factors.append(n / x)
        
    return sorted(factors)

def is_prime(n):
    """
    assummes n is non zero positive integer
    """
    
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    num_of_factors = len(find_factors(n))    
    
    if num_of_factors == 2:
        return True
    else:
        return False
    
primes = [2]
num = 3
while(len(primes) < 2000001):
    if is_prime(num):
        primes.append(num)
        num = num + 2
    else:
        num = num + 2
        
print sum(primes)