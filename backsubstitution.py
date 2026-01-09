from sympy import Matrix, symbols

def back_substitution(U):
    """
    U: augmented matrix i REF (n x (n+1))
    returnerer løsningen som dict
    """
    n = U.rows
    x = symbols(f"x1:{n+1}")
    solution = {}

    # Gå nedefra og op
    for i in reversed(range(n)):
        rhs = U[i, -1]
        for j in range(i+1, n):
            rhs -= U[i, j] * solution[x[j]]
        solution[x[i]] = rhs / U[i, i]

    return solution


# -------- EKSEMPEL --------
# System i REF:
# x1 + 2x2 + x3 = 5
#      x2 - x3 = 1
#           x3 = 2

U = Matrix([
    [1, 2, 1, 5],
    [0, 1, -1, 1],
    [0, 0, 1, 2]
])

sol = back_substitution(U)

print("Løsning:")
for var, val in sol.items():
    print(f"{var} = {val}")
