
colores = ('rojo','azul','verde','negro') # Generamos tupla con 4 colores

color = input('Ingresa Color: ') #Genearmos un input para que el usuario ingrese un color

if color in colores: # Evaluamos si el color esta en la tupla y en base a eso realizamos un print.
    print('Color: {} admitido.'.format(color))
else:
    print('Color: {} no admitido'.format(color))