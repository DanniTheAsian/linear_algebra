from sympy import Matrix, symbols

# -------- INDSÆT AUGMENTED MATRIX --------
A = Matrix([
    [1, 3, 1, 1, 8],
    [2, -2, 1,2, 8],
    [3,1,2,-1,-1]
])

num_vars = A.cols - 1
variables = symbols(f"x1:{num_vars+1}")

A_coeff = A[:, :-1]

rank_A = A_coeff.rank()
rank_aug = A.rank()

rref_matrix, pivots = A.rref()

print("RREF:")
print(rref_matrix)

print("\nRank(A) =", rank_A)
print("Rank([A|b]) =", rank_aug)

print("\nResultat:")

if rank_A < rank_aug:
    print("→ INKONSISTENT system (ingen løsning)")

elif rank_A == rank_aug == num_vars:
    print("→ KONSISTENT med ENTydig (unik) løsning\n")
    for i, pivot_col in enumerate(pivots):
        if pivot_col < num_vars:
            print(f"{variables[pivot_col]} = {rref_matrix[i, -1]}")

else:
    print("→ KONSISTENT med UENDELIGT mange løsninger")
