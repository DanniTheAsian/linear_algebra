"""Linear System Case Analysis Module.

Analyzes parametric linear systems to determine solution existence
for different parameter values using symbolic computation.

Keywords:
    case analysis, parametric system, parameter values, conditional solution,
    symbolic computation, REF
"""
from sympy import Matrix, symbols, simplify
a, b = symbols("a b")
x1, x2 = symbols("x1 x2")

# Augmented matrix
A = Matrix([
    [1, -b, -1],
    [1,  a,  3]
])

print("Augmented matrix:")
print(A)
print()

# ---------- REF ----------
REF = A.echelon_form()
print("REF:")
print(REF)
print()

# REF er:
# [1  -b | -1]
# [0 a+b |  4]

pivot = simplify(a + b)

# ---------- CASES ----------
print("Analyse af løsninger:\n")

# Case 1: Ingen løsning
if pivot == 0:
    print("Case: a + b = 0")
    print("→ Anden række bliver [0  0 | 4]")
    print("→ Inkonsistent system")
    print("→ INGEN LØSNING")

else:
    # Case 2: Entydig løsning
    print("Case: a + b ≠ 0")
    print("→ Entydig løsning\n")

    # Back substitution
    x2_sol = simplify(4 / (a + b))
    x1_sol = simplify(-1 + b * x2_sol)

    print("Back substitution:")
    print(f"x2 = {x2_sol}")
    print(f"x1 = {x1_sol}")

# ---------- Kommentar om uendeligt mange ----------
print("\nBemærkning:")
print("Uendeligt mange løsninger kan IKKE forekomme,")
print("da systemet har 2 ligninger og 2 variable.")
