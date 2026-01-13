from sympy import Matrix

# Keywords: linear systems, consistent, inconsistent, overdetermined, underdetermined

def analyze_linear_system(A):
    """
    Analyserer et lineært ligningssystem givet ved en augmented matrix.
    """

    # Antal ligninger og variable
    m = A.rows
    n = A.cols - 1  # sidste kolonne er konstantled

    # Klassifikation
    if m < n:
        system_type = "Underdetermined"
    elif m > n:
        system_type = "Overdetermined"
    else:
        system_type = "Neither (same number of equations and variables)"

    # Koefficient- og konstantmatrix
    A_coeff = A[:, :-1]
    b = A[:, -1]

    # Antal entries
    coeff_entries = A_coeff.rows * A_coeff.cols
    constant_entries = b.rows * 1

    # Print resultat
    print("Analysis of linear system")
    print("-------------------------")
    print(f"Number of equations (m): {m}")
    print(f"Number of variables (n): {n}")
    print(f"System type: {system_type}")
    print()
    print(f"Number of entries in coefficient matrix: {coeff_entries}")
    print(f"Number of entries in constant matrix: {constant_entries}")




# -------- EKSEMPEL --------
A = Matrix([
    [1, 1, 1, 0],
    [-9, 2, 1, 0],
    [-3, 2, 4, 0]
])

analyze_linear_system(A)
