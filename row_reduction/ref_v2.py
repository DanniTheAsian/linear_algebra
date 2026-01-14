from sympy import Matrix, symbols

def ref_analyze(A):
    """
    REF-analyse af et lineært ligningssystem givet ved en augmented matrix.
    Matcher eksamensstil (pivot = 1, kun elimination under).
    """
    A = Matrix(A)
    rows, cols = A.shape
    n = cols - 1  # antal variable
    x = symbols(f"x1:{n+1}")

    print("Augmented matrix [A|b]:")
    print(A)
    print()

    # ---------- REF (exam style) ----------
    r = 0
    for c in range(n):
        if r >= rows:
            break

        # find pivot
        for i in range(r, rows):
            if A[i, c] != 0:
                A.row_swap(r, i)
                break
        else:
            continue

        # pivot = 1
        pivot = A[r, c]
        A.row_op(r, lambda v, _: v / pivot)

        # eliminer under pivot
        for i in range(r + 1, rows):
            factor = A[i, c]
            A.row_op(i, lambda v, j: v - factor * A[r, j])

        r += 1

    print("REF (Row Echelon Form):")
    print(A)
    print()

    # ---------- Tjek inkonsistens ----------
    for i in range(rows):
        if all(A[i, j] == 0 for j in range(n)) and A[i, n] != 0:
            print("🔴 Konklusion: INGEN løsning")
            print("Forklaring: Række af typen [0 0 ... 0 | c], c ≠ 0")
            return

    # ---------- Find pivot- og frie variabler ----------
    pivot_cols = []
    for i in range(rows):
        for j in range(n):
            if A[i, j] == 1:
                pivot_cols.append(j)
                break

    free_vars = [j for j in range(n) if j not in pivot_cols]

    if len(pivot_cols) == n:
        print("🟢 Konklusion: UNIK løsning")
        print("Forklaring: Pivot i hver variabel → ingen frie variabler")
    else:
        print("🟡 Konklusion: UENDELIGT mange løsninger")
        print("Forklaring: Mindst én fri variabel")
        print("Frie variabler:")
        for j in free_vars:
            print(f"x{j+1}")

if __name__ == "__main__":
    A = [
        [1, -2, 3],
        [2, -1, 0]
    ]

    ref_analyze(A)
