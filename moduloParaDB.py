#Autores:
#Maria Fernanda Remis 18024
#Gabriela Garza 18101
#Filiberto Morales 18321
#Andy Castillo 18040
#Francisco Rosal 18676
#25/04/18
#Modulo paraDB

import pymongo
#Se crea la conexion con el cliente de Mongo
conexion = pymongo.MongoClient()
#Se establece la base de datos ccon la que se trabaja
db = conexion["turisticgt"]
#Se establecen las colecciones con las que se trabajaran
coleccionLugares = db.lugares

def iniciarLugaresDB():
	lugares = [
		{
			'Departamento': "Solola",
			'Categoria': "Restaurante",
			'Nombre': "Cafe loco",
			'Direccion': "Calle Santander Panajachel, Solola",
			'Telefono': 47043588,
			'Web': "",
			'Horario': "9:00 a.m. a 8:00 p.m.",
			'Descripcion': "Ofrecen bebidas con cafe que son deliciosas y que muestran variedad y mucho sabor. Cada semana ofrecen una nueva propuesta de bebida, en Cafe Loco nunca probaras dos veces el mismo sabor.",
			'Comentarios':[{
				'Comentario': "Cafe de alta calidad|Muchas opciones de bebidas frias y calientes",
				'Puntuacion': 5
				},
				{
				'Comentario': "Buena comida",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Solola",
			'Categoria': "Restaurante",
			'Nombre': "Guajimbo's",
			'Direccion': "Santander, panajachel Guatemala",
			'Telefono': 77620063,
			'Web': "",
			'Horario': "",
			'Descripcion': "Churrasqueria sudamericana y centroamericana",
			'Comentarios':[{
				'Comentario': "Buena comida al estilo uruguayo",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Solola",
			'Categoria': "Recreativo",
			'Nombre': "Mirador Rostro Maya",
			'Direccion': "San Juan la laguna, Solola",
			'Telefono': "",
			'Web': "",
			'Horario': "",
			'Descripcion': "Hermoso mirador de San Juan la laguna.",
			'Comentarios':[{
				'Comentario': "Panorama de 360 grados, vista espectacular.",
				'Puntuacion': 5
				}
			]
		},
		{
			'Departamento': "Solola",
			'Categoria': "Recreativo",
			'Nombre': "Museo Lacustre",
			'Direccion': "En las instalaciones del Hotel La osada de Don Rodrigo, final de la calle Santander",
			'Telefono': 77622326,
			'Web': "",
			'Horario': "Lunes a Sabado 8:00 a.m. a 3:00 p.m.",
			'Descripcion': "Este museo se formo con las piezas maas encontradas bajo el agua, en la ciudad que existia en Atitlan",
			'Comentarios':[{
				'Comentario': "Ciudad perdida, Exploracion maya, Hermoso museo.",
				'Puntuacion': 4
				},
				{
				'Comentario': "Buena comida",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Izabal",
			'Categoria': "Restaurante",
			'Nombre': "Ranchon Mary",
			'Direccion': "CA-13, Rio Dulce",
			'Telefono': 79305103,
			'Web': "",
			'Horario': "Todos los dias 6:30 a.m. a 8:30 p.m.",
			'Descripcion': "Restauante de mariscos",
			'Comentarios':[{
				'Comentario': "Las mejores mojarras del area",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Izabal",
			'Categoria': "Restaurante",
			'Nombre': "Happy Fish",
			'Direccion':" Livingston, Izabal, Calle principal de comercio",
			'Telefono': 79470661,
			'Web': "",
			'Horario': "Todos los dias 7:00 a.m. a 10:00 p.m.",
			'Descripcion': "Restauante de mariscos",
			'Comentarios':[{
				'Comentario': "Apto para niños",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Izabal",
			'Categoria': "Recreacion",
			'Nombre': "El boqueron",
			'Direccion':" El estor, Izabal",
			'Telefono': "",
			'Web': "",
			'Horario': "8:00 a.m. a 5:00 p.m.",
			'Descripcion': "Paseo por las aguas",
			'Comentarios':[{
				'Comentario': "Recorrido genial en cayuco",
				'Puntuacion': 5
				}
			]
		},
		{
			'Departamento': "Izabal",
			'Categoria': "Recreacion",
			'Nombre': "Casa Gandau",
			'Direccion':" Rio Dulce, Izabal",
			'Telefono': 55113280,
			'Web': "",
			'Horario': "8:00 a.m. a 4:00 p.m.",
			'Descripcion': "Relajarte en medio de la naturaleza",
			'Comentarios':[{
				'Comentario': "Casa lujosa",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Jutiapa",
			'Categoria': "Restaurante",
			'Nombre': "Drock's seafood & steak restaurant",
			'Direccion':" Jutiapa",
			'Telefono': 78467869,
			'Web': "",
			'Horario': "7:00 a.m. a 9:00 p.m.",
			'Descripcion': "Disfruta de Mariscos y carnes",
			'Comentarios':[{
				'Comentario': "un hermosos lugar",
				'Puntuacion': 4
				},
				{
				'Comentario': "Buena comida",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Jutiapa",
			'Categoria': "Restaurante",
			'Nombre': "pepepanes",
			'Direccion':" calle 6 de septiembre 1-17,Jutiapa 22000",
			'Telefono': 78441088,
			'Web': "",
			'Horario': "11:00 a.m. a 8:00 p.m.",
			'Descripcion': "Comida rapida jutiapaneca",
			'Comentarios':[{
				'Comentario': "ideal para niños",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Jutiapa",
			'Categoria': "Recreacion",
			'Nombre': "Finca D'Rocks",
			'Direccion':" Aldea Las Flores, El Progreso, Jutiapa",
			'Telefono': 78234906,
			'Web': "",
			'Horario': "7:00 a.m. a 9:00 p.m.",
			'Descripcion': "piscina con vista a volcanes",
			'Comentarios':[{
				'Comentario': "un hermosos lugar con instalaciones rusticas",
				'Puntuacion': 5
				}
			]
		},
		{
			'Departamento': "Jutiapa",
			'Categoria': "Recreacion",
			'Nombre': "Eco Parque Mongoy",
			'Direccion':" Kilometro 156 Jutiapa",
			'Telefono': 53755410,
			'Web': "",
			'Horario': "10:00 a.m. a 5:00 p.m.",
			'Descripcion': "Piscinas al lado del rio",
			'Comentarios':[{
				'Comentario': "Ideal para excursiones",
				'Puntuacion': 4
				},
				{
				'Comentario': "Buena comida",
				'Puntuacion': 4
				}
			]
		}
	,
		{
			'Departamento': "suchitepequez",
			'Categoria': "Restaurante",
			'Nombre': "Restaurante Casa Vieja",
			'Direccion':" 7 avenida calle 3-46 zona 1.",
			'Telefono': 53105499,
			'Web': "",
			'Horario': "7:00 a.m. a 5:30 p.m.",
			'Descripcion': "Comida excelente",
			'Comentarios':[{
				'Comentario': "para compartir en familia",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "suchitepequez",
			'Categoria': "Restaurante",
			'Nombre': "El Rancho",
			'Direccion':" km 113 CA2 interio estacion shell cocales, patulul, suchitepequez",
			'Telefono': 78719796,
			'Web': "",
			'Horario': "7:00 a.m. a 9:00 p.m.",
			'Descripcion': "Comida del mar",
			'Comentarios':[{
				'Comentario': "Su especialidad la tilapi",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Suchitepequez",
			'Categoria': "Recreacion",
			'Nombre': "El Chorro del carmen",
			'Direccion':" km164 desde la capital, Zunilito, suchitepequez 01018",
			'Telefono': 42107370,
			'Web': "",
			'Horario': "9:30 a.m. a 5:00 p.m.",
			'Descripcion': "piscinas",
			'Comentarios':[{
				'Comentario': "buen lugar para contratar lancha privada",
				'Puntuacion': 5
				}
			]
		},
		{
			'Departamento': "Suchitepequez",
			'Categoria': "Recreacion",
			'Nombre': "Parque Ecologico Cristiano La Merced",
			'Direccion':" Jutiapa",
			'Telefono': 57805821,
			'Web': "",
			'Horario': "10:00 a.m. a 4:00 p.m.",
			'Descripcion': "Para disfrutar con mi familia",
			'Comentarios':[{
				'Comentario': "elegante, muy bonito y divertido",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Zacapa",
			'Categoria': "Restaurante",
			'Nombre': "El Establo",
			'Direccion':" Zacapa",
			'Telefono': 79412709,
			'Web': "",
			'Horario': "6:00 a.m. a 10:00 p.m.",
			'Descripcion': "Variedad de comida",
			'Comentarios':[{
				'Comentario': "ambiente agradable",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Zacapa",
			'Categoria': "Restaurante",
			'Nombre': "Los Chevys WJB",
			'Direccion':"Zacapa",
			'Telefono': 79410121,
			'Web': "",
			'Horario': "9:00 a.m. a 10:00 p.m.",
			'Descripcion': "Deliciosas Tortillas De Harina",
			'Comentarios':[{
				'Comentario': "exquisito sabor",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Zacapa",
			'Categoria': "Recreacion",
			'Nombre': "Valle Dorado",
			'Direccion':"KM 149, carr Jacobo arbenz Guzman",
			'Telefono': 42107370,
			'Web': "",
			'Horario': "9:30 a.m. a 5:00 p.m.",
			'Descripcion': "Parque acuatico y recrativo",
			'Comentarios':[{
				'Comentario': "Bellas instalaciones",
				'Puntuacion': 5
				}
			]
		},
		{
			'Departamento': "Zacapa",
			'Categoria': "Recreacion",
			'Nombre': "Museo de Paleontologia Estanzuela",
			'Direccion':" 5 Avenida, Estanzuela",
			'Telefono': 79336108,
			'Web': "",
			'Horario': "8:00 a.m. a 5:00 p.m.",
			'Descripcion': "Museo de historia natural",
			'Comentarios':[{
				'Comentario': "No tiene costo de ingreso",
				'Puntuacion': 4
				}
			]
		}
	,
		{
			'Departamento': "Sacatepequez",
			'Categoria': "Restaurante",
			'Nombre': "Fridas",
			'Direccion':" 5a Avenida Norte #29, Arco de Santa Calina, Antigua Guatemala 03001",
			'Telefono': 78321296,
			'Web': "",
			'Horario': "12:00 p.m. a 1:00 a.m.",
			'Descripcion': "Variedad de comida mexicana",
			'Comentarios':[{
				'Comentario': "Excelente atencion",
				'Puntuacion': 4
				},
				{
				'Comentario': "Buena comida",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Sacatepequez",
			'Categoria': "Restaurante",
			'Nombre': "Nim Guaa",
			'Direccion':"carr. a San Lucas Sacatepequez",
			'Telefono': 78303174,
			'Web': "",
			'Horario': "9:00 a.m. a 10:00 p.m.",
			'Descripcion': "Deliciosa comida nacional",
			'Comentarios':[{
				'Comentario': "Muy bonito lugar",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Sacatepequez",
			'Categoria': "Recreacion",
			'Nombre': "Choco Museo",
			'Direccion':"4a calle Oriente, Antigua Guatemala",
			'Telefono': 78324520,
			'Web': "",
			'Horario': "10:30 a.m. a 6:30 p.m.",
			'Descripcion': "Museo de Chocolate",
			'Comentarios':[{
				'Comentario': "Bellas instalaciones, chocolates ricos",
				'Puntuacion': 5
				}
			]
		},
		{
			'Departamento': "Sacatepequez",
			'Categoria': "Recreacion",
			'Nombre': "Casa Popenoe",
			'Direccion':" 5a calle Oriente, Antigua Guatemala",
			'Telefono': 23387959,
			'Web': "",
			'Horario': "9:00 a.m. a 4:00 p.m.",
			'Descripcion': "Centro Cultural",
			'Comentarios':[{
				'Comentario': "Residencia Colonial hermosa",
				'Puntuacion': 5
				}
			]
		}
	,
		{
			'Departamento': "Peten",
			'Categoria': "Restaurante",
			'Nombre': "Katok Peten",
			'Direccion':" peten",
			'Telefono': 78403387,
			'Web': "",
			'Horario': "6:00 a.m. a 10:00 p.m.",
			'Descripcion': "Variedad de comida nacional",
			'Comentarios':[{
				'Comentario': "Decoracion maya",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Peten",
			'Categoria': "Restaurante",
			'Nombre': "Legumbres Maya",
			'Direccion':"Calle Centro America, Flores",
			'Telefono': 30417735,
			'Web': "",
			'Horario': "8:00 a.m. a 9:00 p.m.",
			'Descripcion': "Restaurante Vegetariano",
			'Comentarios':[{
				'Comentario': "exquisito sabor",
				'Puntuacion': 5
				}
			]
		},
		{
			'Departamento': "Peten",
			'Categoria': "Recreacion",
			'Nombre': "ZOO Petencito",
			'Direccion':"carr. a San Miguel",
			'Telefono': "",
			'Web': "",
			'Horario': "8:00 a.m. a 6:00 p.m.",
			'Descripcion': "zoologico",
			'Comentarios':[{
				'Comentario': "Un lugar hermoso",
				'Puntuacion': 5
				}
			]
		},
		{
			'Departamento': "Peten",
			'Categoria': "Recreacion",
			'Nombre': "Jorge's Rope Swing",
			'Direccion':" Peten ",
			'Telefono': 31963196,
			'Web': "",
			'Horario': "8:00 a.m. a 5:00 p.m.",
			'Descripcion': "Baños termales",
			'Comentarios':[{
				'Comentario': "Atraccion turistica bonita",
				'Puntuacion': 4
				}
			]
		}
	,
		{
			'Departamento': "Chiquimula",
			'Categoria': "Restaurante",
			'Nombre': "Pizza Burguer Diner #2",
			'Direccion':" Esquipulas",
			'Telefono': 79430888,
			'Web': "",
			'Horario': "7:00 a.m. a 10:00 p.m.",
			'Descripcion': "Variedad de comida",
			'Comentarios':[{
				'Comentario': "La mejor pizza de oriente",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Chiquimula",
			'Categoria': "Restaurante",
			'Nombre': "La Casa de Papa Tono y Mama Lola",
			'Direccion':"KM 175 carretera a Ipala, Los laureles, Sabana Grande, Chiquimula",
			'Telefono': 51449964,
			'Web': "",
			'Horario': "10:00 a.m. a 9:00 p.m.",
			'Descripcion': "Restaurante de Carnes Asadas",
			'Comentarios':[{
				'Comentario': "exquisito sabor, ideal para niños",
				'Puntuacion': 4
				}
			]
		},
		{
			'Departamento': "Chiquimula",
			'Categoria': "Recreacion",
			'Nombre': "Parque Chatun",
			'Direccion':"KM 226 carr a Honduras, Esquipulas 20007",
			'Telefono': 78730909,
			'Web': "",
			'Horario': "9:30 a.m. a 5:00 p.m.",
			'Descripcion': "Parque acuatico y recrativo",
			'Comentarios':[{
				'Comentario': "Bellas piscinas",
				'Puntuacion': 5
				}
			]
		},
		{
			'Departamento': "Chiquimula",
			'Categoria': "Recreacion",
			'Nombre': "Piedra de los compadres",
			'Direccion':" RN-18 Esquipulas",
			'Telefono': "",
			'Web': "",
			'Horario': "abierto las 24 horas",
			'Descripcion': "Centro Cultural",
			'Comentarios':[{
				'Comentario': "delicioso jugo de caña y paseo por tuc-tuc",
				'Puntuacion': 4
				}
			]
		}
	]

	for i in lugares:
		coleccionLugares.insert(i)