from sympy import Matrix, symbols

def ref_solve(augmented):
    """
    REF-analyse af et lineært ligningssystem ud fra en augmented matrix [A|b].

    Input:
        augmented: list of lists eller sympy.Matrix
          fx [[1,2,3,4],
              [2,4,6,8]]

    Output:
        Printer REF + løsningstype + (evt.) parametrisk løsning.
    """
    A = augmented if isinstance(augmented, Matrix) else Matrix(augmented)

    rows, cols = A.shape
    n = cols - 1  # antal variable
    x = symbols(f"x1:{n+1}")

    print("Augmented matrix [A|b]:")
    print(A)
    print()

    # ---------- REF ----------
    REF = A.echelon_form()
    print("REF (Row Echelon Form):")
    print(REF)
    print()

    # ---------- Find pivotkolonner (fra REF) ----------
    pivot_cols = []
    for i in range(rows):
        for j in range(n):  # kun koefficient-delen
            if REF[i, j] != 0:
                pivot_cols.append(j)
                break

    pivot_cols = list(dict.fromkeys(pivot_cols))  # fjern evt. dubletter, behold orden
    free_cols = [j for j in range(n) if j not in pivot_cols]

    # ---------- Tjek inkonsistens: [0 ... 0 | c], c != 0 ----------
    inconsistent = False
    for i in range(rows):
        if all(REF[i, j] == 0 for j in range(n)) and REF[i, n] != 0:
            inconsistent = True
            break

    if inconsistent:
        print("Konklusion: INGEN løsning (inkonsistent række: 0 = c).")
        return

    # Hvis ingen inkonsistens:
    if len(free_cols) == 0 and len(pivot_cols) == n:
        print("Konklusion: UNIK løsning (ingen frie variabler).")
    else:
        print("Konklusion: UENDELIGT mange løsninger (frie variabler findes).")

    print(f"Pivotkolonner (0-baseret): {pivot_cols}")
    print(f"Frie variabler (0-baseret): {free_cols}")
    print()

    # ---------- Parametrisk løsning (brug RREF kun til at udtrykke pænt) ----------
    # (REF bruges til klassifikation; RREF gør udtrykket læsbart)
    RREF, pivots = A.rref()

    # lav parametre t1, t2, ...
    t = symbols(f"t1:{len(free_cols)+1}") if free_cols else []
    sol = [None] * n

    # sæt frie variable = parametre
    for k, col in enumerate(free_cols):
        sol[col] = t[k]

    # udtryk pivot-variable ud fra RREF
    for i, pcol in enumerate(pivots):
        expr = RREF[i, n]
        for col in free_cols:
            expr -= RREF[i, col] * sol[col]
        sol[pcol] = expr

    print("Parametrisk løsning:")
    for i in range(n):
        print(f"x{i+1} = {sol[i]}")

if __name__ == "__main__":
    # Eksempel (skift til din egen augmented matrix)
    # 3x +  y = 2
    #     y = 1
    aug = [
        [-2, 1, 1],
        [4,-2, 0]
    ]
    ref_solve(aug)
