'''Ingresa por teclado dos coordenadas 'x','y' 
y una ubicación, almacena los 3 valores en una tupla 
e imprime el resultado'''

coordenada1 = input('Introduce la coordenada 1: ')
coordenada2 = input('Introduce la coordenada 2: ')
ubicacion = input('Introduce una ubicacion: ')

tupla = tuple()
tupla = coordenada1, coordenada2, ubicacion  


print(tupla,type(tupla))
