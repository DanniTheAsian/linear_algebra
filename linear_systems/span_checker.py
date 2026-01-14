from sympy import Matrix, symbols


def span_checker(vectors, target):
    """
    Checks whether target is in the span of given vectors
    and explicitly inserts the coefficients.
    """

    k = len(vectors)
    coeffs = symbols(f'c1:{k+1}')

    # A * c = v
    A = Matrix(vectors).T
    b = Matrix(target)
    Aug = A.row_join(b)

    print("Augmented matrix [A | v]:")
    print(Aug)
    print()

    RREF, pivots = Aug.rref()

    print("RREF:")
    print(RREF)
    print()

    rows, cols = RREF.shape

    # ---------- Konsistens ----------
    for r in range(rows):
        if all(RREF[r, c] == 0 for c in range(cols - 1)) and RREF[r, -1] != 0:
            print("❌ Target vector is NOT in the span.")
            return

    print("✅ Target vector IS in the span.\n")

    free_vars = set(range(k)) - set(pivots)
    if free_vars:
        print("✔ Infinite solutions (parametric form).")
        return

    # ---------- Unik løsning ----------
    solution = {}

    print("✔ Coefficients:")
    for col in pivots:
        row = pivots.index(col)
        solution[coeffs[col]] = RREF[row, -1]
        print(f"{coeffs[col]} = {RREF[row, -1]}")

    # ---------- Indsæt værdier ----------
    print("\n✔ Insert coefficients into linear combination:")

    combo = Matrix.zeros(len(target), 1)
    for i in range(k):
        term = solution[coeffs[i]] * Matrix(vectors[i])
        print(f"{solution[coeffs[i]]} * {Matrix(vectors[i]).T}")
        combo += term

    print("\nResulting vector:")
    print(combo)

    print("\nTarget vector:")
    print(b)

    if combo == b:
        print("\n✅ Verified: Linear combination equals target vector.")
    else:
        print("\n❌ Something went wrong.")


# ================== KONKRET EKSEMPEL ==================

if __name__ == "__main__":
    x1 = [2, 1, -1]
    x2 = [1, 0, 1]
    x3 = [1, 1, -2]
    v  = [0, 1, -3]

    span_checker([x1, x2, x3], v)
