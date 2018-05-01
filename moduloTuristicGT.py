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
	return """
Bienvenido a TuristicGT
	MENU:
1. Consulta
2. Ingreso Admin
3. Salir """

def menuConsulta():
	return """
	MENU CONSULTA:
1. Departamentos
2. Recomendar
3. Regresar """

def menuCategorias(dep):
	return """
	MENU DEPARTAMENTO """+str(dep.upper())+""":
1. Restaurantes
2. Entretenimiento
3. Regresar """

def autenticarCuenta(bdColeccion, user, password):
	#ARREGLAR ESTO
	if bdColeccion.find({"Usuario":str(user)}) and bdColeccion.find({"Contrasena":str(password)}):
		return True
	else:
		return False
