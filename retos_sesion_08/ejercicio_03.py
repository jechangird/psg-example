'''Ingresa una cadena por teclado y almacena el valor en una tupla
Concatena la tupla ('¡', ) + tupla almacenada + la tupla ('!', )
Imprime el resultado concatenado
Repite la tupla final 3 veces e imprime el nuevo resultado'''

cadena = input('introduce una cadena:')
cadena = tuple(cadena)
print(cadena, type(cadena))

tupla1 = '!',
tupla2 = '!!',

concatenacion = tupla1 + cadena + tupla2
print(concatenacion)
print(concatenacion * 3)
