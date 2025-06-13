# Sistema de Gestión de Estacionamiento UAM (SGE-UAM)
# Descripción: Este programa permite gestionar el estado de los espacios de estacionamiento en la UAM.
# Versión: 1.0
# Fecha de creación: 16/06/2025
# Grupo: ProyectoAsignatura#6
# Integrantes:
# - EMILIO ENRIQUE DABOUB SANDOVAL
# - JEREMY JOSUE GRADIZ NOGUERA
# - MAVERICK ALEJANDRO MIRANDA GUTIERREZ
# - IVÁN GERARDO CHAVARRÍA BLANDÓN


def inicializar_parqueos():
    """Crea la estructura de diccionarios con todos los espacios en 'disponible'."""
    parqueos = {
        "A": {f"A{i}": "disponible" for i in range(1, 31)},
        "B": {f"B{i}": "disponible" for i in range(1, 51)},
        "C": {f"C{i}": "disponible" for i in range(1, 21)}
    }
    return parqueos

def mostrar_menu():
    """Muestra el menú principal y retorna la opción seleccionada."""
    print("\n*** Sistema de Gestión de Estacionamiento UAM ***\n")
    print("Seleccione una opción:")
    print("1. Registrar OCUPACIÓN de espacio")
    print("2. Registrar LIBERACIÓN de espacio")
    print("3. Ver estado de todos los parqueos")
    print("4. Salir")
    return input("\n> Ingrese su opción: ")

def validar_parqueo(parqueo):
    """Valida si el parqueo ingresado existe."""
    return parqueo.upper() in ["A", "B", "C"]

def validar_numero_espacio(parqueo, numero, parqueos):
    """Valida si el número de espacio existe en el parqueo."""
    max_espacios = {"A": 30, "B": 50, "C": 20}
    try:
        num = int(numero)
        if 1 <= num <= max_espacios[parqueo]:
            return True
        return False
    except ValueError:
        return False

def ocupar_espacio(parqueos):
    """Registra la ocupación de un espacio."""
    parqueo = input("¿En qué parqueo? (A, B, C): ").upper()
    if not validar_parqueo(parqueo):
        print(f"Error: El parqueo {parqueo} no existe.")
        return

    numero = input(f"¿Qué número de espacio se va a ocupar? (Ej: 5 para {parqueo}5): ")
    if not validar_numero_espacio(parqueo, numero, parqueos):
        print(f"Error: El espacio {parqueo}{numero} no es válido.")
        return

    espacio = f"{parqueo}{numero}"
    if parqueos[parqueo][espacio] == "disponible":
        parqueos[parqueo][espacio] = "ocupado"
        print(f"Se ha ocupado el espacio {espacio}.")
    else:
        print(f"Error: El espacio {espacio} ya se encuentra ocupado.")

def liberar_espacio(parqueos):
    """Registra la liberación de un espacio."""
    parqueo = input("¿En qué parqueo? (A, B, C): ").upper()
    if not validar_parqueo(parqueo):
        print(f"Error: El parqueo {parqueo} no existe.")
        return

    numero = input(f"¿Qué número de espacio se va a liberar? (Ej: 5 para {parqueo}5): ")
    if not validar_numero_espacio(parqueo, numero, parqueos):
        print(f"Error: El espacio {parqueo}{numero} no es válido.")
        return

    espacio = f"{parqueo}{numero}"
    if parqueos[parqueo][espacio] == "ocupado":
        parqueos[parqueo][espacio] = "disponible"
        print(f"🅿️ Se ha habilitado el espacio {espacio}.")
    else:
        print(f"Error: El espacio {espacio} ya estaba libre.")

def mostrar_estado(parqueos):
    """Muestra el estado actual de todos los parqueos."""
    print("\n--- ESTADO ACTUAL DE LOS PARQUEOS ---\n")
    for parqueo in parqueos:
        ocupados = sum(1 for estado in parqueos[parqueo].values() if estado == "ocupado")
        disponibles = len(parqueos[parqueo]) - ocupados
        disp_list = [espacio for espacio, estado in parqueos[parqueo].items() if estado == "disponible"]
        ocup_list = [espacio for espacio, estado in parqueos[parqueo].items() if estado == "ocupado"]

        print(f"== PARQUEO {parqueo} ==")
        print(f"- Ocupados: {ocupados}")
        print(f"- Disponibles: {disponibles}")
        print(f"- Lista de espacios disponibles: {', '.join(disp_list) if disp_list else 'Ninguno'}")
        print(f"- Lista de espacios ocupados: {', '.join(ocup_list) if ocup_list else 'Ninguno'}\n")

    input("Presione Enter para volver al menú...")

def main():
    """Función principal que ejecuta el ciclo del programa."""
    parqueos = inicializar_parqueos()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            ocupar_espacio(parqueos)
        elif opcion == "2":
            liberar_espacio(parqueos)
        elif opcion == "3":
            mostrar_estado(parqueos)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()