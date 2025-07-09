import json                   # Importa el módulo json para manejar archivos JSON
import os             # Importa el módulo os para manejar rutas de archivos y directorios
from datetime import datetime   # Importa datetime para manejar fechas y horas

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

def _path(name):                                                #Calcula la ruta absoluta dentro de la carpeta data para el archivo name.
    return os.path.join(data_dir, name)

# Persistencia de parqueos por fecha
def cargar_parqueos(fecha):                                     #Carga el estado de los espacios de estacionamiento del día especificado. Si no existe o está corrupto, inicializa un nuevo estado.
    archivo = _path(f"parking_{fecha}.json")
    if os.path.exists(archivo):
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return inicializar_parqueos()
    return inicializar_parqueos()

def guardar_parqueos(parqueos, fecha):                          #Guarda el estado de los espacios de estacionamiento del día especificado.
    archivo = _path(f"parking_{fecha}.json")
    with open(archivo, 'w') as f:
        json.dump(parqueos, f, indent=4, default=str)

def inicializar_parqueos():                                     #Inicializa un estado por defecto de los espacios de estacionamiento.
    return {
        'A': {f'A{i}':'disponible' for i in range(1,31)},
        'B': {f'B{i}':'disponible' for i in range(1,51)},
        'C': {f'C{i}':'disponible' for i in range(1,21)},
    }

# Usuarios
def cargar_usuarios():                                          #Carga el estado de los usuarios registrados. Si no existe o está corrupto, inicializa un nuevo estado.    
    archivo = _path('users.json')
    if os.path.exists(archivo):
        return json.load(open(archivo))
    return {}

def guardar_usuarios(users):                                    #Guarda el estado de los usuarios registrados.
    archivo = _path('users.json')
    json.dump(users, open(archivo, 'w'), indent=4)

# Historial
def cargar_historial():                                         #Carga el historial de parqueos. Si no existe o está corrupto, inicializa un nuevo estado.
    archivo = _path('history.json')
    if os.path.exists(archivo):
        return json.load(open(archivo))
    return []

def guardar_historial(hist):                                    #Guarda el historial de parqueos.    
    archivo = _path('history.json')
    json.dump(hist, open(archivo, 'w'), indent=4)