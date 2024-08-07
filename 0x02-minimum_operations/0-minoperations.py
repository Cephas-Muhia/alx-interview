#!/usr/bin/python3

"""
A method that calculates the fewest number of operations needed to result in exactly n H characters in the file, given  a number n whereby In a text file, there is a single character H. The editor can execute only two operations in this file: Copy All and Paste
"""

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations

# Testing the function with the given examples
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

