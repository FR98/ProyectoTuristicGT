#Autores:
#Maria Fernanda Remis 18024
#Gabriela Garza 18101
#Filiberto Morales 18321
#Andy Castillo 18040
#Francisco Rosal 18676
#25/04/18
#Modulo TuristicGT

import pymongo

def menuInicio():
	#Menu principal
	return """
Bienvenido a TuristicGT
	MENU:
1. Consulta
2. Ingreso Admin
3. Salir """

def menuConsulta():
	#Menu consulta
	return """
	MENU CONSULTA:
1. Departamentos
2. Recomendar
3. Regresar """

def menuCategorias(dep):
	#Menu categorias
	return """
	MENU DEPARTAMENTO """+str(dep.upper())+""":
1. Restaurantes
2. Entretenimiento
3. Regresar """

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