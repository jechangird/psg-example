'''Crea un diccionario con las siguientes tuplas de animales
tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
Del diccionario obtén y elimina el valor de la clave 'aves'
Modifica el valor de la clave 'gato' por '🐈'
Cambia la clave perro por perros y su valor por print(diccionario,
type(diccionario))'''

#convertir unatupla a diccionario
tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
diccionario = dict(tupla)
print(diccionario,type(diccionario))

#borrar la clave aves
del diccionario['aves']
print(diccionario,type(diccionario))

#modificar el valor de la clave gato
diccionario['gato'] = '🐈'
print(diccionario,type(diccionario))

#cambiar la clave perro por perros y su valor
diccionario['perros'] = ['🐶','🐕']
del diccionario['perro']
print(diccionario,type(diccionario))

