from sympy import Matrix, symbols, pprint

def polynomial_interpolation(points):
    """
    Finds the interpolating polynomial of degree n-1
    using a Vandermonde system and prints all steps.
    """
    x = symbols('x')

    n = len(points)

    # Build Vandermonde matrix and RHS vector
    V = []
    b = []

    for xi, yi in points:
        V.append([xi**k for k in range(n)])
        b.append(yi)

    V = Matrix(V)
    b = Matrix(b)

    print("Vandermonde matrix V:")
    pprint(V)

    print("\nRight-hand side vector b:")
    pprint(b)

    # Solve system
    coeffs = V.LUsolve(b)

    print("\nCoefficients:")
    for i, c in enumerate(coeffs):
        print(f"r{i} = {c}")

    # Build polynomial
    p = sum(coeffs[i] * x**i for i in range(n))

    print("\nInterpolating polynomial p(x):")
    pprint(p)

    return p


def evaluate_polynomial(p, value):
    """
    Evaluates polynomial p at x = value
    """
    x = symbols('x')
    result = p.subs(x, value)

    print(f"\np({value}) = {result}")
    return result


# -------- Problem 2.a (fra billedet) --------

points = [
    (0, 2),
    (1, 2.03),
    (2, -0.40),
    (-1, 0.89)
]

p = polynomial_interpolation(points)

# Estimate y for x = 1.5
evaluate_polynomial(p, 1.5)
