from sympy import Matrix

# Keywords: eigenvalues, characteristic equation

def eigenvalues_matrix(matrix):
    A = Matrix(matrix)
    return A.eigenvals()


if __name__ == "__main__":
    A = [
        [2, 1],
        [1, 2]
    ]

    print("Matrix A:")
    print(Matrix(A))

    print("\nEigenvalues (with multiplicity):")
    eigenvals = eigenvalues_matrix(A)
    for val, mult in eigenvals.items():
        print(f"λ = {val}, multiplicity = {mult}")
