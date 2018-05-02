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
coleccionRecomendaciones = db.recomendaciones

menuPantallaInicio = "0"
#Ciclo principal
Mientras menuPantallaInicio es distinto a "3":
	Mostrar menuInicio()
	menuPantallaInicio = input("Opcion: ")
#CONSULTA
	Si menuPantallaInicio es igual a "1":
		#Consulta
		menuConsulta = "0"
		#Ciclo menu consulta
		Mientras menuConsulta es distinto a "3":
			Mostrar menuConsulta()
			menuConsulta = input("Opcion: ")
			Si menuConsulta es igual a "1":
				#DEPARTAMENTOS
				menuCategorias = "0"
				#Ciclo menu categorias
				Mientras menuCategorias es distinto a "3":
					departamento = input("Ingrese un departamento: ")
					Mostrar menuCategorias()
					menuCategorias = input("Opcion: ")
					Si (menuCategorias es igual a "1") o (menuCategorias es igual a "2"):
						#SELECCIONAR LUGAR
						Si menuCategorias es igual a "1":
							#RESTAURANTES
							Mostrar ("RESTAURANTES EN ..... (BD):")
							Mostrar ("1. Regresar")
							#Funcion mostrar los restaurantes del departamento en la bd
							lugarElecto = input("Ingrese el nombre del restaurante: ")
						sino:
							#ENTRETENIMIENTO
							Mostrar ("ENTRETENIMIENTO EN ..... (BD):")
							Mostrar ("1. Regresar")
							#Funcion mostrar los lugares de entretenimiento del departamento en la bd
							lugarElecto = input("Ingrese el nombre del lugar: ")
						#MOSTRAR INFORMACION DEL LUGAR
						Si lugarElecto es igual a "1":
							#Regresar
							
						sino lugarElecto es distinto a "1":
							#Se muestra la info del lugar electo
							Mostrar ("INFORMACION DEL LUGAR:")
							#Funcion de mostrar la info del lugar
							menuComentarios = "0"
							#Ciclo menu comentarios
							Mientras (menuComentarios es distinto a "1") y (menuComentarios es distinto a "2"):
								Mostrar menuComentarios()
								menuComentarios = input("Opcion: ")
								Si menuComentarios es igual a "1":
									Mostrar ("SU COMENTARIO:")
									coment = input("Ingrese su comentario: ")
									puntuacion = input("Ingrese la puntuacion: ")
									#Se crea diccionario comentario
									comentario = {
												'Comentario': coment,
												'Puntuacion': puntuacion
												}
									opcionesComentario = "0"
									#Ciclo opciones comentario
									Mientras (opcionesComentario es distinto a "1") y (opcionesComentario es distinto a "2"):
										Mostrar opcionesComentario()
										opcionesComentario = input("Opcion: ")
										Si opcionesComentario es igual a "1":
											#Se inserta el comentario en la base de datos
											Mostrar ("Enviado correctamente")
										sino opcionesComentario es igual a "2":
											Mostrar ("El envio se cancelo correctamente")
										sino:
											Mostrar ("Opcion Invalida")

								sino menuComentarios es igual a "2":
									#Regresar
									
								sino:
									Mostrar ("Opcion Invalida")

					sino menuCategorias es igual a "3":
						#Regresar
						
					sino:
						Mostrar ("Opcion Invalida")

			sino menuConsulta es igual a "2":
				#RECOMENDAR
				
				departamento = input("Ingrese un departamento: ")
				categoria = input("Es Restaurante o Entretenimiento: ")
				nombre = input("Ingrese el nombre del lugar: ")
				direccion = input("Ingrese la direccion: ")
				telefono = input("Ingrese el telefono del lugar: ")
				web = input("Ingrese la pagina web: ")
				horario = input("Ingrese el horario de servicio: ")
				descripcion = input("Ingrese la descripcion del lugar: ")
				comentario = input("Ingrese un comentario: ")
				puntuacion = input("Ingrese la puntuacion: ")
				#Se crea diccionario del lugar con funcion
				lugar = moduloTuristicGT.crearDiccLugar(departamento, categoria, nombre, direccion, telefono, web, horario, descripcion, comentario, puntuacion)

				opcionesRecomendar = "0"
				#Ciclo opciones recomendar
				Mientras (opcionesRecomendar es distinto a "1") y (opcionesRecomendar es distinto a "2"):
					Mostrar opcionesRecomendar()
					opcionesRecomendar = input("Opcion: ")
					Si opcionesRecomendar es igual a "1":
						#Se inserta el lugar en la base de datos de recomendaciones
						coleccionRecomendaciones.insert(lugar)
						Mostrar ("Enviado correctamente.")
					sino opcionesRecomendar es igual a "2":
						Mostrar ("El envio se cancelo.")
					sino:
						Mostrar ("Opcion Invalida.")
				
			sino menuConsulta es igual a "3":
				#Regresar al menu principal
				
			sino:
				Mostrar ("Opcion Invalida")
