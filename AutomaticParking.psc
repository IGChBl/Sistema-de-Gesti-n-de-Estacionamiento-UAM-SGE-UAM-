Algoritmo AutomaticParking
	Definir opcion, espacios_disponibles Como Entero
	espacios_disponibles <- 10
	Repetir
		// Mostrar men� mejorado
		Escribir '======================================'
		Escribir '      SISTEMA DE PARQUEO - U. XYZ     '
		Escribir '======================================'
		Escribir '1. Ingresar veh�culo'
		Escribir '2. Salida de veh�culo'
		Escribir '3. Mostrar espacios disponibles'
		Escribir '4. Salir'
		Escribir '--------------------------------------'
		Escribir 'Seleccione una opci�n: '
		Leer opcion
		Segun opcion Hacer
			1:
				Si espacios_disponibles>0 Entonces
					espacios_disponibles <- espacios_disponibles-1
					Escribir ' Veh�culo ingresado.'
					Escribir ' Espacios restantes: ', espacios_disponibles
				SiNo
					Escribir ' Parqueo lleno. No hay espacios disponibles.'
				FinSi
			2:
				Si espacios_disponibles<10 Entonces
					espacios_disponibles <- espacios_disponibles+1
					Escribir ' Veh�culo sali�.'
					Escribir ' Espacios disponibles: ', espacios_disponibles
				SiNo
					Escribir ' El parqueo ya est� vac�o. No hay veh�culos para salir.'
				FinSi
			3:
				Escribir ' Espacios disponibles actualmente: ', espacios_disponibles
			4:
				Escribir ' Saliendo del sistema. �Hasta luego!'
			De Otro Modo:
				Escribir ' Opci�n no v�lida. Intente de nuevo.'
		FinSegun
		Escribir ''
	Hasta Que opcion=4
FinAlgoritmo
