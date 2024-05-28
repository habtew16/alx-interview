#!/usr/bin/python3
"""
function to rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    first find the transpose of the matrix
    then reverse each row then it is rotated
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
