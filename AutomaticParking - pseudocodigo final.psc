Algoritmo AutomaticParking
	Definir opcion, espacios_disponibles,opcion_usuario,rolN,agg,eliminar,liberar,ocupar Como Entero
	espacios_disponibles <- 10
	Definir usuario,correo,password,rol,usuario_base,correo_base,password_base,rol_base,usuarioing,correoing,passing,roling Como Caracter
	definir repite,base,salida,menu Como Logico
	usuario_base="Nombre de Usuario"
	correo_base="correo@base.com"
	password_base="123456"
	rol_base="Usuario"
	usuario=usuario_base
	correo=correo_base
	password=password_base
	rol=rol_base
	repite=Verdadero
	base=Falso
	salida=Verdadero
	agg=0
	
	
	//Menu de registro de usuario e inicio de sesion
	Repetir
		
	 
	 Escribir '======================================'
	 Escribir '      Registro de usuario    '
	 Escribir '======================================'
	 Escribir '1. Registrar usuario'
	 Escribir '2. Iniciar sesion y acceder al sistema(Debe registrar su usuario primero)'
	 Escribir '3. Modificar usuario'
	 Escribir '4. Eliminar Usuario'
	 Escribir "5. Salir"
	 Escribir '--------------------------------------'
	 Escribir 'Seleccione una opción: '
	 Leer opcion_usuario
	 segun opcion_usuario Hacer
		1://Registro de usuario
			Escribir "Digite su nombre de usuario"
			Leer usuario
			Escribir "Digite su correo electronico"
			leer correo
			Escribir "Digite su contraseña"
			leer password
			Escribir "Seleccione el rol que desea tomar"
			Escribir '--------------------------------------'
			Escribir "1. usuario "
			Escribir "2. admin "
			Escribir '--------------------------------------'
			leer rolN
			segun rolN Hacer
				1:
					Escribir "Se ha asignado el rol de usuario"
				2:
					Escribir "Se ha asignado el rol de administrador"
				De Otro Modo:
					Escribir "La opcion asignada no es valida"
					
			FinSegun
			si rolN=1 Entonces
				rol="Usuario"
			SiNo
				rol="Administrador"
			FinSi
			Limpiar Pantalla
			Escribir "Nombre de usuario registrado: ",usuario
			Escribir "Correo registrado : ",correo
			Escribir "Su contraseña: ",password
			Escribir "Su rol asignado: ",rol
		2://Inicio de sesion y acceso directo al sistema
			Repetir
				Escribir "Digite su nombre de usuario(Se le pedira reingresar su nombre si es incorrecto)"
			    leer usuarioing
			Hasta Que usuarioing=usuario
			Repetir
				Escribir "Digite su correo (se le pedira nuevamente si es incorrecto)"
				Leer correoing
			Hasta Que correoing=correo
			
			Repetir
				Escribir "Digite su contraseña (se le pedira nuevamente si es incorrecto)"
				Leer passing
			Hasta Que passing=password
			Repetir
				Escribir "Digite su rol Usuario o Administrador (se le pedira nuevamente si es incorrecto)"
				Leer roling
			Hasta Que roling=rol
			Limpiar Pantalla
			Escribir "Se ha iniciado sesion con exito"
			si rol="Usuario"Entonces
				menu=Verdadero
			
		SiNo
			menu=Falso
		FinSi
		
	si menu=Verdadero Entonces
				
			
		Repetir
				
			 
			// Mostrar menú de usuario
			Escribir '======================================'
			Escribir '      SISTEMA DE PARQUEO - U. XYZ     '
			Escribir '======================================'
			Escribir '1. Ingresar vehículo'
			Escribir '2. Salida de vehículo'
			Escribir '3. Mostrar espacios disponibles'
			Escribir '4. Salir'
			Escribir '--------------------------------------'
			Escribir 'Seleccione una opción: '
			Leer opcion
			Segun opcion Hacer
				1:
					Si espacios_disponibles>0 Entonces
						espacios_disponibles <- espacios_disponibles-1
						Escribir ' Vehículo ingresado.'
						Escribir ' Espacios restantes: ', espacios_disponibles
					SiNo
						Escribir ' Parqueo lleno. No hay espacios disponibles.'
					FinSi
				2:
					Si espacios_disponibles<10 Entonces
						espacios_disponibles <- espacios_disponibles+1
						Escribir ' Vehículo salió.'
						Escribir ' Espacios disponibles: ', espacios_disponibles
					SiNo
						Escribir ' El parqueo ya está vacío. No hay vehículos para salir.'
					FinSi
				3:
					Escribir ' Espacios disponibles actualmente: ', espacios_disponibles
				4:
					Escribir ' Saliendo del sistema. ¡Hasta luego!'
					salida=Falso
				expresion:
				De Otro Modo:
					Escribir ' Opción no válida. Intente de nuevo.'
			FinSegun
		Hasta Que salida=Falso
	SiNo
		// Mostrar menú de admin
		Escribir '======================================'
		Escribir '      SISTEMA DE PARQUEO - U. XYZ     '
		Escribir '======================================'
		Escribir '1. Ingresar vehículo'
		Escribir '2. Salida de vehículo'
		Escribir '3. Mostrar espacios disponibles'
		Escribir '4. Salir'
		Escribir '--------------------------------------'
		Escribir "Herramientas de administrador"
		Escribir "--------------------------------------"
		Escribir "5. Agregar estacionamiento"
		Escribir "6. Eliminar estacionamiento"
		Escribir "7. Liberar Parqueo"
		Escribir "8. Ocupar Parqueo"
		Escribir 'Seleccione una opción: '
		
		Repetir
			
		
		Leer opcion
		Segun opcion Hacer
			1:
				Si espacios_disponibles>0+agg Entonces
					espacios_disponibles <- espacios_disponibles-1
					Escribir ' Vehículo ingresado.'
					Escribir ' Espacios restantes: ', espacios_disponibles
				SiNo
					Escribir ' Parqueo lleno. No hay espacios disponibles.'
				FinSi
			2:
				Si espacios_disponibles<10+agg Entonces
					espacios_disponibles <- espacios_disponibles+1
					Escribir ' Vehículo salió.'
					Escribir ' Espacios disponibles: ', espacios_disponibles
				SiNo
					Escribir ' El parqueo ya está vacío. No hay vehículos para salir.'
				FinSi
			3:
				Escribir ' Espacios disponibles actualmente: ', espacios_disponibles
			4:
				Escribir ' Saliendo del sistema. ¡Hasta luego!'
				salida=Falso
			5:
				Escribir "Digite el numero de espacios de estacionamiento desea agregar"
				leer agg
				espacios_disponibles=espacios_disponibles+agg
				Escribir "Espacios agregados. Ahora el estacionamiento tiene un total de: ",espacios_disponibles ,"espacios"
			6:
				Escribir "Digite la cantidad de estacionamientos que desea eliminar, hay un total de ",espacios_disponibles
				leer eliminar
				espacios_disponibles=espacios_disponibles-eliminar
				si agg<=eliminar Entonces
					agg=0
				SiNo
					agg=agg-eliminar
				FinSi
				Escribir "Se han eliminado correctamente los espacios del estacionamiento ahora hay un total de ",espacios_disponibles ,"espacios disponibles"
			7:
				Escribir "Digite la cantidad de espacios que desea liberar"
				leer liberar
				espacios_disponibles=espacios_disponibles+liberar
				Escribir "Los espacios han sido liberados ahora hay un total de ",espacios_disponibles, "espacios disponibles"
			8:
				Escribir "Digite la cantidad de espacios que desea ocupar"
				leer ocupar
				espacios_disponibles=espacios_disponibles-ocupar
				si agg<=ocupar Entonces
					agg=0
				SiNo
					agg=agg-ocupar
				FinSi
				
			De Otro Modo:
				Escribir ' Opción no válida. Intente de nuevo.'
		FinSegun
	     Hasta Que salida=Falso
		
	FinSi
	
			
		3:
			Escribir "Digite su nuevo nombre de usuario"
			Leer usuario
			Escribir "Digite su nuevo correo electronico"
			leer correo
			Escribir "Digite su nueva contraseña"
			leer password
			Escribir "Seleccione el nuevo rol que desea tomar"
			Escribir '--------------------------------------'
			Escribir "1. usuario "
			Escribir "2. admin "
			Escribir '--------------------------------------'
			leer rolN
			segun rolN Hacer
				1:
					Escribir "Se ha asignado el rol de usuario"
				2:
					Escribir "Se ha asignado el rol de administrador"
				De Otro Modo:
					Escribir "La opcion asignada no es valida"
					
			FinSegun
			si rolN=1 Entonces
				rol="Usuario"
			SiNo
				rol="Administrador"
			FinSi
			Limpiar Pantalla
			Escribir "Nuevo nombre de usuario registrado: ",usuario
			Escribir "Nuevo correo registrado : ",correo
			Escribir "Su nueva contraseña: ",password
			Escribir "Su nuevo rol asignado: ",rol
		4:
			Repetir
				Escribir "Digite su nombre de usuario(Se le pedira reingresar su nombre si es incorrecto)"
			    leer usuarioing
			Hasta Que usuarioing=usuario
			
			Repetir
				Escribir "Digite su contraseña (se le pedira nuevamente si es incorrecto)"
				Leer passing
			Hasta Que passing=password
			Repetir
				Escribir "Digite su rol usuario o Administrador (se le pedira nuevamente si es incorrecto)"
				Leer roling
			Hasta Que roling=rol
			Escribir "Escriba la palabra CONFIRMAR para eliminar el usuario y sus datos(Digitela en mayuscula)"
			leer confirmacion
			si confirmacion="CONFIRMAR" Entonces
				usuario_base="Nombre de Usuario"
				correo_base="correo@base.com"
				password_base="123456"
				rol_base="usuario"
				usuario=usuario_base
				correo=correo_base
				password=password_base
				rol=rol_base
				Escribir "Los datos del usuario han sido eliminados con exito"
			SiNo
				Escribir "No se ha digitado la palabra CONFIRMAR correctamente"
			FinSi
		5:
			repite=Falso
		   
		De Otro Modo:
			Escribir "Opcion no valida"
			
			
			
			
			
			
			
			
			
			
		 
			
			
			
			
	FinSegun
Hasta Que repite=Falso
Escribir "Gracias por utilizar Automatic Parking Hasta luego"

	
FinAlgoritmo
