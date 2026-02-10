#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            prev = triangle[i - 1]
            for j in range(1, i):
                row[j] = prev[j - i] + [j]
        triangle.append(row)

    return triangle
