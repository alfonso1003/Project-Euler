"""
Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

num_collatz_len_dict = {}
for x in range(1, 1000001):
    number = x
    collatz_sequence = []
    while number != 1:
        if number % 2 == 1:
            number = 3 * number + 1
        else:
            number = number / 2
    
        collatz_sequence.append(number)
    
        num_collatz_len_dict[x] = len(collatz_sequence)
    
#print num_collatz_len_dict
print max(num_collatz_len_dict, key=num_collatz_len_dict.get)
