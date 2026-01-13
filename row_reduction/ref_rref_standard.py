from sympy import Matrix, symbols

def ref_and_rref(A):
    rows, cols = A.shape
    num_vars = cols - 1  # sidste kolonne er konstantled

    # Variabler x1, x2, ...
    variables = symbols(f"x1:{num_vars+1}")

    print("Augmented matrix A:")
    print(A)
    print()

    # ---------- REF ----------
    REF = A.echelon_form()
    print("REF (Row Echelon Form):")
    print(REF)
    print()

    # ---------- RREF ----------
    RREF, pivots = A.rref()
    print("RREF (Reduced Row Echelon Form):")
    print(RREF)
    print()

    # ---------- Inkonsistens ----------
    for r in range(rows):
        if all(RREF[r, c] == 0 for c in range(num_vars)) and RREF[r, -1] != 0:
            print("❌ Systemet er INKONSISTENT (ingen løsninger)")
            return

    pivot_vars = [variables[i] for i in pivots]
    free_vars = [variables[i] for i in range(num_vars) if i not in pivots]

    print("Pivot-variable:", pivot_vars)
    print("Frie variable:", free_vars)
    print()

    # ---------- Parametrisk løsning ----------
    if not free_vars:
        print("✅ Unik løsning:")
        for i, var in enumerate(variables):
            print(f"{var} = {RREF[i, -1]}")
        return

    print("♾️ Uendeligt mange løsninger (parametrisk form):")

    # Parametre t1, t2, ...
    parameters = symbols(f"t1:{len(free_vars)+1}")
    param_map = dict(zip(free_vars, parameters))

    solutions = {}

    # Frie variable
    for fv in free_vars:
        solutions[fv] = param_map[fv]

    # Pivot-variable (én pr. pivot-række)
    for row_index, col_index in enumerate(pivots):
        var = variables[col_index]
        expr = RREF[row_index, -1]

        for fv in free_vars:
            fv_index = variables.index(fv)
            expr -= RREF[row_index, fv_index] * param_map[fv]

        solutions[var] = expr

    for var in variables:
        print(f"{var} = {solutions[var]}")


if __name__ == "__main__":
    A = Matrix([
        [3, -1, -31],
        [1,2,37]
    ])

    ref_and_rref(A)
