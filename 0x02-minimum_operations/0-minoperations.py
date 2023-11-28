#!/usr/bin/python3
"""
a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n):
    result = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            result += divisor
            n //= divisor
        divisor += 1
    return result
