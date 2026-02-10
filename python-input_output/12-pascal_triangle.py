#!/usr/bin/python3
'''Module that provides a function to generate Pascal's triangle.'''


def pascal_triangle(n):
    '''Return a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): Number of rows of the triangle.

    Returns:
        list[list[int]]: Pascal's triangle represented as a list of rows.
        Returns an empty list if n <= 0.'''
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            prev = triangle[i - 1]
            for j in range(1, i):
                row[j] = prev[j - 1] + prev[j]
        triangle.append(row)

    return triangle
