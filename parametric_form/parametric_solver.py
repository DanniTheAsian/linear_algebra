from sympy import symbols, Eq, solve, Matrix

# Keywords: parametric solution, free variables

# Variabler og parameter
x1, x2, t = symbols('x1 x2 t')

# ---------- METODE 1: Algebraisk ----------
eq = Eq(2*x1 + 3*x2, 1)

# Vælg x1 som fri parameter
x2_expr = solve(eq.subs(x1, t), x2)[0]

print("Metode 1 (algebraisk):")
print(f"x1 = t")
print(f"x2 = {x2_expr}")
print(f"Løsning: (x1, x2) = ({t}, {x2_expr})")
print()

# ---------- METODE 2: Matrix / RREF ----------
A = Matrix([[2, 3, 1]])  # augmented matrix
rref, pivots = A.rref()

print("Metode 2 (RREF):")
print("RREF:")
print(rref)

# Fortolkning af RREF
#  x1 + (1/3)x2 = 2/3
#  vælg x2 = t
x1_expr = rref[0,2] - rref[0,1]*t

print("Parametrisk løsning:")
print(f"x2 = t")
print(f"x1 = {x1_expr}")
print(f"Løsning: (x1, x2) = ({x1_expr}, {t})")
