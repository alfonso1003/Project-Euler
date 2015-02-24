"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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
while(len(primes) < 10001):
    if is_prime(num):
        primes.append(num)
        num = num + 2
    else:
        num = num + 2
        
print primes[-1]
    