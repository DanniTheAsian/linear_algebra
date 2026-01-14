"""Homogeneous System Analysis Module.

Analyzes homogeneous systems Ax = 0 to determine solution types:
trivial solution only vs. infinitely many solutions.

Keywords:
    homogeneous system, trivial solution, nontrivial solution, nullspace,
    rank-nullity, RREF, free variables
"""
from sympy import Matrix


def analyze_homogeneous_system(A):
    """
    Analyze the homogeneous system Ax = 0.

    Args:
        A (list[list[int | float]]): Coefficient matrix

    Returns:
        dict with keys:
        - 'rank'
        - 'num_variables'
        - 'solution_type'
    """
    A = Matrix(A)

    # RREF of A (no augmented column needed for homogeneous system)
    rref_matrix, pivots = A.rref()

    rank = len(pivots)
    num_variables = A.cols

    if rank == num_variables:
        solution_type = "Only trivial solution"
    else:
        solution_type = "Infinitely many solutions"

    return {
        "rank": rank,
        "num_variables": num_variables,
        "solution_type": solution_type
    }


if __name__ == "__main__":
    # ---------- Example 1: Only trivial solution ----------
    A1 = [
        [1, 0],
        [0, 1]
    ]

    result = analyze_homogeneous_system(A1)

    print("Matrix A1:")
    print(Matrix(A1))
    print("Result:", result)

    # ---------- Example 2: Infinitely many solutions ----------
    A2 = [
        [1, 2],
        [2, 4]
    ]

    result = analyze_homogeneous_system(A2)

    print("\nMatrix A2:")
    print(Matrix(A2))
    print("Result:", result)
