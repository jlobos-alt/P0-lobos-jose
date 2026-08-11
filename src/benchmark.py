"""Benchmark: compara mimatmul (Python puro) contra NumPy (A @ B).

Mide el tiempo de multiplicación de matrices cuadradas float64 de varios
tamaños, con varias repeticiones y una ejecución de calentamiento.
Guarda cada repetición en data/benchmark_results.csv y genera el gráfico
figures/benchmark.png.
"""

import csv
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mimatmul import mimatmul  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
DATA = RAIZ / "data"
FIGURES = RAIZ / "figures"
CSV_SALIDA = DATA / "benchmark_results.csv"
PNG_SALIDA = FIGURES / "benchmark.png"

TAMANOS = [16, 32, 64, 128]
REPETICIONES = 3

# Prohibido usar internamente en mimatmul, pero el benchmark compara contra
# NumPy con el operador @, tal como pide el enunciado.
def multiplicacion_numpy(A, B):
    return A @ B


def medir(func, A, B):
    """Mide en segundos una ejecución de func(A, B) con un reloj apropiado."""
    inicio = time.perf_counter()
    func(A, B)
    return time.perf_counter() - inicio


def correr_benchmark():
    resultados = []
    for n in TAMANOS:
        rng = np.random.default_rng(n)
        A = rng.random((n, n), dtype=np.float64)
        B = rng.random((n, n), dtype=np.float64)

        # Calentamiento (una ejecución de cada método antes de medir).
        medir(mimatmul, A.tolist(), B.tolist())
        medir(multiplicacion_numpy, A, B)

        for rep in range(1, REPETICIONES + 1):
            t_mimatmul = medir(mimatmul, A.tolist(), B.tolist())
            resultados.append(["mimatmul", n, rep, t_mimatmul])
            t_numpy = medir(multiplicacion_numpy, A, B)
            resultados.append(["numpy", n, rep, t_numpy])
    return resultados


def guardar_csv(resultados):
    DATA.mkdir(parents=True, exist_ok=True)
    with open(CSV_SALIDA, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["metodo", "tamano", "repeticion", "tiempo"])
        escritor.writerows(resultados)


def generar_grafico(resultados):
    import matplotlib.pyplot as plt

    FIGURES.mkdir(parents=True, exist_ok=True)
    por_metodo = {"mimatmul": {}, "numpy": {}}
    for metodo, tamano, rep, tiempo in resultados:
        por_metodo[metodo].setdefault(tamano, []).append(tiempo)

    for metodo, puntos in por_metodo.items():
        tamanos = sorted(puntos)
        promedios = [sum(puntos[n]) / len(puntos[n]) for n in tamanos]
        plt.plot(tamanos, promedios, marker="o", label=metodo)

    plt.xscale("log", base=2)
    plt.yscale("log")
    plt.xlabel("Tamaño de la matriz (n x n)")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Benchmark: mimatmul vs NumPy")
    plt.legend(title="Método")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(PNG_SALIDA, dpi=150)
    plt.close()


def main():
    print("Ejecutando benchmark...")
    resultados = correr_benchmark()
    guardar_csv(resultados)
    print(f"Resultados guardados en {CSV_SALIDA}")
    for fila in resultados:
        print(f"  {fila[0]:8s}  n={fila[1]:3d}  rep={fila[2]}  {fila[3]:.6f} s")
    generar_grafico(resultados)
    print(f"Gráfico guardado en {PNG_SALIDA}")


if __name__ == "__main__":
    main()
