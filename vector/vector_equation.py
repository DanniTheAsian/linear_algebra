from sympy import Matrix, symbols

def system_to_vector_equation(A):
    """
    Omskriver et lineært ligningssystem til vektorligning:
    x1*v1 + x2*v2 + ... = b
    """

    rows, cols = A.shape
    num_vars = cols - 1  # sidste kolonne er konstantled

    # Variable x1, x2, ...
    variables = symbols(f"x1:{num_vars+1}")

    # Koefficient-matrix og højreside
    coeffs = A[:, :-1]
    b = A[:, -1]

    print("Vektorligning:")
    print()

    terms = []
    for i in range(num_vars):
        column_vector = coeffs[:, i]
        terms.append(f"{variables[i]} * {column_vector}")

    left_side = " + ".join(terms)

    print(left_side, " = ", b)


if __name__ == "__main__":
    # ----- EKSEMPEL FRA OPGAVEN -----
    # x1 - x2 + 3x3 = 5
    # -3x1 + x2 + x3 = -6
    # 5x1 - 8x2      = 9

    A = Matrix([
        [ 1, -1,  3,  5],
        [-3,  1,  1, -6],
        [ 5, -8,  0,  9]
    ])

    system_to_vector_equation(A)
