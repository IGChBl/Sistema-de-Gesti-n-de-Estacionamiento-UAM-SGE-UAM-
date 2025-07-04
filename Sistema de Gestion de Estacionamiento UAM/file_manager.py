import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

def _path(name):
    return os.path.join(data_dir, name)

# Persistencia de parqueos por fecha
def cargar_parqueos(fecha):
    archivo = _path(f"parking_{fecha}.json")
    if os.path.exists(archivo):
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return inicializar_parqueos()
    return inicializar_parqueos()

def guardar_parqueos(parqueos, fecha):
    archivo = _path(f"parking_{fecha}.json")
    with open(archivo, 'w') as f:
        json.dump(parqueos, f, indent=4, default=str)

def inicializar_parqueos():
    return {
        'A': {f'A{i}':'disponible' for i in range(1,31)},
        'B': {f'B{i}':'disponible' for i in range(1,51)},
        'C': {f'C{i}':'disponible' for i in range(1,21)},
    }

# Usuarios
def cargar_usuarios():
    archivo = _path('users.json')
    if os.path.exists(archivo):
        return json.load(open(archivo))
    return {}

def guardar_usuarios(users):
    archivo = _path('users.json')
    json.dump(users, open(archivo, 'w'), indent=4)

# Historial
def cargar_historial():
    archivo = _path('history.json')
    if os.path.exists(archivo):
        return json.load(open(archivo))
    return []

def guardar_historial(hist):
    archivo = _path('history.json')
    json.dump(hist, open(archivo, 'w'), indent=4)