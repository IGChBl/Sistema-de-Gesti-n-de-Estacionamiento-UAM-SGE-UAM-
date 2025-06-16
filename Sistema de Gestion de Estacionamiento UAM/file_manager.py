import json
import os

def cargar_parqueos(fecha):
    """Carga el estado de los parqueos desde un archivo JSON para la fecha dada."""
    archivo = f"parking_{fecha}.json"
    if os.path.exists(archivo):
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: El archivo {archivo} está corrupto. Inicializando nuevo estado.")
            return inicializar_parqueos()
    return inicializar_parqueos()

def guardar_parqueos(parqueos, fecha):
    """Guarda el estado de los parqueos en un archivo JSON para la fecha dada."""
    archivo = f"parking_{fecha}.json"
    try:
        with open(archivo, 'w') as f:
            json.dump(parqueos, f, indent=4)
    except Exception as e:
        print(f"Error al guardar el archivo {archivo}: {e}")

def inicializar_parqueos():
    """Crea la estructura de diccionarios con todos los espacios en 'disponible'."""
    parqueos = {
        "A": {f"A{i}": "disponible" for i in range(1, 31)},
        "B": {f"B{i}": "disponible" for i in range(1, 51)},
        "C": {f"C{i}": "disponible" for i in range(1, 21)}
    }
    return parqueos