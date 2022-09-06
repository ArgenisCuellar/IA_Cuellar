variable = "Correcto."

try:
	print(variable)
except:
	print("La variable no está declarada.")

#Los manejos de expeciones nos sirven para evitar que el programa sea cerrado por algun tipo de error 
# estos errores pueden ser especificados despues de la palabra clave except, y puede ejecutar un codigo en caso de que se encuentra dicha
# excepcion 

# funciona intentado ejecuar el bloque del codigo del try, y en caso de que se genere alguna excepcion ejecutara el bloque del except 

# puede ser utilizado al introducir datos, por ejemplo buscando que el usurio ingrese un numeor e ingresa una letra, esto ocasionaria un 
#excepcion haciendo que el programa terminase, con un manejo de excepciones podriamos evitar esto e enviar un mensaje al usuario 
# indicandole el error.