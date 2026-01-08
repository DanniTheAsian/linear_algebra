from sympy import Matrix, symbols

# -------- INDSÆT MATRIX (augmented matrix) --------
A = Matrix([
    [1, 2, -1, 8],
    [2, 3, -1, 11],
    [-2, 0, -3, -3]
])

# Antal variable (sidste kolonne er højreside)
num_vars = A.cols - 1

# Variabelnavne x1, x2, x3, ...
variables = symbols(f"x1:{num_vars+1}")

# -------- RREF --------
rref_matrix, pivots = A.rref()

print("RREF:")
print(rref_matrix)
print("\nPivot kolonner:", pivots)

# -------- FIND LØSNING --------
solution = {}

for i, pivot_col in enumerate(pivots):
    solution[variables[pivot_col]] = rref_matrix[i, -1]

print("\nLøsning:")
for var in variables:
    if var in solution:
        print(f"{var} = {solution[var]}")
    else:
        print(f"{var} = fri variabel")
