import re
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto) # Este metodo separa las palabras en base a un espacio como indicado en el parametro 
# Generando una lista de todas las palabras separadas por un espacio
print(busqueda)



texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto) # Este metodo remplazara las coincidencias del primer parametro con el 2ndo generando un str
print(busqueda)