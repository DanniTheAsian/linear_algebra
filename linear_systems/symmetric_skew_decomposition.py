from sympy import Matrix

# Keywords: symmetric matrix, skew-symmetric matrix, decomposition, matrix algebra, transponering

def symmetric_skew_decomposition(A):
    """
    Decomposes a square matrix A into:
        S = 1/2 (A + A^T)   (symmetric part)
        W = 1/2 (A - A^T)   (skew-symmetric part)

    Verifies that:
        A = S + W
    """

    # Check that A is square
    rows, cols = A.shape
    if rows != cols:
        raise ValueError("Matrix must be square")

    print("Original matrix A:")
    print(A)
    print()

    # Transpose
    AT = A.T

    # Symmetric and skew-symmetric parts
    S = (A + AT) / 2
    W = (A - AT) / 2

    print("Symmetric part S = 1/2 (A + A^T):")
    print(S)
    print()

    print("Skew-symmetric part W = 1/2 (A - A^T):")
    print(W)
    print()

    # Verification
    print("Verification: A = S + W ?")
    print(S + W)
    print()

    if S + W == A:
        print("✔ Verified: A = S + W")
    else:
        print("❌ Error: decomposition failed")

    # Extra checks (theoretical properties)
    print()
    print("Check symmetry properties:")
    print("S^T == S :", S.T == S)
    print("W^T == -W:", W.T == -W)

    return S, W


# ------------------ EXAMPLE ------------------

A = Matrix([
    [2, 4, 3],
    [1, 5, 7],
    [0, -2, 6]
])

symmetric_skew_decomposition(A)
