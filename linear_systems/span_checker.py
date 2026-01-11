from sympy import Matrix, symbols

def span_checker(vectors, target):
    """
    Checks whether target is in the span of the given vectors.

    Args:
        vectors (list[list or tuple]): Basis vectors [x1, x2, ..., xk]
        target (list or tuple): Target vector v

    Prints:
        - Whether target is in the span
        - The linear combination if it exists
        - Parametric solution if infinite solutions
    """

    # Number of vectors
    k = len(vectors)

    # Create symbols for coefficients
    coeffs = symbols(f'c1:{k+1}')

    # Build matrix with vectors as columns
    A = Matrix(vectors).T
    b = Matrix(target)

    # Augmented matrix
    Aug = A.row_join(b)

    print("Augmented matrix [A | v]:")
    print(Aug)
    print()

    # RREF
    rref_matrix, pivots = Aug.rref()

    print("RREF of augmented matrix:")
    print(rref_matrix)
    print()

    # Check consistency
    rows, cols = rref_matrix.shape
    for i in range(rows):
        if all(rref_matrix[i, j] == 0 for j in range(cols - 1)) and rref_matrix[i, -1] != 0:
            print("❌ Target vector is NOT in the span (inconsistent system).")
            return

    print("✅ Target vector IS in the span.")

    # Read solutions
    free_vars = set(range(k)) - set(pivots)

    if not free_vars:
        print("✔ Unique linear combination:")
        for i, c in enumerate(coeffs):
            value = rref_matrix[i, -1]
            print(f"{c} = {value}")
    else:
        print("✔ Infinite solutions (parametric form):")
        for i, c in enumerate(coeffs):
            if i in pivots:
                expr = rref_matrix[pivots.index(i), -1]
                for j in free_vars:
                    expr -= rref_matrix[pivots.index(i), j] * coeffs[j]
                print(f"{c} = {expr}")
            else:
                print(f"{c} = free parameter")

    print()
    print("Linear combination:")
    combo = sum(coeffs[i] * Matrix(vectors[i]) for i in range(k))
    print("v =", combo)


# ------------------ EXAMPLE ------------------

x1 = [2, 1, -1]
x2 = [1, 0, 1]
x3 = [1, 1, -2]
v  = [0, 1, -3]

span_checker([x1, x2, x3], v)
