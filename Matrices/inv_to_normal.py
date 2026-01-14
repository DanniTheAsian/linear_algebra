from sympy import Matrix, Rational

def find_A_from_inverse_expression(M):
    """
    Løser opgaver af typen:
    (2A)^T = M^{-1}
    og finder A
    """

    print("Givet matrix M:")
    print(M)
    print()

    # Transponér M
    MT = M.T
    print("M^T:")
    print(MT)
    print()

    # Invers af M^T
    MT_inv = MT.inv()
    print("(M^T)^(-1):")
    print(MT_inv)
    print()

    # Gang med 1/2
    A = Rational(1, 2) * MT_inv
    print("A = 1/2 * (M^T)^(-1):")
    print(A)
    print()

    return A


# -------- EKSEMPEL FRA OPGAVEN --------
M = Matrix([
    [1, -1],
    [2,  3]
])

A = find_A_from_inverse_expression(M)
