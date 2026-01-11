from sympy import Matrix

def classify_system(A, b):
    """
    Classify a linear system Ax = b.

    Args:
        A (list[list[int | float]]): Coefficient matrix
        b (list[int | float]): Right-hand side vector

    Returns:
        str: 'unique solution', 'infinitely many solutions', or 'no solution'
    """
    # Build augmented matrix [A | b]
    augmented = Matrix(A).row_join(Matrix(b))

    # Compute RREF
    rref_matrix, pivots = augmented.rref()

    num_vars = Matrix(A).cols

    # Check for inconsistency: [0 0 ... 0 | c], c != 0
    for row in rref_matrix.tolist():
        if all(x == 0 for x in row[:-1]) and row[-1] != 0:
            return "No solution"

    # If number of pivots == number of variables → unique solution
    if len(pivots) == num_vars:
        return "Unique solution"

    # Otherwise → infinitely many solutions
    return "Infinitely many solutions"


if __name__ == "__main__":
    # ---------- Example 1: Unique solution ----------
    A1 = [
        [2, 1],
        [1, -1]
    ]
    b1 = [3, 0]

    print("System 1:", classify_system(A1, b1))

    # ---------- Example 2: Infinitely many solutions ----------
    A2 = [
        [1, 2],
        [2, 4]
    ]
    b2 = [3, 6]

    print("System 2:", classify_system(A2, b2))

    # ---------- Example 3: No solution ----------
    A3 = [
        [1, 2],
        [2, 4]
    ]
    b3 = [3, 5]

    print("System 3:", classify_system(A3, b3))
