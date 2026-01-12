from sympy import Matrix

def determinant_cofactor_expansion(A, axis="col", index=1): #ændres efter behov axis og index
    """
    Computes det(A) using cofactor expansion (Laplace expansion)
    along a chosen row or column.
    """

    if A.rows != A.cols:
        raise ValueError("Matrix must be square")

    n = A.rows

    # ----- Base cases -----
    if n == 1:
        print(f"det({A}) = {A[0,0]}")
        return A[0,0]

    if n == 2:
        det = A[0,0]*A[1,1] - A[0,1]*A[1,0]
        print(f"det({A}) = {det}")
        return det

    det_val = 0
    axis = axis.lower()

    if axis == "row":
        i = index
        print(f"\nCofactor expansion along ROW {i+1}\n")

        for j in range(n):
            a = A[i, j]
            if a == 0:
                continue  # skip zero terms

            minor = A.minor_submatrix(i, j)
            sign = (-1)**(i + j)
            cofactor = sign * minor.det()

            print(f"a{i+1}{j+1} = {a}")
            print("minor:")
            print(minor)
            print(f"cofactor c{i+1}{j+1} = {cofactor}\n")

            det_val += a * cofactor

    elif axis == "col":
        j = index
        print(f"\nCofactor expansion along COL {j+1}\n")

        for i in range(n):
            a = A[i, j]
            if a == 0:
                continue  # skip zero terms

            minor = A.minor_submatrix(i, j)
            sign = (-1)**(i + j)
            cofactor = sign * minor.det()

            print(f"a{i+1}{j+1} = {a}")
            print("minor:")
            print(minor)
            print(f"cofactor c{i+1}{j+1} = {cofactor}\n")

            det_val += a * cofactor

    else:
        raise ValueError("axis must be 'row' or 'col'")

    print(f"det(A) = {det_val}")
    return det_val

# -------- Example (fra dit billede) --------

A = Matrix([
    [-3, 0, 0],
    [4, 1, 0],
    [-1, 4, -4]
])

determinant_cofactor_expansion(A)
