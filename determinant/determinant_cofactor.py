from sympy import Matrix

def determinant_cofactor_expansion(A, row=0):
    """
    Computes det(A) using cofactor expansion along a given row.
    """
    if A.rows != A.cols:
        raise ValueError("Matrix must be square")

    n = A.rows
    det = 0

    print(f"Cofactor expansion along row {row + 1}:\n")

    for j in range(n):
        a = A[row, j]
        minor = A.minor_submatrix(row, j)
        cofactor = (-1)**(row + j) * minor.det()

        print(f"a{row+1}{j+1} = {a}")
        print(f"minor:")
        print(minor)
        print(f"cofactor c{row+1}{j+1} = {cofactor}\n")

        det += a * cofactor

    print(f"det(A) = {det}")
    return det


# -------- Example (fra dit billede) --------

A = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

determinant_cofactor_expansion(A)