#INGRESO ADMIN
	sino menuPantallaInicio es igual a "2":
		#INGRESO ADMIN
		usuario = input("Ingrese su usuario: ")
		contrasena = input("Ingrese su contrasena: ")
		menuIngreso = "0"
		#Ciclo menu ingreso admin
		Mientras (menuIngreso es distinto a "1") y (menuIngreso es distinto a "2"):
			Mostrar menuIngreso()
			menuIngreso = input("Opcion: ")

			Si menuIngreso es igual a "1":
				#Autenticacion de ingreso
				autenticado = moduloTuristicGT.autenticarCuenta(coleccionUsuarios, usuario, contrasena)
				Si autenticado:
					Mientras autenticado:
						#Autenticacion valida
						Mostrar ("BIENVENIDO ")
						Mostrar menuAdmin()
						menuAdmin = input("Opcion: ")
						Si menuAdmin es igual a "1":
							#DEPARTAMENTOS
							Mostrar ("Error #404. Pagina en construccion.")
						sino menuAdmin es igual a "2":
							#INGRESAR UN NUEVO LUGAR
							
							departamento = input("Ingrese un departamento: ")
							categoria = input("Es Restaurante o Entretenimiento: ")
							nombre = input("Ingrese el nombre del lugar: ")
							direccion = input("Ingrese la direccion: ")
							telefono = input("Ingrese el telefono del lugar: ")
							web = input("Ingrese la pagina web: ")
							horario = input("Ingrese el horario de servicio: ")
							descripcion = input("Ingrese la descripcion del lugar: ")
							comentario = ""
							puntuacion = ""
							#Se crea diccionario del lugar con funcion
							lugar = moduloTuristicGT.crearDiccLugar(departamento, categoria, nombre, direccion, telefono, web, horario, descripcion, comentario, puntuacion)

							opcionesIngresar = "0"
							#Ciclo opciones ingresar
							Mientras (opcionesIngresar es distinto a "1") y (opcionesIngresar es distinto a "2"):
								Mostrar opcionesIngresar()
								opcionesIngresar = input("Opcion: ")
								Si opcionesIngresar es igual a "1":
									#Se inserta el lugar en la base de datos
									coleccionLugares.insert(lugar)
									Mostrar ("Ingresado correctamente.")
								sino opcionesIngresar es igual a "2":
									Mostrar ("El ingreso se cancelo.")
								sino:
									Mostrar ("Opcion Invalida.")

						sino menuAdmin es igual a "3":
							#VER RECOMENDACIONES
							Mostrar ("Error #404. Pagina en construccion.")
						sino menuAdmin es igual a "4":
							#REGISTRAR UN NUEVO ADMIN
							
							nombre = input("Ingrese el nombre: ")
							apellido = input("Ingrese el apellido: ")
							usuario = input("Inngrese el usuario: ")
							contrasena = input("Ingrese la contrasena: ")
							user = moduloTuristicGT.crearDiccUser(nombre, apellido, usuario, contrasena)

							opcionesRegistrar = "0"
							#Ciclo opciones registrar
							Mientras (opcionesRegistrar es distinto a "1") y (opcionesRegistrar es distinto a "2"):
								Mostrar opcionesRegistrar()
								opcionesRegistrar = input("Opcion: ")
								Si opcionesRegistrar es igual a "1":
									#Se inserta el usuario en la base de datos
									coleccionUsuarios.insert(user)
									Mostrar ("Registrado correctamente.")
								sino opcionesRegistrar es igual a "2":
									Mostrar ("El registro se cancelo.")
								sino:
									Mostrar ("Opcion Invalida.")

						sino menuAdmin es igual a "5":
							#Logout
							autenticado = False
							Mostrar ("HASTA LA PROXIMA ")
						sino:
							Mostrar ("Opcion Invalida")

				sino:
					Mostrar ("Usuario o Contrasena incorrectos.")

			sino menuIngreso es igual a "2":
				
			sino:
				Mostrar ("Opcion Invalida")

	sino menuPantallaInicio es igual a "3":
		#Salir
		Mostrar ("Adios")
	sino:
		Mostrar ("Opcion invalida")