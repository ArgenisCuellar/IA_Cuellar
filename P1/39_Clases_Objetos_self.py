

class Usuario:

    def __init__(self, nombre, apelidos) :
        self.nombre = nombre
        self.apellidos = apelidos
        
    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Enrique', 'Barros Fernández')

usuario002 = Usuario('Javier', 'Gomila Reyes')

usuario002.nombre = 'Jacinto' # Utilizando el nombre del objeto.atributo podemos asignar valores previamente establecidos.



