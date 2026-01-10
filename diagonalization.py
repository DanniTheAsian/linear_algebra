from sympy import Matrix


def diagonalize_matrix(matrix):
    """
    Attempt to diagonalize a square matrix A.

    Args:
        matrix (list[list[int | float]]): Square matrix A

    Returns:
        tuple:
        (is_diagonalizable, P, D)
        - is_diagonalizable (bool)
        - P: matrix of eigenvectors (or None)
        - D: diagonal matrix of eigenvalues (or None)
    """
    A = Matrix(matrix)

    # Try diagonalization using SymPy
    try:
        P, D = A.diagonalize()
        return True, P, D
    except Exception:
        return False, None, None


if __name__ == "__main__":
    # ---------- Example 1: Diagonalizable ----------
    A1 = [
        [2, 1],
        [1, 2]
    ]

    print("Matrix A1:")
    print(Matrix(A1))

    is_diag, P, D = diagonalize_matrix(A1)

    if is_diag:
        print("\nA1 is diagonalizable")
        print("\nMatrix P (eigenvectors):")
        print(P)

        print("\nMatrix D (eigenvalues on diagonal):")
        print(D)

        print("\nCheck: A = P * D * P^-1")
        print(P * D * P.inv())
    else:
        print("\nA1 is NOT diagonalizable")

    # ---------- Example 2: Not diagonalizable ----------
    A2 = [
        [1, 1],
        [0, 1]
    ]

    print("\n-----------------------------")
    print("Matrix A2:")
    print(Matrix(A2))

    is_diag, P, D = diagonalize_matrix(A2)

    if is_diag:
        print("\nA2 is diagonalizable")
    else:
        print("\nA2 is NOT diagonalizable (not enough eigenvectors)")
