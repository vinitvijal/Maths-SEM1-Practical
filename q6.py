#write a function to Generate basis of column space, null space, row space and left null space of a matrix space.

import numpy as np

def main():
    # Create a matrix
    A = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
    print("Matrix:")
    print(A)

    # Find the basis of the column space
    col = np.linalg.matrix_rank(A)
    print("Basis of the column space:", col)

    # Find the basis of the null space
    null = np.linalg.matrix_rank(A)
    print("Basis of the null space:", null)

    # Find the basis of the row space
    row = np.linalg.matrix_rank(A)
    print("Basis of the row space:", row)

    # Find the basis of the left null space
    left = np.linalg.matrix_rank(A)
    print("Basis of the left null space:", left)