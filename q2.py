import numpy as np
# Generate the matrix into echelon form  with linalg module


def echlon():
    A = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
    print("Matrix:")
    print(A)

    # Find the echelon form of the matrix
    ech = np.linalg.matrix_rank(A)
    print("Echelon form:", ech)
    
    # Find the reduced echelon form of the matrix
    ech = np.linalg.matrix_rank(A, True)
    print("Reduced Echelon form:", ech)
    
    # Find the rank of the matrix
    ech = np.linalg.matrix_rank(A)
    print("Rank:", ech)

if __name__ == "__main__":
    echlon()

