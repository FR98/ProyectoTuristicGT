#Autores:
#Maria Fernanda Remis 18024
#Gabriela Garza 18101
#Filiberto Morales 18321
#Andy Castillo 18040
#Francisco Rosal 18676
#25/04/18
#Modulo TuristicGT

import pymongo

def autenticarCuenta(bdColeccion, user, password):
	#Autenticacion de ingreso
	objeto = bdColeccion.find({"Usuario":str(user)})
	for i in objeto:
		for j in i:
			if j == "Contrasena":
				if i[j] == password:
					return True
				else:
					return False

def crearDiccLugar(departamento, categoria, nombre, direccion, telefono, web, horario, descripcion, comentario, puntuacion):
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
	return lugar

def crearDiccUser(nombre, apellido, usuario, contrasena):
	user = {
		'Nombre': nombre,
		'Apellido': apellido,
		'Usuario': usuario,
		'Contrasena': contrasena
	}
	return user

def menuInicio():
	#Menu principal
	return """
	Bienvenido a TuristicGT
		MENU:
	1. Consulta
	2. Ingreso Admin
	3. Salir"""

def menuConsulta():
	#Menu consulta
	return """
		MENU CONSULTA:
	1. Departamentos
	2. Recomendar
	3. Regresar"""

def menuCategorias(dep):
	#Menu categorias
	return """
		MENU DEPARTAMENTO """+str(dep.upper())+""":
	1. Restaurantes
	2. Entretenimiento
	3. Regresar"""

def menuComentarios():
	#Menu comentarios
	return """
	1. Ingresar un comentario
	2. Regresar"""

def opcionesComentario():
	#Opciones comentario
	return """
	1. Enviar
	2. Cancelar"""

def opcionesRecomendar():
	#Opciones recomendar
	return """
	1. Enviar
	2. Cancelar"""

def menuIngreso():
	#Menu ingreso
	return """
	1. Entrar
	2. Cancelar"""

def menuAdmin():
	#Menu admin
	return """
		MENU ADMIN:
	1. Departamentos
	2. Ingresar un nuevo lugar
	3. Ver Recomendaciones
	4. Registrar un nuevo admin
	5. Logout"""

def opcionesIngresar():
	#Opciones ingresar
	return """
	1. Ingresar
	2. Cancelar"""