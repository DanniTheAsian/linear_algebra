from sympy import Matrix, symbols, simplify

def solve_linear_system_rref(A):
    """
    Løser et lineært ligningssystem via Gauss-Jordan (RREF).

    Input:
      A: augmented matrix (m x (n+1))

    Output:
      - RREF
      - konsistent / inkonsistent
      - løsning i matrixform
      - løsning som linearkombination
    """

    rows, cols = A.shape
    n = cols - 1  # antal variable
    x = symbols(f"x1:{n+1}")

    print("Augmented matrix:")
    print(A)
    print()

    # ---------- RREF ----------
    RREF, pivots = A.rref()
    print("RREF:")
    print(RREF)
    print()

    # ---------- Konsistens ----------
    for i in range(rows):
        if all(RREF[i, j] == 0 for j in range(n)) and RREF[i, -1] != 0:
            print("Systemet er INKONSISTENT")
            print("→ række [0 0 ... 0 | k], k ≠ 0")
            return

    print("Systemet er KONSISTENT\n")

    # ---------- Leading & free variables ----------
    pivot_cols = list(pivots)
    free_cols = [j for j in range(n) if j not in pivot_cols]

    print("Leading variables:", [x[j] for j in pivot_cols])
    print("Free variables:", [x[j] for j in free_cols])
    print()

    # ---------- Parametre ----------
    alpha = symbols("α")
    sol = {}

    # frie variable
    for j in free_cols:
        sol[x[j]] = alpha

    # pivot-variable (back substitution direkte fra RREF)
    for i, p in enumerate(pivot_cols):
        rhs = RREF[i, -1]
        for j in free_cols:
            rhs -= RREF[i, j] * sol[x[j]]
        sol[x[p]] = simplify(rhs)

    # ---------- Løsning ----------
    print("Generel løsning:")
    for var in x:
        print(f"{var} = {sol.get(var, 0)}")

    # ---------- Matrixform ----------
    const_vec = []
    param_vec = []

    for var in x:
        expr = sol.get(var, 0)
        const_part = expr.subs(alpha, 0)
        param_part = simplify(expr - const_part)
        const_vec.append(const_part)
        param_vec.append(param_part / alpha if alpha in param_part.free_symbols else 0)

    print("\nMatrixform:")
    print("x =")
    print(Matrix(const_vec), "+ α", Matrix(param_vec))


# ================== EKSEMPEL FRA OPGAVEN ==================

A = Matrix([
    [1,  3, 1,  1,  3],
    [2, -2, 1,  2,  8],
    [3,  1, 2, -1, -1]
])

solve_linear_system_rref(A)
