"""Matrix Invertibility Analysis Module.

Determines for which parameter values a matrix is invertible by analyzing
when the determinant equals zero (critical values).

Keywords:
    invertibility, determinant, matrix inverse, singular matrix,
    parameter analysis, symbolic computation, linear algebra
"""
from sympy import Matrix, symbols, solve, factor


def invertibility_by_determinant(A: Matrix, param):
    """
    Determines for which values of 'param' the matrix A is invertible.
    """

    if A.rows != A.cols:
        raise ValueError("Matrix must be square")

    print("Matrix A:")
    print(A)
    print()

    # Compute determinant symbolically
    detA = factor(A.det())
    print("det(A) =")
    print(detA)
    print()

    # Solve det(A) = 0
    critical_values = solve(detA, param)

    if len(critical_values) == 0:
        print(f"det(A) ≠ 0 for all {param}")
        print("→ A is invertible for all values of", param)
    else:
        print(f"det(A) = 0 for {param} = {critical_values}")
        print(f"→ A is invertible for all {param} ≠ {critical_values}")

    return detA, critical_values

if __name__ == "__main__":

    k = symbols('k')

    A = Matrix([
        [4, k, 3],
        [k, 2, k],
        [5, k, 4]
    ])

    detA, bad_k = invertibility_by_determinant(A, k)
