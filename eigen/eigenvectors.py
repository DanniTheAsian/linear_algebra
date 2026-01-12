from sympy import Matrix


def eigenvectors_matrix(matrix):
    """
    Compute eigenvalues and eigenvectors of a square matrix.

    Args:
        matrix (list[list[int | float]]): Square matrix A

    Returns:
        list of tuples:
        (eigenvalue, multiplicity, [eigenvectors])
    """
    A = Matrix(matrix)
    return A.eigenvects()


if __name__ == "__main__":
    # Example matrix
    A = [
        [7, 6],
        [1, 2]
    ]

    print("Matrix A:")
    print(Matrix(A))

    print("\nEigenvalues and eigenvectors:")

    eigen_data = eigenvectors_matrix(A)

    for eigenvalue, multiplicity, eigenvectors in eigen_data:
        print(f"\nEigenvalue λ = {eigenvalue}")
        print(f"Algebraic multiplicity: {multiplicity}")
        print("Eigenvector(s):")

        for v in eigenvectors:
            print(v)
