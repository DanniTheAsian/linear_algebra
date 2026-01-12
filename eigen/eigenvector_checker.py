from sympy import Matrix

# Keywords: eigenvector, eigenvalue

def verify_eigenvector(A, v):
    """
    Verify whether v is an eigenvector of A by checking Av = λv.
    Prints steps and returns (is_eigenvector, lambda_value or None).
    """
    A = Matrix(A)
    v = Matrix(v)

    print("Matrix A:")
    print(A)
    print("\nVector v:")
    print(v)

    Av = A * v
    print("\nCompute Av:")
    print(Av)

    # Find lambda from a nonzero entry in v
    lam = None
    for i in range(v.rows):
        if v[i] != 0:
            lam = Av[i] / v[i]
            break

    if lam is None:
        print("\nVector v is the zero vector -> not an eigenvector.")
        return False, None

    print(f"\nCandidate λ from first nonzero component: λ = {lam}")

    # Check Av == λv
    if Av == lam * v:
        print("\nCheck Av == λv: TRUE")
        print(f"Therefore v is an eigenvector with eigenvalue λ = {lam}")
        return True, lam
    else:
        print("\nCheck Av == λv: FALSE")
        print("Therefore v is NOT an eigenvector of A")
        return False, None


if __name__ == "__main__":
    # Matrix from the task (image)
    A = [
        [7, 6],
        [6, -2]
    ]

    # v = [-1, 2]^T
    v = [-1, 2]

    verify_eigenvector(A, v)
