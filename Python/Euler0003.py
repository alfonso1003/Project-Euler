"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def find_factors(n):
    factors = []
    max = int(math.floor(math.sqrt(n)))
    for x in range(1, max):
        if n % x == 0:
            factors.append(x)
            factors.append(n / x)
        
    return sorted(factors)


def is_prime(n):
    return None

factors = find_factors(600851475143)