import numpy as np

# Create and transform vectors and matrices (the transpose vector (matrix) conjugate transpose of a vector (matrix))

def main():
    # Create a vector
    v = np.array([1, 2, 3])
    print("Vector:")
    print(v)


    # Create a matrix
    A = np.array([[1, 2, 3], [2, 4, -6], [3, 6, 9]])
    print("Matrix:")
    print(A)



    # Transpose the vector
    print("Transpose of the vector:")
    print(v.T)

    # Transpose the matrix
    print("Transpose of the matrix:")
    print(A.T)

    # Conjugate transpose the vector
    print("Conjugate transpose of the vector:")
    print(v.conj().T)

    # Conjugate transpose the matrix
    print("Conjugate transpose of the matrix:")
    print(A.conj().T)

if __name__ == "__main__":
    main()