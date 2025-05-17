"""Simple script to compute XX^T (Gram matrix) using naive loops.

This is a placeholder implementation in pure Python as the original
algorithm from the paper "$XX^t$ Can Be Faster" is not available.

Usage:
    python3 xx_fast.py

The script generates a random matrix and computes the Gram matrix using
naive multiplication implemented with nested loops.
"""

import random
from typing import List

Matrix = List[List[float]]


def gram_matrix(x: Matrix) -> Matrix:
    """Compute X * X^T for a matrix X represented as nested lists."""
    n = len(x)
    m = len(x[0]) if x else 0
    result: Matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0.0
            for k in range(m):
                s += x[i][k] * x[j][k]
            result[i][j] = s
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
