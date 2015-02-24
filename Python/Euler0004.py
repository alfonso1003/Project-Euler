"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome_num(n):
    num_as_str = str(n)
    return num_as_str == num_as_str[::-1]


palindrome_nums = []
for n1 in range(100,1000):
    for n2 in range(100,1000):
        num = n1*n2
        if is_palindrome_num(num) == True:
            palindrome_nums.append(num)

print max(palindrome_nums)