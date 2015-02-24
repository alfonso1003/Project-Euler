"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
c = len(nums)


x = 20
found = False

while(not found):
    count = 0

    for n in nums:
        if x % n == 0:
            count = count + 1

    if count == c:
        print x
        found = True
    else:
        x = x + 1