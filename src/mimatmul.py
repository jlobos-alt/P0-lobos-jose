"""mimatmul: multiplicación de matrices en Python puro."""


def mimatmul(A, B):
    """Multiplica dos matrices A (m x n) y B (n x p) usando listas de listas.

    Devuelve la matriz C (m x p) donde C[i][j] = sum_k A[i][k] * B[k][j].

    Parámetros
    ----------
    A, B : listas de listas de números. A debe tener forma (m, n) y
        B debe tener forma (n, p).

    Lanza
    -----
    ValueError si alguna matriz está vacía, si las filas tienen largos
    distintos o si el número de columnas de A no coincide con el número
    de filas de B.
    """
    if not A or not B:
        raise ValueError("Las matrices no pueden estar vacías")
    if any(len(fila) != len(A[0]) for fila in A):
        raise ValueError("Todas las filas de A deben tener el mismo largo")
    if any(len(fila) != len(B[0]) for fila in B):
        raise ValueError("Todas las filas de B deben tener el mismo largo")
    if len(A[0]) != len(B):
        raise ValueError(
            "Dimensiones incompatibles: A tiene "
            f"{len(A[0])} columnas y B tiene {len(B)} filas"
        )

    filas = len(A)
    columnas = len(B[0])
    C = [[0] * columnas for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            suma = 0
            for k in range(len(B)):
                suma += A[i][k] * B[k][j]
            C[i][j] = suma

    return C
