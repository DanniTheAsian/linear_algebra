from sympy import Matrix, symbols, det, pprint

# Keywords: eigenvalues, triangular matrix

def eigenvalues_upper_triangular(U):
    """
    Computes eigenvalues of an upper triangular matrix
    by forming and evaluating the characteristic polynomial.
    Prints all steps.
    """
    U = Matrix(U)

    if U.rows != U.cols:
        raise ValueError("Matrix must be square")

    n = U.rows
    lam = symbols('λ')

    print("Upper triangular matrix U:")
    pprint(U)

    # Form A - λI
    I = Matrix.eye(n)
    char_matrix = U - lam * I

    print("\nMatrix (U - λI):")
    pprint(char_matrix)

    # Determinant = characteristic polynomial
    char_poly = det(char_matrix)

    print("\nCharacteristic polynomial:")
    pprint(char_poly)

    # Solve det(U - λI) = 0
    eigenvalues = char_poly.factor().as_ordered_factors()

    print("\nSolve det(U - λI) = 0:")
    for factor in eigenvalues:
        pprint(factor)

    # Extract eigenvalues directly (diagonal entries)
    eigs = [U[i, i] for i in range(n)]

    print("\nEigenvalues:")
    for i, ev in enumerate(eigs, start=1):
        print(f"λ{i} = {ev}")

    return eigs


# -------- Problem 5.a (fra billedet) --------

U = [
    [6, 0, 0],
    [1, 8, 0],
    [2, 4, 2]
]

eigenvalues_upper_triangular(U)
