
class Usuario:

    def __init__(self, nombre, apelidos) :
        self.nombre = nombre
        self.apellidos = apelidos
        
    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)
        

class UsuariosPremium(Usuario):
    def __init__(self, nombre, apelidos, instagram):
        self.nombre = nombre
        self.apellidos = apelidos
        self.instagram = instagram
        

#Con el codigo anterior al tener dos innit aunque haya heredado el sobreescribirlo en la subclase este tomara el de esta
# si el objeto le pertenece a la clase.