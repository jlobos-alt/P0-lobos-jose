"""Pruebas para mimatmul."""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from mimatmul import mimatmul


def test_caso_conocido():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    esperado = [[19, 22], [43, 50]]
    assert mimatmul(A, B) == esperado


def test_matrices_cuadradas():
    A = [[1, 0, 2], [0, 1, 0], [3, 1, 1]]
    B = [[2, 1, 0], [0, 2, 1], [1, 0, 3]]
    esperado = [
        [1 * 2 + 0 * 0 + 2 * 1, 1 * 1 + 0 * 2 + 2 * 0, 1 * 0 + 0 * 1 + 2 * 3],
        [0 * 2 + 1 * 0 + 0 * 1, 0 * 1 + 1 * 2 + 0 * 0, 0 * 0 + 1 * 1 + 0 * 3],
        [3 * 2 + 1 * 0 + 1 * 1, 3 * 1 + 1 * 2 + 1 * 0, 3 * 0 + 1 * 1 + 1 * 3],
    ]
    assert mimatmul(A, B) == esperado


def test_matrices_rectangulares():
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    esperado = [[58, 64], [139, 154]]
    assert mimatmul(A, B) == esperado


def test_consistente_con_numpy():
    rng = np.random.default_rng(42)
    for m, n, p in [(2, 3, 4), (5, 5, 5), (4, 2, 3)]:
        A = rng.random((m, n))
        B = rng.random((n, p))
        resultado = np.array(mimatmul(A.tolist(), B.tolist()))
        esperado = A @ B
        assert np.allclose(resultado, esperado, atol=1e-10)


def test_dimensiones_incompatibles():
    A = [[1, 2, 3], [4, 5, 6]]  # 2 x 3
    B = [[1, 2], [3, 4]]        # 2 x 2 (columnas de A != filas de B)
    with pytest.raises(ValueError, match="incompatibles"):
        mimatmul(A, B)


def test_matriz_vacia():
    with pytest.raises(ValueError, match="vacías"):
        mimatmul([], [[1, 2]])
