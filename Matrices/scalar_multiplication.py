"""Scalar Multiplication Module.

Performs scalar multiplication on matrices, scaling all entries by a given scalar value.

Keywords:
    scalar multiplication, matrix scaling, scalar product,
    matrix operations, linear algebra
"""
from typing import List, Union

# Keywords: scalar multiplication, matrix algebra

Number = Union[int, float]
Matrix = List[List[Number]]


def scalar_multiply_matrix(scalar: Number, matrix: Matrix) -> Matrix:
    """
    Multiply a scalar with a matrix.

    Args:
        scalar (int | float): The scalar value.
        matrix (list[list[int | float]]): The matrix to multiply.

    Returns:
        Matrix: A new matrix where every entry is multiplied by `scalar`.
    """
    result: Matrix = []

    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(scalar * value)
        result.append(new_row)

    return result


def print_matrix(matrix: Matrix) -> None:
    """Print matrix row by row."""
    for row in matrix:
        print(row)


if __name__ == "__main__":
    # Scalar
    k = 3

    # Matrix (2x2)
    A: Matrix = [
        [1, 2],
        [3, 4]
    ]

    print("Original matrix A:")
    print_matrix(A)

    print("\nScalar:", k)

    print("\nResult of scalar multiplication k * A:")
    result = scalar_multiply_matrix(k, A)
    print_matrix(result)
