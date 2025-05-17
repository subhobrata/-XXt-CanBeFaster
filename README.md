# -XXt-CanBeFaster

This repository contains a **placeholder** implementation related to the
paper "$XX^t$ Can Be Faster". The original paper is included as
`2505.09814v1.pdf`, but no official code was provided.  The script
`xx_fast.py` shows one way to compute the Gram matrix `X X^T` in pure
Python.  It is not meant to reproduce the full algorithm from the paper
and merely demonstrates the idea using symmetry to avoid duplicate
computations.

To run the example:

```bash
python3 xx_fast.py
```

The script generates a small random matrix and outputs its Gram matrix.

