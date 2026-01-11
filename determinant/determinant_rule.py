from sympy import symbols, Matrix, simplify

# Definér symboler
a, b, c, p, q, r, x, y, z = symbols('a b c p q r x y z')

# Matrix A
A = Matrix([
    [a, b, c],
    [p, q, r],
    [x, y, z]
])

print("Matrix A:")
print(A)
detA = A.det()
print("det(A) =", detA)
print()

# Matrix B
B = Matrix([
    [-2*a, -2*b, -2*c],
    [2*p + x, 2*q + y, 2*r + z],
    [3*x, 3*y, 3*z]
])

print("Matrix B:")
print(B)
detB_symbolic = B.det()
print("det(B) (symbolsk) =", detB_symbolic)
print()

# --- Trin-for-trin rækkeoperationer ---

# Faktor-tracking
factor = 1

# Regel 2: faktor ud af række 1 og 3
B1 = B.copy()
B1[0, :] = B1[0, :] / (-2)
factor *= -2

B1[2, :] = B1[2, :] / 3
factor *= 3

print("Efter at trække -2 ud af R1 og 3 ud af R3:")
print(B1)
print("Samlet faktor =", factor)
print()

# Regel 3: R2 <- R2 - R3 (ændrer ikke determinanten)
B2 = B1.copy()
B2[1, :] = B2[1, :] - B2[2, :]

print("Efter R2 <- R2 - R3:")
print(B2)
print("Samlet faktor =", factor)
print()

# Regel 2: faktor 2 ud af række 2
B3 = B2.copy()
B3[1, :] = B3[1, :] / 2
factor *= 2

print("Efter at trække 2 ud af R2:")
print(B3)
print("Samlet faktor =", factor)
print()

print("B3 er nu A")
print()

# --- Slutresultat ---
# Givet i opgaven:
detA_value = -1

detB_value = simplify(factor * detA_value)

print("Endeligt resultat:")
print("det(B) =", detB_value)
