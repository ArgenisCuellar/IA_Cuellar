import re
texto = "¿Van al zoológico?"
buscar = re.findall("zo{2}lógico", texto) 
# con una expresion regular podemos generar busquedas mas especificas como buscar algun patron en especifico 
# en este caso el {2} indica que busca la o 2 veces, dando como final la busqueda de zoologico
# estas expresiones regulares son muy utiles al buscar alguna informacion especifica asi como validar datos o patrones en registro de datos.

if buscar:
	print("Hay al menos una coincidencia.")
else:
	print("No hay coincidencias.")