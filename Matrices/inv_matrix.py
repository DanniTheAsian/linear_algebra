from sympy import Matrix

def inverse_matrix(A):
    """
    Beregner den inverse af en matrix A, hvis den findes.
    
    Args:
        A (Matrix): SymPy matrix
    
    Returns:
        Matrix: A^{-1}
    """
    if A.det() == 0:
        raise ValueError("Matrixen er ikke invertibel (determinant = 0)")
    
    return A.inv()


# -------- EKSEMPEL --------
A = Matrix([
    [120, 140],
    [130, 130]
])

print("Matrix A:")
print(A)

A_inv = inverse_matrix(A)

print("\nInverse matrix A^(-1):")
print(A_inv)

#print("\nTjek: A * A^(-1) =")
#print(A * A_inv)
