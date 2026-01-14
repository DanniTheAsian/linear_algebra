"""Solution Verification Module.

Verifies whether a given candidate solution satisfies a system of equations
by substituting into each equation.

Keywords:
    solution verification, equation checking, candidate solution,
    linear equations, consistency checking
"""
from sympy import symbols, Eq, simplify


def check_candidate_solution(equations, candidate, var_order=None, verbose=True):
    """
    Tjekker om en kandidat (x1,x2,x3,...) er en løsning til et ligningssystem.

    equations: liste af sympy Eq(...) fx [Eq(x1+x2,3), Eq(x2-x3,2)]
    candidate: dict fx {x1: 2, x2: 1, x3: 0}
    var_order: valgfri liste til pæn print-rækkefølge, fx [x1,x2,x3]
    """
    all_ok = True

    if verbose:
        if var_order is None:
            var_order = list(candidate.keys())
        print("Kandidat:")
        print(", ".join([f"{v} = {candidate[v]}" for v in var_order]))
        print()

    for i, eq in enumerate(equations, start=1):
        lhs_val = simplify(eq.lhs.subs(candidate))
        rhs_val = simplify(eq.rhs.subs(candidate))
        ok = (lhs_val == rhs_val)

        if verbose:
            print(f"Ligning {i}: {eq}")
            print(f"  LHS = {lhs_val}, RHS = {rhs_val}  -->  {'✅ OK' if ok else '❌ IKKE OK'}")
            print()

        all_ok = all_ok and ok

    if verbose:
        print("Konklusion:", "✅ Kandidaten ER en løsning." if all_ok else "❌ Kandidaten ER IKKE en løsning.")

    return all_ok


if __name__ == "__main__":
    # --- Variabler ---
    x1, x2, x3 = symbols("x1 x2 x3")

    # --- Ligningssystem (som på dit billede) ---
    equations = [
        Eq(3*x1 + 2*x2 + x3, 8),
        Eq(3*x1 + 3*x2 - x3, 4),
        Eq(2*x1 + 2*x2 + 2*x3, 4),
    ]

    # --- Kandidat (x1,x2,x3) = (2,1,0) ---
    candidate = {x1: -3, x2: 4, x3: 2}

    check_candidate_solution(equations, candidate, var_order=[x1, x2, x3])
