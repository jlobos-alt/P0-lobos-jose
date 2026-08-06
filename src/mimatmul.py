"""mimatmul: multiplicación de matrices en Python puro."""


def mimatmul(A, B):
    """Multiplica dos matrices A (m x n) y B (n x p) usando listas de listas.

    Devuelve la matriz C (m x p) donde C[i][j] = sum_k A[i][k] * B[k][j].
    """
    if not A or not B:
        raise ValueError("Las matrices no pueden estar vacías")
    if len(A[0]) != len(B):
        raise ValueError(
            "Las dimensiones no coinciden: columnas de A != filas de B"
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
