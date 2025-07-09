Algoritmo GestionEstacionamientoUAM
	
    Definir TOTAL_ESPACIOS Como Entero
    TOTAL_ESPACIOS <- 50
    Dimension espacios[TOTAL_ESPACIOS]
    espacios Como Logico
    Definir opcion Como Entero
    Definir i, espacio Como Entero
    Definir placa Como Cadena
    Definir espacios_libres Como Entero
	
    Para i <- 1 Hasta TOTAL_ESPACIOS Hacer
        espacios[i] <- Falso
    FinPara
	
    Repetir
        Escribir "=== Sistema de Gestión de Estacionamiento UAM ==="
        Escribir "1. Registrar entrada de vehículo"
        Escribir "2. Registrar salida de vehículo"
        Escribir "3. Consultar estado del estacionamiento"
        Escribir "4. Salir"
        Escribir "Seleccione una opción: "
        Leer opcion
		
        Segun opcion Hacer
            Caso 1:
                espacios_libres <- 0
                Para i <- 1 Hasta TOTAL_ESPACIOS Hacer
                    Si espacios[i] = Falso Entonces
                        espacios_libres <- espacios_libres + 1
                    FinSi
                FinPara
				
                Si espacios_libres > 0 Entonces
                    Escribir "Espacios libres: ", espacios_libres
                    Escribir "Ingrese el número de espacio (1 a ", TOTAL_ESPACIOS, "): "
                    Leer espacio
                    Si espacio >= 1 Y espacio <= TOTAL_ESPACIOS Entonces
                        Si espacios[espacio] = Falso Entonces
                            Escribir "Ingrese la placa del vehículo: "
                            Leer placa
                            espacios[espacio] <- Verdadero
                            Escribir "Vehículo con placa ", placa, " registrado en el espacio ", espacio
                        Sino
                            Escribir "Error: El espacio ", espacio, " ya está ocupado."
                        FinSi
                    Sino
                        Escribir "Error: Número de espacio inválido."
                    FinSi
                Sino
                    Escribir "Estacionamiento lleno. No hay espacios disponibles."
                FinSi
				
            Caso 2:
                Escribir "Ingrese el número de espacio a liberar (1 a ", TOTAL_ESPACIOS, "): "
                Leer espacio
                Si espacio >= 1 Y espacio <= TOTAL_ESPACIOS Entonces
                    Si espacios[espacio] = Verdadero Entonces
                        espacios[espacio] <- Falso
                        Escribir "Espacio ", espacio, " liberado exitosamente."
                    Sino
                        Escribir "Error: El espacio ", espacio, " ya está libre."
                    FinSi
                Sino
                    Escribir "Error: Número de espacio inválido."
                FinSi
				
            Caso 3:
                espacios_libres <- 0
                Escribir "=== Estado del Estacionamiento ==="
                Para i <- 1 Hasta TOTAL_ESPACIOS Hacer
                    Si espacios[i] = Falso Entonces
                        Escribir "Espacio ", i, ": Libre"
                        espacios_libres <- espacios_libres + 1
                    Sino
                        Escribir "Espacio ", i, ": Ocupado"
                    FinSi
                FinPara
                Escribir "Total de espacios libres: ", espacios_libres
                Escribir "Total de espacios ocupados: ", TOTAL_ESPACIOS - espacios_libres
				
            Caso 4:
                Escribir "Saliendo del sistema. ¡Gracias por usar el programa!"
                
            De Otro Modo:
                Escribir "Opción inválida. Por favor, seleccione una opción válida."
        FinSegun
		
        Escribir "Presione cualquier tecla para continuar..."
        Esperar Tecla
		
    Hasta Que opcion = 4

FinAlgoritmo