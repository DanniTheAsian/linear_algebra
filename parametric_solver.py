from sympy import symbols, Eq, solve, Matrix

# Variabler og parameter
x1, x2, t = symbols('x1 x2 t')

# ---------- METODE 1: Algebraisk ----------
equation = Eq(3*x1 + x2, 2)

# Sæt x1 = t og løs for x2
solution_alg = solve(equation.subs(x1, t), x2)

print("Metode 1 (algebraisk):")
print(f"x1 = t")
print(f"x2 = {solution_alg[0]}")
print()

# ---------- METODE 2: Matrix / RREF ----------
A = Matrix([[3, 1, 2]])  # augmented matrix

rref_matrix, pivots = A.rref()

print("Metode 2 (RREF):")
print("RREF:")
print(rref_matrix)

print("Parametrisk løsning:")
print("x1 = t")
print("x2 = 2 - 3t")
