import numpy as np

# Find cofactors, determinant, adjoint and inverse of a matrix. using numpy

def main():
    A = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
    print("Matrix:")
    print(A)

    # Find the determinant of the matrix
    det = np.linalg.det(A)
    print("Determinant:", det)

    # Find the inverse of the matrix
    inv = np.linalg.inv(A)
    print("Inverse:")
    print(inv)

    # Find the adjoint of the matrix
    adj = np.linalg.inv(A).T
    print("Adjoint:")
    print(adj)

    # Find the cofactors of the matrix
    cof = np.linalg.inv(A).T * np.linalg.det(A)
    print("Cofactors:")
    print(cof)

    # Find the cofactor of the first row and first column
    cof = np.linalg.inv(A).T[0, 0] * np.linalg.det(A)
    print("Cofactor of the first row and first column:", cof)

if __name__ == "__main__":
    main()