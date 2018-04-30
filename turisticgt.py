#Autores:
#Maria Fernanda Remis 18024
#Gabriela Garza 18101
#Filiberto Morales 18321
#Andy Castillo 18040
#Francisco Rosal 18676
#25/04/18
#Aplicacion TuristicGT

#Se importa el modulo pymongo
import pymongo

#Se crea la conexion con el cliente de Mongo
conexion = pymongo.MongoClient()
#Se establece la base de datos ccon la que se trabaja
db = conexion["turisticgt"]
#Se establece la coleccion con la que se trabaja
coleccion = db.lugares

menuPantallaInicio = "0"
#Ciclo principal
while menuPantallaInicio != "3":
	menuPantallaInicio = input("""
	Bienvenido a TuristicGT
		MENU PRINCIPAL:
	1. Consulta
	2. Ingreso Admin
	3. Salir
	Opcion: """)

	if menuPantallaInicio == "1":
		#Consulta
		menuConsulta = "0"
		while menuConsulta != "3":
			menuConsulta = input("""
		MENU CONSULTA:
	1. Departamentos
	2. Recomendar
	3. Regresar
	Opcion: """)
			if menuConsulta == "1":
				#Departamentos
				menuCategorias = "0"
				while menuCategorias != "3":
					departamento = input("\nIngrese un departamento: ")
					menuCategorias = input("""
		MENU DEPARTAMENTO """+str(departamento.upper())+""":
	1. Restaurantes
	2. Entretenimiento
	3. Regresar
	Opcion: """)
					if menuCategorias == "1":
						#Restaurantes
						print("\nRESTAURANTES EN "+str(departamento.upper()+" (BD):"))
						#Funcion mostrar los restaurantes del departamento en la bd
						restauranteElecto = input("Ingrese el numero del restaurante de su eleccion: ")
						print("\nSe han mostrado todos los lugares")
					elif menuCategorias == "2":
						#Entretenimiento
						print("\nENTRETENIMIENTO EN "+str(departamento.upper()+" (BD):"))
						#Funcion mostrar los lugares de entretenimiento del departamento en la bd
						lugarElecto = input("Ingrese el numero  del lugar de su eleccion: ")
						print("\nSe han mostrado todos los lugares")
					elif menuCategorias == "3":
						print("")
					else:
						print("Opcion Invalida")
			elif menuConsulta == "2":
				#Recomendar
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
						#coleccion.insert(lugar)
						print("Enviado correctamente.")
					elif opcionesRecomendar == "2":
						print("El envio se cancelo.")
					else:
						print("Opcion invalida.")
				
			elif menuConsulta == "3":
				#Regresar al menu principal
				print("")
			else:
				print("Opcion invalida")

	elif menuPantallaInicio == "2":
		#Ingreso Admin
		print("\nError #404. Pagina en construccion, sentimos las molestias")

	elif menuPantallaInicio == "3":
		#Salir
		print("Adios")
	else:
		print("Opcion invalida")