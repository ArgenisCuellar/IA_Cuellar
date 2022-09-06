import re
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.findall("e", texto) # con el metodo findall mostrara todas las e en un array que haya encontrado en la variable indicada.
print(busqueda)