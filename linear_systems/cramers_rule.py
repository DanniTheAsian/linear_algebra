from sympy import Matrix, Rational

def solve_cramers_rule(A: Matrix, b: Matrix, show_steps=True):
    """
    Solves Ax = b using Cramer's Rule.
    Works for any n×n system with det(A) ≠ 0.
    """

    if A.rows != A.cols:
        raise ValueError("Matrix A must be square")

    if b.cols != 1 or b.rows != A.rows:
        raise ValueError("b must be a column vector with same number of rows as A")

    n = A.rows
    detA = A.det()

    if show_steps:
        print("A =")
        print(A)
        print("\nb =")
        print(b)
        print(f"\ndet(A) = {detA}")

    if detA == 0:
        raise ValueError("Cramer's rule cannot be used (det(A)=0)")

    solution = Matrix.zeros(n, 1)

    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b  # replace column i with b
        detAi = Ai.det()

        xi = Rational(1, 1) * detAi / detA
        solution[i, 0] = xi

        if show_steps:
            print(f"\nA_{i+1} (replace column {i+1} with b):")
            print(Ai)
            print(f"det(A_{i+1}) = {detAi}")
            print(f"x{i+1} = det(A_{i+1}) / det(A) = {detAi}/{detA} = {xi}")

    return solution

if __name__ == "__main__":
    A = Matrix([
    [2, 1],
    [3,7]
])

b = Matrix([
    [1],
    [-2]
])

x = solve_cramers_rule(A, b)

print("\nLøsning x =")
print(x)
