from typing import List

Matrix = List[List[float]]

# --------------------------------------------------
# Scalar multiplication
# --------------------------------------------------

def scalar_multiply(c: float, A: Matrix) -> Matrix:
    """Returns c * A."""
    return [[c * A[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


# --------------------------------------------------
# Matrix addition
# --------------------------------------------------

def matrix_add(A: Matrix, B: Matrix) -> Matrix:
    """Returns A + B."""
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


# --------------------------------------------------
# Matrix multiplication
# --------------------------------------------------

def matrix_product(A: Matrix, B: Matrix) -> Matrix:
    """Returns A · B."""
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions do not match for multiplication")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


# --------------------------------------------------
# Transpose
# --------------------------------------------------

def transpose_matrix(A: Matrix) -> Matrix:
    return [[A[i][j] for i in range(len(A))]
            for j in range(len(A[0]))]


# --------------------------------------------------
# Pretty print
# --------------------------------------------------

def print_matrix(A: Matrix) -> None:
    for row in A:
        print(" ".join(f"{x:6}" for x in row))


# --------------------------------------------------
# Demo
# --------------------------------------------------

if __name__ == "__main__":

    A = [[1, 2],
         [3, 4]]

    B = [[0, 1],
         [1, 0]]

    print("2A:")
    print_matrix(scalar_multiply(2, A))

    print("\nA + B:")
    print_matrix(matrix_add(A, B))

    print("\nA · B:")
    print_matrix(matrix_product(A, B))
