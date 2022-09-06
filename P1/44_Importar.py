import math

def area(radio):
	resultado = math.pi * radio * radio
	print(resultado)

area(2)


area = lambda radio: (math.pi * radio * radio) #ambas funciones son la misma solo utilizando lambda podemos reducir el tamaño

print(area(2))