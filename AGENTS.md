# AGENTS.md

Instrucciones para trabajar con OpenCode en este repositorio.

## Propósito del proyecto

Implementar `mimatmul` (multiplicación de matrices en Python puro) y comparar
su desempeño contra `numpy` con un benchmark, entregando un gráfico y análisis
de CPU y RAM. El repo se usa para P0E1 y P0E2.

## Reglas

- Mantener el código sencillo y legible.
- No inventar mediciones ni datos: todo valor debe obtenerse ejecutando código real.
- No ejecutar comandos destructivos de Git (force push, reset, rebase, etc.) sin pedir permiso.
- No subir credenciales, claves ni datos sensibles al repositorio.
- Ejecutar las pruebas después de modificar código:

```powershell
python -m pytest tests/
```

- La raíz del proyecto es este directorio; el código vive en `src/`.
- No incluir el ambiente virtual (`.venv/`) en el repositorio.
