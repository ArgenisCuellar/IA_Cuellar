#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo') # 4 argumentos
colores('lila', 'negro', 'rojo') # 3 argumentos
colores('rosa') # 1 argumento
colores('marrón', 'naranja') # 2 argumentos

#Completa el siguiente pedazo de codigo
def colores2(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores2('Rojo','Blanco')