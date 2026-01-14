from sympy import Matrix, eye

def inverse_with_steps(A: Matrix):
    """
    Finder A^{-1} for en vilkårlig n×n matrix A
    vha. Gauss–Jordan-elimination og viser alle trin.
    """
    rows, cols = A.shape
    if rows != cols:
        raise ValueError("Matrixen skal være kvadratisk.")

    print("Matrix A:")
    print(A)
    print()

    # Tjek invertibilitet via determinant
    detA = A.det()
    print(f"det(A) = {detA}")
    if detA == 0:
        print("→ Matrixen er IKKE invertibel.")
        return None
    print("→ Matrixen er invertibel.\n")

    # Augmented matrix [A | I]
    I = eye(rows)
    Aug = A.row_join(I)

    print("Augmented matrix [A | I]:")
    print(Aug)
    print()

    # RREF (Gauss–Jordan)
    RREF, pivots = Aug.rref()

    print("Efter Gauss–Jordan (RREF):")
    print(RREF)
    print()

    # Split resultat
    A_inv = RREF[:, cols:]

    print("Venstre side (skal være I):")
    print(RREF[:, :cols])
    print()

    print("Højre side = A^(-1):")
    print(A_inv)
    print()

    # Tjek
    print("Tjek: A * A^(-1) =")
    print(A * A_inv)
    print()

    print("Tjek: A^(-1) * A =")
    print(A_inv * A)
    print()

    return A_inv


if __name__ == "__main__":

    A = Matrix([
        [1, 0],
        [2, 2]
    ])

    A_inv = inverse_with_steps(A)
