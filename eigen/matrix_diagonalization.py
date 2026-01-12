from sympy import Matrix, symbols, pprint, Rational

# Keywords: diagonalization, eigenvectors, RREF

def eigenvector_via_rref(A, lam):
    """
    Computes an eigenvector by solving (A - λI)x = 0 using RREF.
    Prints all steps.
    """
    A = Matrix(A)
    n = A.rows
    I = Matrix.eye(n)

    print(f"\nSolve (A - λI)x = 0 for λ = {lam}")

    M = A - lam * I
    print("\nMatrix A - λI:")
    pprint(M)

    augmented = M.row_join(Matrix.zeros(n, 1))

    print("\nAugmented matrix [A - λI | 0]:")
    pprint(augmented)

    rref_matrix, pivots = augmented.rref()

    print("\nRREF:")
    pprint(rref_matrix)
    print(f"Pivots (leading variables): {pivots}")

    free_vars = [i for i in range(n) if i not in pivots]
    print(f"Free variable indices: {free_vars}")

    if not free_vars:
        raise ValueError(
            f"No non-trivial solution for (A - {lam}I)x = 0 → λ is not an eigenvalue."
        )

    # Build eigenvector by setting first free variable = 1
    v = [0]*n
    free_index = free_vars[0]
    v[free_index] = 1

    for pivot_row, pivot_col in enumerate(pivots):
        v[pivot_col] = -rref_matrix[pivot_row, free_index]

    v = Matrix(v)

    print("\nGeneral solution x = α ·")
    pprint(v)

    print("\nChoosing α = 1, basic eigenvector:")
    pprint(v)

    return v


def diagonalization_full(A):
    """
    Full diagonalization with printed steps.
    """
    A = Matrix(A)

    print("Matrix A:")
    pprint(A)

    # ✅ CORRECT eigenvalues (robust)
    eigenvalues = list(A.eigenvals().keys())

    print("\nEigenvalues:")
    for ev in eigenvalues:
        print(ev)

    # Step 2: eigenvectors via RREF
    eigenvectors = []
    for ev in eigenvalues:
        v = eigenvector_via_rref(A, ev)
        eigenvectors.append(v)

    # Step 4: assemble P
    P = Matrix.hstack(*eigenvectors)
    print("\nMatrix P (eigenvectors as columns):")
    pprint(P)

    # Step 5: assemble D
    D = Matrix.diag(*eigenvalues)
    print("\nMatrix D:")
    pprint(D)

    # Step 6: compute P^{-1}
    Pinv = P.inv()
    print("\nMatrix P^{-1}:")
    pprint(Pinv)

    # Step 7: verify A = PDP^{-1}
    print("\nVerify A = P D P^{-1}:")
    pprint(P * D * Pinv)

    # ------------------ Dominant eigenvalue approximation ------------------

    print("\n--- Dominant eigenvalue approximation (k → ∞) ---")

    # Dominant eigenvalue is λ = 1
    D_approx = Matrix([
        [1, 0],
        [0, 0]   # (3/10)^k → 0
    ])

    print("\nApproximated D^k:")
    pprint(D_approx)

    A_approx = P * D_approx * Pinv

    print("\nApproximation of A^k:")
    pprint(A_approx)

    # Initial vector x0
    x0 = Matrix([1000, 0])

    print("\nInitial vector x0:")
    pprint(x0)

    xk_approx = A_approx * x0

    print("\nApproximate x_k = A^k x0:")
    pprint(xk_approx)

    print("\nNumerical approximation:")
    print([float(xk_approx[0]), float(xk_approx[1])])

    return P, D, Pinv


# -------- Problem 7.a (exact matrix from facit) --------

A = Matrix([
    [8, 5],
    [2, 5]
]) / 10

diagonalization_full(A)

