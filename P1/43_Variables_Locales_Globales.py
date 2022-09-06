def funcion1():
	global num1 # Utilizando global dentro antes de alguna variable dentro de alguna funcion podremos utilizar el valor de esta desde fuera
	num1 = 10

funcion1()

print(num1)
