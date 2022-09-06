
class Usuario:

    def __init__(self, nombre, apelidos) :
        self.nombre = nombre
        self.apellidos = apelidos
        
    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)
        
class UsuariosPremium(Usuario):
    pass

#Indicando dentro de un parentesis seguido de el nombre de la clase podemos indicar de que clase heredara metodos y atributos.