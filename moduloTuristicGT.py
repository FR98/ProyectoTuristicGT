#Autores:
#Maria Fernanda Remis 18024
#Gabriela Garza 18101
#Filiberto Morales 18321
#Andy Castillo 18040
#Francisco Rosal 18676
#25/04/18
#Modulo TuristicGT

def esNumero (num):
    try:
        float(num)
        return True
    except:
        return False

def opcionValida (x,a,b):
    if x>a and x<b:
        return True
    else:
        return False

def menuInicio ():
    return """
    Bienvenido a TuristicGT
	    MENU:
	1. Consulta
	2. Ingreso Admin
	3. Salir """

def menuConsulta ():
    return """
            MENU:
	1. Departamentos
	2. Recomendar
	3. Regresar """

def menuCategorias ():
    return """
            MENU:
        1. Restaurantes
	2. Entretenimiento
	3. Regresar """

def opcionesRecomendar ():
    return """
        1. Aceptar
	2. Cancelar """

