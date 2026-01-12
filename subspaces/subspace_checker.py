from sympy import Matrix

# Keywords: subspace, span

def is_subspace_span(vectors):
    """
    Span(vectors) er altid et underrum (hvis vektorerne har samme dimension)
    """
    if not vectors:
        return False, "Span(empty) er ikke defineret"

    vectors = [Matrix(v) for v in vectors]
    dim = vectors[0].rows

    if any(v.rows != dim for v in vectors):
        return False, "Vektorerne har ikke samme dimension"

    return True, "Span af vektorer er altid et underrum"
