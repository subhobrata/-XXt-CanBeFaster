"""Example script to compute the Gram matrix ``X X^T``.

This is **not** the official implementation from the paper
``$XX^t$ Can Be Faster``.  The paper does not provide source code, so the
algorithm below is a simplified placeholder.  It demonstrates how one
might compute the Gram matrix using pure Python while exploiting the
symmetry of ``X X^T`` to reduce work.

Usage::

    python3 xx_fast.py

The script generates a random matrix and prints its Gram matrix.
"""

import random
from typing import List

Matrix = List[List[float]]


def dot(a: List[float], b: List[float]) -> float:
    """Return the dot product of two vectors."""
    s = 0.0
    for x, y in zip(a, b):
        s += x * y
    return s


def gram_matrix(x: Matrix) -> Matrix:
    """Compute ``X X^T`` for ``X`` represented as a list of lists.

    Only the upper-triangular part is computed explicitly; the symmetric
    entries are mirrored.  While still O(n^2 m) in complexity, this saves
    roughly half of the inner-product evaluations compared to a naive
    double loop.
    """

    n = len(x)
    result: Matrix = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            s = dot(x[i], x[j])
            result[i][j] = s
            result[j][i] = s

    return result


def random_matrix(rows: int, cols: int, seed: int = 0) -> Matrix:
    random.seed(seed)
    return [[random.random() for _ in range(cols)] for _ in range(rows)]


def main() -> None:
    x = random_matrix(4, 3)
    g = gram_matrix(x)
    for row in g:
        print(" ".join(f"{v:.4f}" for v in row))


if __name__ == "__main__":
    main()
