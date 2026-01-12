from sympy import Matrix, symbols

# -------- INDSÆT AUGMENTED MATRIX --------
A = Matrix([
    [3,2,5],
    [2,0,6],
    [-1,5,-13],
])

# Antal variable
num_vars = A.cols - 1
variables = symbols(f"x1:{num_vars+1}")

# Split matrix
A_coeff = A[:, :-1]   # koefficientmatrix
b = A[:, -1]          # højreside

# -------- RANK --------
rank_A = A_coeff.rank()
rank_aug = A.rank()

# -------- RREF --------
rref_matrix, pivots = A.rref()

print("RREF:")
print(rref_matrix)

print("\nRank(A) =", rank_A)
print("Rank([A|b]) =", rank_aug)

# -------- LØSNINGSKLASSIFIKATION --------
print("\nLøsningstype:")

if rank_A < rank_aug:
    print("→ Ingen løsning (inkonsistent system)")

elif rank_A == rank_aug == num_vars:
    print("→ Entydig løsning")

    print("\nLøsning:")
    for i, pivot_col in enumerate(pivots):
        print(f"{variables[pivot_col]} = {rref_matrix[i, -1]}")

else:
    print("→ Uendeligt mange løsninger")

    print("\nBasis- og frie variable:")
    pivot_vars = [variables[i] for i in pivots]
    free_vars = [v for v in variables if v not in pivot_vars]

    print("Basisvariable:", pivot_vars)
    print("Frie variable:", free_vars)
