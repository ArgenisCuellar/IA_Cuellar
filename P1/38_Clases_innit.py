
class Usuario:

    def __init__(self, nombre, apelidos) :
        self.nombre = nombre
        self.apellidos = apelidos
        
    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Enrique', 'Barros Fernández')

usuario002 = Usuario('Javier', 'Gomila Reyes')

##El metodo innit indica que siempre al momento de ser creado el objeto de tipo Usuario, debe indicar nombre y apellidos.

