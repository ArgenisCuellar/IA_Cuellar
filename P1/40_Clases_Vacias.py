
class Usuario:

    def __init__(self, nombre, apelidos) :
        self.nombre = nombre
        self.apellidos = apelidos
        
    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Enrique', 'Barros Fernández')

usuario002 = Usuario('Javier', 'Gomila Reyes')

usuario002.nombre = 'Jacinto' 

del usuario002.nombre # Podemos borrar atributos con el metodo del

del usuario002 # al igual que podemos borrar el objeto completo

class NombreClase:
	pass

#Podemos crear una clase vacia con la forma anterior





