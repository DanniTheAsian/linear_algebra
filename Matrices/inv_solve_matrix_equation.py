"""Matrix Equation Solver Module.

Solves matrix equations of the form (X1 * A * X2)^{T,-1} = B^{T,-1}
by isolating A using transpose and inverse rules.

Keywords:
    matrix equation, matrix inverse, transpose, matrix algebra,
    symbolic computation, isolating variables
"""
from sympy import Matrix, eye, Rational


def solve_for_A(
    left_matrices,
    B,
    transpose_left=False,
    inverse_left=False,
    transpose_right=False,
    inverse_right=False,
):
    """
    Løser matrixligninger af typen:

        (X1 * A * X2)^{T,-1} = B^{T,-1}

    hvor A isoleres ved brug af inverse- og transpose-regler.
    """

    Y = B

    # --- Ryd højresiden ---
    if inverse_right:
        Y = Y.inv()
    if transpose_right:
        Y = Y.T

    # --- Ryd venstresiden (modsat rækkefølge) ---
    if inverse_left:
        Y = Y.inv()
    if transpose_left:
        Y = Y.T

    # --- Flyt kendte matricer væk fra A ---
    for M in reversed(left_matrices):
        Y = M.inv() * Y

    return Y


# ============================================================
# EKSEMPEL 1  (Problem 5.a)
# (2A)^T = M^{-1}
# ============================================================

print("\n--- Eksempel 1: (2A)^T = M^{-1} ---")

M = Matrix([
    [1, -1],
    [2,  3]
])

A1 = solve_for_A(
    left_matrices=[2 * eye(2)],
    B=M,
    transpose_left=True,
    inverse_right=True
)

print("A =")
print(A1)

# Forventet:
# [[ 3/10, -2/10],
#  [ 1/10,  1/10]]


# ============================================================
# EKSEMPEL 2  (Problem 5.b)
# (M A)^(-1) = B
# ============================================================

print("\n--- Eksempel 2: (M A)^(-1) = B ---")

M = Matrix([
    [1, 0],
    [2, 1]
])

B = Matrix([
    [1, 0],
    [2, 2]
])

A2 = solve_for_A(
    left_matrices=[M],
    B=B,
    inverse_left=True
)

print("A =")
print(A2)

# Forventet:
# [[ 1,  0],
#  [-3, 1/2]]


# ============================================================
# EKSEMPEL 3
# (M A N)^T = B
# ============================================================

print("\n--- Eksempel 3: (M A N)^T = B ---")

M = Matrix([
    [1, 2],
    [0, 1]
])

N = Matrix([
    [2, 0],
    [1, 1]
])

B = Matrix([
    [3, 1],
    [4, 2]
])

A3 = solve_for_A(
    left_matrices=[M, N],
    B=B,
    transpose_left=True
)

print("A =")
print(A3)


# ============================================================
# EKSEMPEL 4
# (A^T)^(-1) = B
# ============================================================

print("\n--- Eksempel 4: (A^T)^(-1) = B ---")

B = Matrix([
    [2, 1],
    [1, 1]
])

A4 = solve_for_A(
    left_matrices=[],
    B=B,
    inverse_left=True,
    transpose_left=True
)

print("A =")
print(A4)
