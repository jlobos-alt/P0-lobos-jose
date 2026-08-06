"""Obtiene información básica del computador y la guarda en data/system_info.json."""

import json
import os
import platform
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DATA = RAIZ / "data"


def ejecutar_comando(comando):
    """Ejecuta un comando de PowerShell y devuelve su salida limpia o None."""
    try:
        salida = subprocess.run(
            ["powershell", "-NoProfile", "-Command", comando],
            capture_output=True,
            text=True,
            timeout=15,
        )
        texto = salida.stdout.strip()
        return texto if texto else None
    except Exception:
        return None


def info_windows():
    modelo_cpu = ejecutar_comando(
        "(Get-CimInstance Win32_Processor).Name"
    )
    nucleos_fisicos = ejecutar_comando(
        "(Get-CimInstance Win32_Processor).NumberOfCores"
    )
    ram_bytes = ejecutar_comando(
        "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory"
    )
    return {
        "modelo_procesador": modelo_cpu,
        "nucleos_fisicos": int(nucleos_fisicos) if nucleos_fisicos else None,
        "ram_total_bytes": int(ram_bytes) if ram_bytes else None,
    }


def obtener_info():
    info = {
        "sistema_operativo": platform.system(),
        "sistema_operativo_version": platform.version(),
        "arquitectura": platform.machine(),
        "python_version": sys.version.split()[0],
        "python_implementacion": platform.python_implementation(),
        "nombre_equipo": platform.node(),
        "procesadores_logicos": os.cpu_count(),
    }

    if platform.system() == "Windows":
        info.update(info_windows())
    else:
        try:
            import os as _os

            info["modelo_procesador"] = _os.cpu_count()
        except Exception:
            info["modelo_procesador"] = None
        info["nucleos_fisicos"] = None
        info["ram_total_bytes"] = None

    return info


def main():
    info = obtener_info()
    DATA.mkdir(parents=True, exist_ok=True)
    salida = DATA / "system_info.json"
    salida.write_text(json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(info, indent=2, ensure_ascii=False))
    print(f"\nGuardado en: {salida}")


if __name__ == "__main__":
    main()
