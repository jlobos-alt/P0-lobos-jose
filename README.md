# P0 — Matriz multiplicación propia (mimatmul)

## Propósito general

Este proyecto implementa `mimatmul`, una función en Python puro para multiplicar
matrices (listas de listas) sin usar librerías externas de álgebra lineal. El
objetivo es comparar su desempeño (tiempo, CPU y RAM) contra `numpy` mediante un
benchmark, y presentar los resultados en un gráfico.

## Sistema operativo

Windows

## Versión de Python

3.13.15

## Ambiente virtual

Crear y activar el ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Instalar dependencias

```powershell
pip install -r requirements.txt
```

## Estado actual del proyecto (P0E1)

- Ambiente de desarrollo configurado.
- Información del computador obtenida en `data/system_info.json`.
- Primera versión de `src/mimatmul.py` implementada (multiplicación de matrices
  en Python puro).
- Prueba inicial en `tests/test_mimatmul.py`.
- Pendiente para P0E2: benchmark definitivo, datos finales, gráfico y documentación completa.
