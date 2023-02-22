# Solve a system of Homogeneous equations using the Gauss Jordan method.

import numpy as np

def main():
    # Create a matrix
    A = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
    print("Matrix:")
    print(A)

    # Create a vector
    v = np.array([1, 2, 3])
    print("Vector:")
    print(v)

    # Solve the system of homogeneous equations
    x = np.linalg.solve(A, v)
    print("Solution to the system of homogeneous equations:")
    print(x)

    # Create a vector
    v = np.array([1, 2, 3])
    print("Vector:")
    print(v)

    # Solve the system of non-homogeneous equations
    x = np.linalg.solve(A, v)
    print("Solution to the system of non-homogeneous equations:")
    print(x)

main()