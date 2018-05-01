#Autores:
#Maria Fernanda Remis 18024
#Gabriela Garza 18101
#Filiberto Morales 18321
#Andy Castillo 18040
#Francisco Rosal 18676
#25/04/18
#Aplicacion TuristicGT

#Se importan modulos
import pymongo
import moduloTuristicGT

#Se crea la conexion con el cliente de Mongo
conexion = pymongo.MongoClient()
#Se establece la base de datos ccon la que se trabaja
db = conexion["turisticgt"]
#Se establecen las colecciones con las que se trabajaran
coleccionLugares = db.lugares
coleccionUsuarios = db.usuariosAdminTuristic


#usuario = {
#	'Nombre': "Admin", 
#	'Apellido': "Admin", 
#	'Usuario': "Admin", 
#	'Contraseña': "admin"}
#coleccionUsuarios.insert(usuario)
#usuario = {
#	'Nombre': "Willi", 
#	'Apellido': "Rosal", 
#	'Usuario': "Master", 
#	'Contraseña': "admin"}
#coleccionUsuarios.insert(usuario)


menuPantallaInicio = "0"
#Ciclo principal
while menuPantallaInicio != "3":
	print(moduloTuristicGT.menuInicio())
	menuPantallaInicio = input("Opcion: ")

#
#	Consulta
#

	if menuPantallaInicio == "1":
		#Consulta
		menuConsulta = "0"
		while menuConsulta != "3":
			print(moduloTuristicGT.menuConsulta())
			menuConsulta = input("Opcion: ")
			if menuConsulta == "1":
				#
				#Departamentos
				#
				menuCategorias = "0"
				while menuCategorias != "3":
					departamento = input("\nIngrese un departamento: ")
					print(moduloTuristicGT.menuCategorias(departamento))
					menuCategorias = input("Opcion: ")

					if (menuCategorias == "1") or (menuCategorias == "2"):
						#
						#Seleccionar lugar
						#
						if menuCategorias == "1":
							#Restaurantes
							print("\nRESTAURANTES EN "+str(departamento.upper()+" (BD):"))
							print("1. Regresar")
							#Funcion mostrar los restaurantes del departamento en la bd
							lugarElecto = input("Ingrese el numero del restaurante de su eleccion: ")
						else:
							#Entretenimiento
							print("\nENTRETENIMIENTO EN "+str(departamento.upper()+" (BD):"))
							print("1. Regresar")
							#Funcion mostrar los lugares de entretenimiento del departamento en la bd
							lugarElecto = input("Ingrese el nombre del lugar de su eleccion: ")
						
						#
						#Mostrar info del lugar
						#
						if lugarElecto == "1":
							#Regresar
							print("")
						elif lugarElecto != "1":
							#Se muestra la info del lugar electo
							print("\nINFORMACION DEL LUGAR "+str(lugarElecto.upper())+":")
							#Funcion de mostrar la info del lugar
							menuComentarios = "0"
							while (menuComentarios != "1") and (menuComentarios != "2"):
								menuComentarios = input("""
	1. Ingresar un comentario
	2. Regresar
	Opcion: """)
								if menuComentarios == "1":
									print("\nSU COMENTARIO:")
									coment = input("Ingrese su comentario: ")
									puntuacion = input("Ingrese la puntuacion del lugar (sobre 5): ")
									comentario = {
												'Comentario': coment,
												'Puntuacion': puntuacion
												}
									opcionesComentario = "0"
									while (opcionesComentario != "1") and (opcionesComentario != "2"):
										opcionesComentario = input("""
	1. Enviar
	2. Cancelar
	Opcion: """)
										if opcionesComentario == "1":
											#Insertar el comentario en la base de datos
											print("Enviado correctamente")
										elif opcionesComentario == "2":
											print("El envio se cancelo correctamente")
										else:
											print("Opcion Invalida")

								elif menuComentarios == "2":
									#Regresar
									print("")
								else:
									print("Opcion Invalida")

					elif menuCategorias == "3":
						#Regresar
						print("")
					else:
						print("Opcion Invalida")

			elif menuConsulta == "2":
				#
				#Recomendar
				#
				print("")
				departamento = input("Ingrese un departamento: ")
				categoria = input("Es 1. Restaurante o 2. Entretenimiento: ")
				nombre = input("Ingrese el nombre del lugar: ")
				direccion = input("Ingrese la direccion: ")
				telefono = input("Ingrese el telefono del lugar: ")
				web = input("Ingrese la pagina web: ")
				horario = input("Ingrese el horario de servicio: ")
				descripcion = input("Ingrese la descripcion del lugar: ")
				comentario = input("Ingrese un comentario del lugar: ")
				puntuacion = input("Ingrese la puntuacion del lugar (sobre 5): ")

				lugar = {
				'Departamento': departamento,
				'Categoria': categoria,
				'Nombre': nombre,
				'Direccion': direccion,
				'Telefono': telefono,
				'Web': web,
				'Horario': horario,
				'Descripcion': descripcion,
				'Comentarios':[{
							'Comentario': comentario,
							'Puntuacion': puntuacion
							}]
				}

				opcionesRecomendar = "0"
				while (opcionesRecomendar != "1") and (opcionesRecomendar != "2"):
						
					opcionesRecomendar = input("""
	1. Enviar
	2. Cancelar
	Opcion: """)

					if opcionesRecomendar == "1":
						#coleccionLugares.insert(lugar)
						print("Enviado correctamente.")
					elif opcionesRecomendar == "2":
						print("El envio se cancelo.")
					else:
						print("Opcion Invalida.")
				
			elif menuConsulta == "3":
				#Regresar al menu principal
				print("")
			else:
				print("Opcion Invalida")

#
#	Ingreso de Admin
#
	elif menuPantallaInicio == "2":
		#Ingreso Admin
		usuario = input("\nIngrese su usuario: ")
		contrasena = input("Ingrese su contrasena: ")
		
		menuIngreso = "0"
		while (menuIngreso != "1") and (menuIngreso != "2"):
			menuIngreso = input("""
	1. Entrar
	2. Cancelar
	Opcion: """)

			if menuIngreso == "1":
				#Ingreso de admin
				autenticado = moduloTuristicGT.autenticarCuenta(coleccionUsuarios, usuario, contrasena)
				if autenticado:
					print("Bienvenido "+str(usuario))
				else:
					print("\nUsuario o Contrasena incorrectos.")

			elif menuIngreso == "2":
				print("")
			else:
				print("Opcion Invalida")


	elif menuPantallaInicio == "3":
		#Salir
		print("Adios")
	else:
		print("Opcion invalida")