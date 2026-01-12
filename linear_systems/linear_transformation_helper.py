from sympy import Matrix, symbols

# Keywords: linear transformation, linearity, basis vectors

def linear_transformation_helper(x1, x2, y, Tx1, Tx2):
    """
    Computes T(y) using linearity:
        y = a*x1 + b*x2  ==>  T(y) = a*T(x1) + b*T(x2)

    Args:
        x1, x2 : basis vectors in R^n
        y      : target vector in R^n
        Tx1    : T(x1)
        Tx2    : T(x2)
    """

    # Step 1: Solve y = a*x1 + b*x2  -->  [x1 x2 | y]
    A = Matrix([x1, x2]).T          # coefficient matrix
    b = Matrix(y)                   # constant vector

    Aug = A.row_join(b)

    print("Augmented matrix [x1 x2 | y]:")
    print(Aug)
    print()

    rref, pivots = Aug.rref()

    print("RREF:")
    print(rref)
    print()

    # Check consistency
    rows, cols = rref.shape
    for i in range(rows):
        if all(rref[i, j] == 0 for j in range(cols - 1)) and rref[i, -1] != 0:
            print("❌ y cannot be written as a linear combination of x1 and x2")
            return

    # Read coefficients
    a = rref[0, -1]
    b_coeff = rref[1, -1]

    print(f"Solution:")
    print(f"a = {a}")
    print(f"b = {b_coeff}")
    print()

    # Step 2: Compute T(y)
    Ty = a * Matrix(Tx1) + b_coeff * Matrix(Tx2)

    print("Using linearity:")
    print("T(y) = a*T(x1) + b*T(x2)")
    print()
    print("T(y) =")
    print(Ty)

    return Ty


# ------------------ EXAMPLE ------------------

x1  = [1, 1, 0]
x2  = [0, -1, 1]
y   = [1, 3, -2]

Tx1 = [1, 2]
Tx2 = [-2, 1]

linear_transformation_helper(x1, x2, y, Tx1, Tx2)
