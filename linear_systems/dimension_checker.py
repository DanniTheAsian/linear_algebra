from sympy import Matrix

# Keywords: matrix dimensions, matrix multiplication

def dimension_checker(A=None, B=None, x=None):
    """
    Checks whether matrix products are defined and explains why.

    Args:
        A (Matrix): matrix A
        B (Matrix): matrix B
        x (Matrix): vector x (column vector)
    """

    print("=== DIMENSION CHECKER ===\n")

    # Helper to print shape
    def shape(M, name):
        r, c = M.shape
        print(f"{name} has shape {r} x {c}")
        return r, c

    # Check A * x
    if A is not None and x is not None:
        print("Checking A * x:")
        rA, cA = shape(A, "A")
        rx, cx = shape(x, "x")

        if cA == rx and cx == 1:
            print("✔ A * x is defined")
            print(f"Resulting vector has shape {rA} x 1\n")
        else:
            print("❌ A * x is NOT defined")
            print("Reason: number of columns of A must equal number of rows of x\n")

    # Check A * B
    if A is not None and B is not None:
        print("Checking A * B:")
        rA, cA = shape(A, "A")
        rB, cB = shape(B, "B")

        if cA == rB:
            print("✔ A * B is defined")
            print(f"Resulting matrix has shape {rA} x {cB}\n")
        else:
            print("❌ A * B is NOT defined")
            print("Reason: number of columns of A must equal number of rows of B\n")

    # Check B * A
    if A is not None and B is not None:
        print("Checking B * A:")
        rB, cB = shape(B, "B")
        rA, cA = shape(A, "A")

        if cB == rA:
            print("✔ B * A is defined")
            print(f"Resulting matrix has shape {rB} x {cA}\n")
        else:
            print("❌ B * A is NOT defined")
            print("Reason: number of columns of B must equal number of rows of A\n")


# ------------------ EXAMPLE ------------------

A = Matrix([[1, 2, 3],
            [4, 5, 6]])      # 2 x 3

B = Matrix([[1, 2],
            [3, 4],
            [5, 6]])        # 3 x 2

x = Matrix([1, 2, 3])       # 3 x 1

dimension_checker(A=A, B=B, x=x)
