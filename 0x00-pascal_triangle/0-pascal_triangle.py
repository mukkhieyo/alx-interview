#!/usr/bin/python3
"""
A Pascal Triangle
"""


def pascal_triangle(n):
    """
    A function that returns  a list of lists of integers
    representing the Pascal’s triangle n
    """
    if n <= 0:
        return []
    """Initializing first row"""
    result = [[1]]
    """Looping through the other rows"""
    for i in range(1, n):
        """Initializing the row with a fixed number 1"""
        row = [1]
        """Looping through the middle items"""
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])
        """Add the last fixed number 1"""
        row.append(1)
        """Add the full row to the triangle"""
        result.append(row)
    return result
