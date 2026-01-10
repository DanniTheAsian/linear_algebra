from sympy import Matrix


def determinant_matrix(matrix):
    """
    Compute the determinant of a square matrix.

    Args:
        matrix (list[list[int | float]]): Square matrix A

    Returns:
        det (number): Determinant of A
        is_invertible (bool): True if det != 0
    """
    A = Matrix(matrix)
    det = A.det()

    return det, det != 0


if __name__ == "__main__":
    # ---------- Example 1: Invertible matrix ----------
    A1 = [
        [2, 1],
        [1, 1]
    ]

    det, invertible = determinant_matrix(A1)

    print("Matrix A1:")
    print(Matrix(A1))
    print(f"det(A1) = {det}")
    print("Invertible:", invertible)

    # ---------- Example 2: Not invertible ----------
    A2 = [
        [1, 2],
        [2, 4]
    ]

    det, invertible = determinant_matrix(A2)

    print("\nMatrix A2:")
    print(Matrix(A2))
    print(f"det(A2) = {det}")
    print("Invertible:", invertible)
