"""Cofactor and Adjugate Matrix Module.

Computes cofactors and adjugate (adjoint) matrices using cofactor expansion.
The adjugate matrix is useful for computing matrix inverses.

Keywords:
    cofactor, adjugate, adjoint, matrix inverse, minor, determinant
"""
from sympy import Matrix


def cofactor(A: Matrix, i: int, j: int):
    """
    Beregner cofactor c_ij = (-1)^(i+j) * det(A_ij)
    i, j er 0-baserede indeks
    """
    minor = A.minor_submatrix(i, j)
    sign = (-1) ** (i + j)
    return sign * minor.det(), minor


def cofactor_matrix(A: Matrix, show_steps=True):
    """
    Konstruerer hele cofactor-matricen C
    """
    if A.rows != A.cols:
        raise ValueError("Matrix must be square")

    n = A.rows
    C = Matrix.zeros(n, n)

    if show_steps:
        print("Computing cofactor matrix C:\n")

    for i in range(n):
        for j in range(n):
            cij, minor = cofactor(A, i, j)
            C[i, j] = cij

            if show_steps:
                print(f"c{i+1}{j+1} = (-1)^({i+1}+{j+1}) det(A_{i+1}{j+1})")
                print("minor =")
                print(minor)
                print(f"c{i+1}{j+1} = {cij}\n")

    return C


def adjugate(A: Matrix, show_steps=True):
    """
    Beregner adj(A) = C^T
    """
    if show_steps:
        print("Matrix A:")
        print(A)
        print()

    C = cofactor_matrix(A, show_steps=show_steps)

    if show_steps:
        print("Cofactor matrix C =")
        print(C)
        print()

    adjA = C.T

    if show_steps:
        print("Adjugate matrix adj(A) = C^T =")
        print(adjA)
        print()

    return adjA

if __name__ == "__main__":
    A = Matrix([
    [ 1,  0, -1],
    [-1,  1,  0],
    [ 0, -1,  1]
])

adjA = adjugate(A)
