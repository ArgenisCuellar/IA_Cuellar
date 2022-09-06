class Usuario:
	nombre = ''
	apellidos = ''

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario()

usuario001.nombre = 'Enrique'
usuario001.apellidos = 'Barros Fernández'

usuario001.imprime_datos()

## Ejemplo donde creamos una clase Usuario con dos atributos nombre y apellidos, dentro con una funcion imprime_datos que llama a los
#atributos y permite que accedan a ellos.