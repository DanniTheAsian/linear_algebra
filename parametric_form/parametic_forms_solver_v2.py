from sympy import symbols, Eq, solve

def parametric_solution_from_equation(equation, variables):
    """
    Finder parametrisk løsning på to måder for én lineær ligning.

    equation: sympy Eq(...) fx Eq(3*x1 + x2, 2)
    variables: liste af sympy-symboler fx [x1, x2]
    """

    if len(variables) != 2:
        raise ValueError("Denne funktion er lavet til én ligning med to variable")

    x, y = variables
    alpha, beta = symbols("alpha beta", real=True)

    print("Givet ligning:")
    print(equation)

    print("\n--- Metode 1: Isolér", x, "---")
    x_expr = solve(equation, x)[0]
    x_param = x_expr.subs(y, beta)
    print(f"{x} = {x_param}")
    print(f"{y} = {beta}")

    print("\n--- Metode 2: Isolér", y, "---")
    y_expr = solve(equation, y)[0]
    y_param = y_expr.subs(x, alpha)
    print(f"{x} = {alpha}")
    print(f"{y} = {y_param}")


if __name__ == "__main__":
    # ----- Eksempel: 3x1 + x2 = 2 -----
    x1, x2 = symbols("x1 x2")
    eq = Eq(2*x1 + 3*x2, 1)

    parametric_solution_from_equation(eq, [x1, x2])
