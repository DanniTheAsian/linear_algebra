from sympy import Matrix

# Keywords: determinant, cofactor, Laplace expansion, adjungeret matrix

def determinant_cofactor_expansion(A, axis="col", index=0):
    """
    Computes det(A) using cofactor expansion (Laplace expansion)
    along a chosen row or column.
    """

    if A.rows != A.cols:
        raise ValueError("Matrix must be square")

    n = A.rows

    # ----- Base cases -----
    if n == 1:
        print(f"det(A) = {A[0,0]}")
        return A[0,0]

    if n == 2:
        det = A[0,0]*A[1,1] - A[0,1]*A[1,0]
        print(f"det(A) = {det}")
        return det

    det_val = 0
    axis = axis.lower()

    if axis == "row":
        i = index
        print(f"\nCofactor expansion along ROW {i+1}\n")

        for j in range(n):
            a = A[i, j]
            if a == 0:
                continue

            minor = A.minor_submatrix(i, j)
            cofactor = (-1)**(i + j) * minor.det()

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
                continue

            minor = A.minor_submatrix(i, j)
            cofactor = (-1)**(i + j) * minor.det()

            print(f"a{i+1}{j+1} = {a}")
            print("minor:")
            print(minor)
            print(f"cofactor c{i+1}{j+1} = {cofactor}\n")

            det_val += a * cofactor

    else:
        raise ValueError("axis must be 'row' or 'col'")

    print(f"det(A) = {det_val}")
    return det_val


def print_cofactor(A, i, j):
    """
    Prints and computes the cofactor c_{ij}(A)
    """
    print(f"\nComputations for c{i+1}{j+1}(A):")

    minor = A.minor_submatrix(i, j)
    sign = (-1)**(i + j)
    det_minor = minor.det()
    cofactor = sign * det_minor

    print(f"c{i+1}{j+1}(A) = (-1)^({i+1}+{j+1}) * det(minor)")
    print("minor:")
    print(minor)
    print(f"= {sign} * ({det_minor})")
    print(f"= {cofactor}")

    return cofactor


def inverse_entry(A, i, j, detA=None):
    """
    Prints and computes the (i,j)-entry of A^{-1}
    using (A^{-1})_ij = c_ji / det(A)
    """
    if detA is None:
        detA = determinant_cofactor_expansion(A)

    print(f"\nComputing (A^-1)_{i+1}{j+1}:")
    print(f"(A^-1)_{i+1}{j+1} = c{j+1}{i+1} / det(A)")

    cji = print_cofactor(A, j, i)
    value = cji / detA

    print(f"(A^-1)_{i+1}{j+1} = {cji}/{detA} = {value}")

    return value


# -------- Example (kan udskiftes med ALLE matricer) --------

A = Matrix([
    [1, 2, -1],
    [3,1,1],
    [0,4,7]
])

print("Matrix A:")
print(A)

detA = determinant_cofactor_expansion(A)

# Directly ask for inverse entries (no manual index thinking!)
a11 = inverse_entry(A, 0, 0, detA)
a23 = inverse_entry(A, 1, 2, detA)
