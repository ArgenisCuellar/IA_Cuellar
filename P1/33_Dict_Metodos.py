teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoria': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1 # eliminar el teclado 1 entero
del teclado2['Categoria'] # eliminar categoria del teclado 2 
del teclado2['Precio'] # eliminar precio del teclado 2

print(teclado2['Modelo'])