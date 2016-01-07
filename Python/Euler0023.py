"""
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math

def find_proper_divisors(n):
    factors = []
    max_factor_to_check = int(math.floor(math.sqrt(n)))
    for x in range(1, max_factor_to_check + 1):
        if n % x == 0:
            factors.append(x)
            
            if n != x and 2*x != n:
                factors.append(n / x)
    factors.remove(n)

    # there's a bug somewhere in the code above. finding divisors of 16 will return a list with 4 twice.
    # will fix bug later. In the meantime, I'm removing duplicates from the factor list below as a workaround.
    return sorted(list(set(factors)))

def find_sum_of_factors(n):
    return sum(find_proper_divisors(n))

def is_abundant(n):
    return n < find_sum_of_factors(n)


abundant_numbers = []
for i in range(4, 28124):
    if is_abundant(i):
        abundant_numbers.append(i)
        
def is_sum_of_two_abundants(n, abundant_numbers):
    is_sum = False
    
    for a in abundant_numbers:
        if a > n:
            break
        if (n - a) in abundant_numbers:
            is_sum = True
            break
    return is_sum

assert is_sum_of_two_abundants(24, abundant_numbers) == True
assert is_sum_of_two_abundants(54, abundant_numbers) == True
assert is_sum_of_two_abundants(126, abundant_numbers) == True
assert is_sum_of_two_abundants(114, abundant_numbers) == True
assert is_sum_of_two_abundants(28120 + 28122, abundant_numbers) == True


# this is horribly ineffecient. will have to refactor later.
numbers_not_the_sum_of_two_abundants = []
for i in range(1, 28124):
    print "i", str(i)
    if not is_sum_of_two_abundants(i, abundant_numbers):
        print "a", str(i)
        numbers_not_the_sum_of_two_abundants.append(i)

# 4179871
print sum(numbers_not_the_sum_of_two_abundants)
