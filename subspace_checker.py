from sympy import Matrix


def is_subspace(vectors):
    """
    Check whether a set of vectors forms a subspace of R^n.

    Args:
        vectors (list[list[int | float]]): List of vectors

    Returns:
        dict with keys:
        - 'is_subspace' (bool)
        - 'contains_zero_vector' (bool)
        - 'closed_under_addition' (bool)
        - 'closed_under_scalar_multiplication' (bool)
    """
    # Convert vectors to SymPy column vectors
    vectors = [Matrix(v) for v in vectors]

    dim = vectors[0].rows
    zero_vector = Matrix.zeros(dim, 1)

    # 1️⃣ Check zero vector
    contains_zero = zero_vector in vectors

    # 2️⃣ Check closure under addition (pairwise)
    closed_add = True
    for v in vectors:
        for u in vectors:
            if v + u not in vectors:
                closed_add = False
                break

    # 3️⃣ Check closure under scalar multiplication (test few scalars)
    closed_scalar = True
    test_scalars = [2, -1]
    for v in vectors:
        for c in test_scalars:
            if c * v not in vectors:
                closed_scalar = False
                break

    is_sub = contains_zero and closed_add and closed_scalar

    return {
        "is_subspace": is_sub,
        "contains_zero_vector": contains_zero,
        "closed_under_addition": closed_add,
        "closed_under_scalar_multiplication": closed_scalar
    }


if __name__ == "__main__":
    # ---------- Example 1: Subspace ----------
    V1 = [
        [0, 0],
        [1, 0],
        [2, 0],
        [-1, 0]
    ]

    print("Set V1:")
    result = is_subspace(V1)
    print(result)

    # ---------- Example 2: Not a subspace ----------
    V2 = [
        [1, 1],
        [2, 2]
    ]

    print("\nSet V2:")
    result = is_subspace(V2)
    print(result)
