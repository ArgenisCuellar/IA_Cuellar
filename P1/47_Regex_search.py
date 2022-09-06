import re
texto = "Bienvenidos a Programación fácil"
busqueda = re.search("i", texto) # con el metodo search en este caso esta buscando una Letra I dentro de la variable texto
# Al encontarla genera un objeto de tipo Match que indica la posicion de lo buscando en el parametro anterior

print(busqueda)