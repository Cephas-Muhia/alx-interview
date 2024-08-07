#!/usr/bin/python3

"""
A method that calculates the fewest number of operations needed to result in
exactly n H characters in the file. Given a number n, the text editor can
execute only two operations in this file: Copy All and Paste.
"""


def minOperations(n):
    """
    min_operations
    Gets fewest number of operations needed to result in exactly n H characters
    """
    if n < 2:
        return 0

    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            # Total even-divisions by root = total operations
            ops += root
            # Set n to the remainder
            n //= root
            # Reduce root to find remaining smaller values that evenly divide n
            root -= 1
        # Increment root until it evenly divides n
        root += 1
    return ops

