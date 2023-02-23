# Generate basis of column space, null space, row space and left null space of a matrix space


import sympy as sp

def main():
    # Create a matrix
    A = sp.Matrix([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
    print("Matrix:")
    print(A)

    # Find the basis of the column space
    col = A.columnspace()
    print("Basis of the column space:", col)

    # Find the basis of the null space
    null = A.nullspace()
    print("Basis of the null space:", null)

    # Find the basis of the row space
    row = A.rowspace()
    print("Basis of the row space:", row)

 

if __name__ == "__main__":
    main()
