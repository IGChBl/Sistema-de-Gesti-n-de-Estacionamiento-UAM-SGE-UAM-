Algoritmo AutomaticParking
	Definir opcion, espacios_disponibles,opcion_usuario,rolN Como Entero
	espacios_disponibles <- 10
	Definir usuario,correo,password,rol,usuario_base,correo_base,password_base,rol_base,usuarioing,correoing,passing,roling Como Caracter
	definir repite,base,salida Como Logico
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
	 Escribir 'Seleccione una opci�n: '
	 Leer opcion_usuario
	 segun opcion_usuario Hacer
		1://Registro de usuario
			Escribir "Digite su nombre de usuario"
			Leer usuario
			Escribir "Digite su correo electronico"
			leer correo
			Escribir "Digite su contrase�a"
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
			Escribir "Su contrase�a: ",password
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
				Escribir "Digite su contrase�a (se le pedira nuevamente si es incorrecto)"
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
			FinSi
		SiNo
			menu=Falso
	si menu=Verdadero Entonces
				
			
		Repetir
				
			 
			// Mostrar men� de usuario
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
					salida=Falso
				expresion:
				De Otro Modo:
					Escribir ' Opci�n no v�lida. Intente de nuevo.'
			FinSegun
		Hasta Que salida=Falso
	SiNo
		// Mostrar men� de admin
		Escribir '======================================'
		Escribir '      SISTEMA DE PARQUEO - U. XYZ     '
		Escribir '======================================'
		Escribir '1. Ingresar veh�culo'
		Escribir '2. Salida de veh�culo'
		Escribir '3. Mostrar espacios disponibles'
		Escribir '4. Salir'
		Escribir '--------------------------------------'
		Escribir "Herramientas de administrador"
		Escribir "5. 
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
				salida=Falso
			expresion:
			De Otro Modo:
				Escribir ' Opci�n no v�lida. Intente de nuevo.'
		FinSegun
	Hasta Que salida=Falso
		
	FinSi
	
			
		3:
			Escribir "Digite su nuevo nombre de usuario"
			Leer usuario
			Escribir "Digite su nuevo correo electronico"
			leer correo
			Escribir "Digite su nueva contrase�a"
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
			Escribir "Su nueva contrase�a: ",password
			Escribir "Su nuevo rol asignado: ",rol
		4:
			Repetir
				Escribir "Digite su nombre de usuario(Se le pedira reingresar su nombre si es incorrecto)"
			    leer usuarioing
			Hasta Que usuarioing=usuario
			
			Repetir
				Escribir "Digite su contrase�a (se le pedira nuevamente si es incorrecto)"
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
