"""Pruebas iniciales para mimatmul."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from mimatmul import mimatmul


def test_matrices_2x2():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    esperado = [[19, 22], [43, 50]]
    assert mimatmul(A, B) == esperado


def test_multiplicar_por_identidad():
    A = [[1, 2], [3, 4]]
    I = [[1, 0], [0, 1]]
    assert mimatmul(A, I) == A


def test_matrices_rectangulares():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    esperado = [[58, 64], [139, 154]]
    assert mimatmul(A, B) == esperado
