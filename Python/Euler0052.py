"""
Permuted multiples
Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
 
def num_digits(n):
    """
    return a sorted list of digits in a number
    """
    l = []
    while True:
        l.append(n % 10)
        n /= 10
        
        if n == 0:
            break
    l.sort()
    
    return l


 
i = 1
while True:
    a = num_digits(i)
    for j in range(1,7):
        b = num_digits(i * j)
        if a != b:
            break
        if j == 6:
            print i
            i = 0
    if i == 0:
        break
    i += 1