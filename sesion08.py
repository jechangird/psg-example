print('tupla de enteros')
enteros = (1,2,3,4,5,6)
print(enteros)
print(type(enteros))

print('indexado positivo de una tupla')
tupla = (1,2.0,'hola',True)
print(tupla[0], type(tupla[0]))
print(tupla[1], type(tupla[1]))
print(tupla[2], type(tupla[2]))
print(tupla[3], type(tupla[3]))

print('indexado negativo de una tupla')
tupla = (1,2.0,'hola',True)
print(tupla[-1], type(tupla[-1]))
print(tupla[-2], type(tupla[-2]))
print(tupla[-3], type(tupla[-3]))
print(tupla[-4], type(tupla[-4]))

print('slicing de una tupla')
tupla = (0,1,2,3,4,5,6)
print(tupla)
sub_tupla = tupla[0:5]
print(sub_tupla)

print('slicing de una tupla con saltos')
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print(tupla)
sub_tupla = tupla[0::2]
print(sub_tupla)

print('slicing de una tupla con saltos negativos')
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print(tupla)
sub_tupla = tupla[7:2:-2]
print(sub_tupla)

print('concatenacion de tuplas')
tupla1 = (0,1,2)
tupla2 = (3,4,5)
print(tupla1,tupla2)
concatenar = tupla1 + tupla2
print(concatenar)

print('repeticion de tuplas')
tupla = (0,1,2,3,4,5,6,7,8,9,10)
repetir = tupla * 3
print(tupla)
print(repetir)

print ("Asignación múltiple")
persona = ("Jhon", "Doe", 22, 1.75)
nombre, apellido, edad, estatura = persona
print (persona)
print (nombre)
print (apellido)
print (edad)
print (estatura)

#para saber el indice de un valor
print ("Método index(valor)")
tupla = (1,2.0, "hola", True)
print (tupla.index(2.0))
print (tupla.index("hola"))

#para saber cuantas veces aparece un valor en una tupla
print ("Método count(valor)")
tupla = (1, 2.0, "hola", False, "hola", "HOLA")
print (tupla.count(1))
print (tupla.count("hola"))
print (tupla.count(10))

print ("Función len()")
tupla = (1,2.0, "hola", True)
longitud = len(tupla)
print (tupla)
print (longitud)

print ("Función max()")
tupla = (1,2,10,5,8,0)
maximo = max(tupla)
print (tupla)
print (maximo)

print ("Función min()")
tupla = ("a","z","c","b","f","d")
minimo = min(tupla)
print (tupla)
print (minimo)

print ("Función sum()")
tupla = (1.0, 0.5, 2.5, 3.1)
suma = sum(tupla)
print (tupla)
print (suma)

print ("Tuplas anidadas")
tupla = (1,2,3, (4,5,6))
print (tupla)
print (tupla, type(tupla))
print (tupla[3], type(tupla[3]))
print (tupla[3][0], type(tupla[3][0]))









