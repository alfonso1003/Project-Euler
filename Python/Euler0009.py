"""
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def gen_pyth_triples(n):
    a = (2*n + 1)
    b = (2*n*(n + 1))
    # c = (2*n*(n + 1) + 1)
    c = 1000 - a - b
    return a, b, c


"""
n = 1

found = False
while(not found):
    a, b, c = gen_pyth_triples(n)
    print a, b, c
    
    if a + b + c == 1000:
        print a*b*c
        found = True
    else:
        n = n + 1
"""

for n in range(0, 100):
    a, b, c =  gen_pyth_triples(n)
    print a, b, c
    print a + b + c
