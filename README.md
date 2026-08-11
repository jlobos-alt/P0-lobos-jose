# P0 — mimatmul: multiplicación de matrices en Python puro

## Propósito general

Este proyecto implementa `mimatmul`, una función en Python puro que multiplica
matrices (listas de listas) usando ciclos explícitos, sin librerías externas de
álgebra lineal. Se compara su desempeño contra `numpy` (`A @ B`) mediante un
benchmark reproducible y se presentan los resultados en un gráfico, junto con
observaciones sobre el uso de CPU y RAM del computador.

Estructura del repositorio:

```
P0-lobos-jose/
├── README.md
├── AGENTS.md
├── requirements.txt
├── src/
│   ├── system_info.py
│   ├── mimatmul.py
│   └── benchmark.py
├── tests/
│   └── test_mimatmul.py
├── data/
│   ├── system_info.json
│   └── benchmark_results.csv
└── figures/
    └── benchmark.png
```

## Reproducir el proyecto

Comandos exactos (en Windows PowerShell):

```powershell
# 1. Clonar el repositorio
git clone https://github.com/jlobos-alt/P0-lobos-jose.git
cd P0-lobos-jose

# 2. Crear el ambiente virtual
python -m venv .venv

# 3. Activar el ambiente
.\.venv\Scripts\Activate.ps1

# 4. Instalar las dependencias
pip install -r requirements.txt

# 5. Ejecutar las pruebas
python -m pytest tests/

# 6. Ejecutar el benchmark (genera data/benchmark_results.csv y figures/benchmark.png)
python src/benchmark.py

# (Opcional) Obtener la información del computador
python src/system_info.py
```

En macOS/Linux la activación es `source .venv/bin/activate`.

## Información del computador

| Característica | Valor |
|---|---|
| Sistema operativo | Windows 10.0.26200 |
| Arquitectura | AMD64 |
| Procesador | 11th Gen Intel(R) Core(TM) i7-1185G7 @ 3.00GHz |
| Núcleos físicos | 4 |
| Procesadores lógicos | 8 |
| Memoria RAM total | 15.4 GB |
| Versión de Python | 3.13.15 |

El detalle completo está en `data/system_info.json`.

## Implementación de mimatmul

`src/mimatmul.py` implementa `mimatmul(A, B)` con tres ciclos anidados de
Python (`i`, `j`, `k`). Valida que las matrices no estén vacías, que todas las
filas tengan el mismo largo y que el número de columnas de `A` coincida con el
número de filas de `B`, lanzando `ValueError` con un mensaje claro en caso
contrario. No utiliza `@`, `np.matmul`, `np.dot` ni `np.einsum`.

## Pruebas

`tests/test_mimatmul.py` cubre:

- un caso conocido (2x2);
- matrices cuadradas;
- matrices rectangulares;
- comparación de resultados con NumPy;
- dimensiones incompatibles;
- matrices vacías.

Todas pasan con `pytest` (6 pruebas).

## Benchmark

`src/benchmark.py` compara `mimatmul` contra NumPy (`A @ B`) usando:

- matrices cuadradas `float64`;
- cuatro tamaños: 16, 32, 64 y 128;
- tres repeticiones por tamaño y método;
- una ejecución de calentamiento por método antes de medir;
- `time.perf_counter` como reloj;
- guardado de cada repetición en `data/benchmark_results.csv`;
- tamaños seguros para este computador (RAM libre ~5 GB).

## Resultados

`data/benchmark_results.csv` contiene las mediciones reales
(`metodo, tamano, repeticion, tiempo`). El gráfico `figures/benchmark.png`
muestra el tiempo (escala logarítmica) según el tamaño, para ambos métodos.

## Observaciones de rendimiento

- **¿mimatmul utiliza uno o varios núcleos?** Uno. Al ser Python puro con ciclos
  explícitos, se ejecuta en un solo hilo (además el GIL de CPython evita el
  paralelismo real con hilos).
- **¿NumPy utiliza uno o varios núcleos?** Varios. NumPy delega la
  multiplicación a bibliotecas BLAS optimizadas (en esta instalación OpenBLAS),
  que paralelizan la operación usando varios hilos.
- **¿Por qué NumPy es más rápido?** Porque ejecuta operaciones vectorizadas en
  código C/Fortran altamente optimizado, con manejo eficiente de caché y
  múltiples hilos, en lugar de interpretar la operación elemento a elemento en
  Python como hace `mimatmul`. En las mediciones fue entre ~50 y ~260 veces
  más rápido según el tamaño.
- **¿Por qué las repeticiones no dan exactamente el mismo tiempo?** Por ruido
  del sistema: planificación del sistema operativo, cambios de frecuencia del
  procesador (turbo), estado de las cachés y procesos en segundo plano.
- **¿Cuál es la matriz cuadrada más grande que cabría en la RAM libre?** Con
  ~5 GB de RAM libre y una matriz `float64` que ocupa `8 * n^2` bytes, una sola
  matriz cabría con `n ≈ 25000`; considerando las dos matrices de entrada y el
  resultado, cabría aproximadamente una de `n ≈ 14000`.

## Uso de OpenCode

- **¿Qué parte realizó correctamente el agente?** Configuró el ambiente y el
  repositorio, escribió `mimatmul`, las pruebas, el benchmark, generó el CSV y
  el gráfico, y redactó este README.
- **¿Qué parte tuvo que corregir o modificar?** El correo asociado a los
  commits (tuve que reescribir la historia para que quedara con mi correo
  correcto) y los tamaños del benchmark, que ajusté para que fueran seguros y
  rápidos en mi equipo.
- **¿Qué archivo comprende mejor después del proyecto?** `src/mimatmul.py`,
  porque su lógica es simple y se refleja directamente en las pruebas.
- **¿Qué parte del código todavía le resulta menos clara?** El uso de múltiples
  núcleos por parte de NumPy/BLAS: sé que ocurre, pero me cuesta visualizar
  cómo se distribuye el trabajo entre hilos.
