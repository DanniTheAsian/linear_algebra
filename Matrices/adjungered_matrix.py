
from sympy import Matrix

# Keywords: adjugate matrix, cofactor, inverse matrix

def adjugate_general(A):
    """
    Computes the adjugate matrix of a square matrix A
    using cofactors.
    """
    if A.rows != A.cols:
        raise ValueError("Matrix must be square")

    n = A.rows
    cofactors = Matrix.zeros(n, n)

    for i in range(n):
        for j in range(n):
            minor = A.minor_submatrix(i, j)
            cofactors[i, j] = (-1)**(i + j) * minor.det()

    adj = cofactors.T
    return adj


# -------- Example --------
A = Matrix([[120, 140],
            [130, 130]])

adjA = adjugate_general(A)
print("Adjugate matrix:")
print(adjA)
