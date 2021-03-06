"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def find_factors(n):
    factors = []
    max = int(math.floor(math.sqrt(n)))
    for x in range(1, max + 1):
        if n % x == 0:
            factors.append(x)
            
            if n != x and 2*x != n:
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

factors = find_factors(600851475143)

print max(f for f in factors if is_prime(f) == True)
