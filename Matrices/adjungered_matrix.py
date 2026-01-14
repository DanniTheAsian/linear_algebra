"""Adjugate Matrix and Inverse Computation Module.

Computes adjugate matrices via cofactors and solves matrix equations using
adjugate-based matrix inverse: A^(-1) = (1/det(A)) * adj(A).

Keywords:
    adjugate, adjoint, cofactor, matrix inverse, determinant method,
    inverse formula, cofactor matrix
"""
from sympy import Matrix, Rational


# Code below
def adjugate_general(A: Matrix) -> Matrix:
    """
    Computes adj(A) = cofactor(A)^T for any square matrix A.
    """
    if A.rows != A.cols:
        raise ValueError("Matrix must be square")

    n = A.rows
    cof = Matrix.zeros(n, n)

    for i in range(n):
        for j in range(n):
            minor = A.minor_submatrix(i, j)
            cof[i, j] = (-1) ** (i + j) * minor.det()

    return cof.T


# ============================================================
# INVERSE VIA ADJUGATE
# ============================================================

def inverse_via_adjugate(A: Matrix) -> Matrix:
    """
    Computes A^{-1} = (1/det(A)) * adj(A).
    """
    detA = A.det()
    if detA == 0:
        raise ValueError("Matrix is not invertible (det(A)=0).")

    adjA = adjugate_general(A)
    return Rational(1, 1) / detA * adjA


# ============================================================
# SOLVE Ax = b USING ADJUGATE
# ============================================================

def solve_via_adjugate(A: Matrix, b: Matrix) -> Matrix:
    """
    Solves Ax = b using x = A^{-1} b with inverse via adjugate.
    """
    if b.cols != 1:
        raise ValueError("b must be a column vector")

    A_inv = inverse_via_adjugate(A)
    return A_inv * b


# ============================================================
# DEMO / TEST (KAN FJERNES TIL EKSAMEN)
# ============================================================

if __name__ == "__main__":

    print("\n--- GENEREL TEST 1 (2x2) ---")
    A = Matrix([[120, 140],
                [130, 130]])
    b = Matrix([[5800],
                [5980]])

    print("A =")
    print(A)
    print("\nb =")
    print(b)

    x = solve_via_adjugate(A, b)
    print("\nLøsning x = A^(-1)b =")
    print(x)

    print("\n--- GENEREL TEST 2 (3x3) ---")
    A2 = Matrix([[2, 1, 0],
                 [1, 1, 1],
                 [0, 2, 1]])
    b2 = Matrix([[1],
                 [2],
                 [3]])

    print("A =")
    print(A2)
    print("\nb =")
    print(b2)

    x2 = solve_via_adjugate(A2, b2)
    print("\nLøsning x =")
    print(x2)
