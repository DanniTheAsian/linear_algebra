from sympy import Matrix, symbols

# Keywords: parametric form, free variables, lead variables

def parametric_form(A, b):
    n = A.shape[1]
    vars = symbols(f'x1:{n+1}')

    Aug = A.row_join(b)
    print("Augmented matrix:")
    print(Aug)
    print()

    rref_matrix, pivots = Aug.rref()
    print("RREF:")
    print(rref_matrix)
    print()

    pivot_cols = list(pivots)
    free_vars = [i for i in range(n) if i not in pivot_cols]

    print("Pivot variables:", [vars[i] for i in pivot_cols])
    print("Free variables:", [vars[i] for i in free_vars])
    print()

    params = symbols(f't1:{len(free_vars)+1}')
    solution = {}

    for row, col in enumerate(pivot_cols):
        expr = rref_matrix[row, -1]
        for j, free_col in enumerate(free_vars):
            expr -= rref_matrix[row, free_col] * params[j]
        solution[vars[col]] = expr

    for j, free_col in enumerate(free_vars):
        solution[vars[free_col]] = params[j]

    print("Parametric form:")
    for var in vars:
        print(f"{var} = {solution[var]}")

    return solution


if __name__ == "__main__":
    A = Matrix([
        [3,1, 2],
        [6,2, 4],
        [1,0,1]
    ])

    b = Matrix([
        [5],
        [10],
        [2]
    ])

    parametric_form(A, b)
