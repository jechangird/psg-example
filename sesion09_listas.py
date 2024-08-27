print('lista de enteros')
lista = [1,2,3,4,5]
print(lista)

print ("Lista de cadenas")
mi_lista = ["hola", "mundo", "python"]
print (mi_lista)

print ("Lista mixta")
mi_lista = [1, "hola", 3.14, "mundo", 5]
print (mi_lista)

'''Se usa la función list() para crear una lista a partir de una secuencia

Su utilidad es convertir una tupla, cadena o conjunto en una lista'''

print ("Lista a partir de una cadena")
mi_lista = list("hola mundo")
print (mi_lista)

print ("Lista a partir de una tupla")
mi_tupla = (1,2,3,4,5)
print (mi_tupla)
mi_lista = list(mi_tupla)
print (mi_lista)

print ("Lista por comprensión")
mi_lista = [x for x in range(10)]
print (mi_lista)

print ("Indexación positivo de una lista")
lista = [1, "hola", 3.14, (1,2)]
print(lista)
print (lista[0], type(lista[0])) 
print (lista[1], type(lista[1])) 
print (lista[2], type(lista[2])) 
print (lista[3], type(lista[3])) 

print ("Indexación negativo de una lista")
lista = [1, "hola", 3.14, (1,2)]
print (lista[-1], type(lista[-1]))
print (lista[-2], type(lista[-2]))
print (lista[-3], type(lista[-3]))
print (lista[-4], type(lista[-4]))

print ("Modificación de una lista")
lista = [1, "hola", 3.14, (1,2)]
print (lista)
lista[0] = 2
lista[1] = "mundo"
print (lista)

print ("Slicing de una lista")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[2:7]
print (sub_lista)
print (type(sub_lista))

print ("Slicing con paso positivo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[0:9:3]
print (sub_lista)

print ("Slicing con paso negativo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[8:2:-4]
print (sub_lista)

print ("Slicing negativo con paso positivo")
lista = ["P", "y", "t", "h", "o", "n", "L", "a", "P", "a", "z"]
print (lista)
sub_lista = lista[-1:-8:2]
print (sub_lista)

print ("Concatenación de listas")
lista1 = [1,2,3]
lista2 = ["a","b","c"]
concatenar = lista1 + lista2
print (lista1, lista2)
print (concatenar)
print (type(concatenar))

print ("Repetición de listas")
lista = [True, False]
repetir = lista * 3
print (lista)
print (repetir)
print (type(repetir))

#metodos de busqueda
#busca donde aparece el objeto la primera vez, sino lo encuentra lanza un error
print ("Método index(valor)")
lista = [1,True,3.14,"hola",5]
valor = "hola"
print (valor, lista.index(valor))
valor = 3.14
print (valor, lista.index(valor))

#recibe un valor y devuelve el nro de veces que aparece en la lista
print ("Método count(valor)")
lista = [1,True,3.14,"hola",5, True, True, 3.140]
valor = True
print (valor, lista.count(valor))
valor = 3.14
print (valor, lista.count(valor))

#metodos de adicion, modifican la lista original
#insert(i,valor) inserta un valor en la posicion i
print ("Método insert(i, valor)")
lista = [1,2,3,4,5]
print (lista)
lista.insert(2, "OwO")
print (lista)

#append(valor), agrega un elemento al final de la lista
print ("Método append(valor)")
lista = [1,2,3,4,5]
print (lista)
lista.append("(OwO=)")
print (lista)

#extend(iterable) recibe una secuencia y agrega sus elementos al final
#  de la lista como otra lista, tupla, cadena
print ("Método extend(iterable)")
lista = [1,2,3]
print (lista)
lista.extend(":3")
print (lista)
lista.extend(["(¬_¬ )", "(O_O=)"])
print (lista)
lista.extend(("😅", "😎"))
print (lista)

#remove(valor) recibe un valor y elimina la primera aparición de ese
#  valor en la lista si no existe lanza un error
print ("Método remove(valor)")
lista = [1,2,"UwU",4,5, "UwU"]
print (lista)
lista.remove("UwU")
print (lista)

#pop(i) o pop() recibe un index o índice y elimina el elemento en
#  esa posición Si no se especifica el índice elimina el último elemento
print ("Método pop(i)")
lista = ["OwO",3,"UwU",5]
print (lista)
lista.pop(1)
print (lista)
print ("Método pop()")
lista.pop()
print (lista)

#clear() elimina todos los elementos de la lista dejándola vacía
print ("Método clear()")
lista = ["ewe","OwO","UwU"]
print (lista)
lista.clear()
print (lista)

#metodos de ordenamiento
#sort() ordena los elementos de la lista de menor a mayor
print ("Método sort()")
lista = [3,1,5,2,4]
print (lista)
lista.sort()
print (lista)

#sort(reverse=True) ordena los elementos de la lista de mayor a menor
print ("Método sort()")
lista = [3,1,5,2,4]
print (lista)
lista.sort(reverse=True)
print (lista)

#reverse() invierte el orden de los elementos de la lista
print ("Método reverse()")
lista = [3,1,5,2,4]
print (lista)
lista.reverse()
print (lista)

#Metodos de copia
#Cuando se asigna una lista a otra variable se crea una referencia 
# a la lista original NO se crea una copia de la lista, 
# si se modifica esta se modifica la original
print ("Asignación de lista")
lista = [1,2,3,4,5]
print (lista)
copia = lista
copia[0] = 6
print (copia)
print (lista)

#Para crear una copia de la lista se debe utilizar el método copy()
#  o el slicing [:]
print ("Método copia con slicing")
lista = [1,2,3,4,5]
print (lista)
copia = lista[:]
copia[0] = 6
print (copia)
print (lista)

#copy() devuelve una copia de la lista es equivalente al slicing [:]
print ("Método copy()")
lista = [3,1,5,2,4]
print (lista)
copia = lista.copy()
print (copia)
print (copia == lista)
print(copia is list)

#len() longitud de la lista
print ("Función len()")
lista = [1,True,3.14,"🐍",5]
print (lista)
print (len(lista))

#max() devuelve el valor máximo de la lista o el elemento más grande
#Si la lista contiene cadenas devuelve el valor máximo en orden 
# alfabético
#Si la lista contiene enteros y flotantes devuelve el valor 
# máximo numérico
print ("Función max()")
lista = [1,2,3,4,5]
print (lista)
print (max(lista))
lista = ["a","b","c","d","e"]
print (lista)
print (max(lista))

#min() devuelve el valor mínimo de la lista o el elemento más pequeño
#Si la lista contiene cadenas devuelve el valor mínimo en orden alfabético
#Si la lista contiene enteros y flotantes devuelve el valor mínimo numérico
print ("Función min()")
lista = [1,2,3,4,5]
print (lista)
print (min(lista))
lista = ["a","b","c","d","e"]
print (lista)
print (min(lista))

#sum() devuelve la suma de los elementos de la lista
#Se debe asegurar que los elementos de la lista sean numéricos
print ("Función sum()")
lista = [1,2,3,4,5]
print (lista)
print (sum(lista))

#Comparación de listas
#Podemos consultar si una lista contiene un elemento específico 
# utilizando el operador in, not in
#Si una variable hace referencia a otra variable podemos utilizar 
# el is , is not, para comparar si son la misma lista
print ("Comparación de listas")
lista = [1,2,3,4,5]
print (lista)
print (3 in lista)
print (6 in lista)
print (3 not in lista)
print (6 not in lista)
print ([1,2,3] in lista)

#is - is not
print ("Comparación de listas")
lista1 = [1,2,3,4,5] #memoria1
lista2 = [1,2,3,4,5] #memoria2
lista3 = [1,2]
print (lista1, lista2, lista3)
print (lista1 is lista2) #false
print (lista1 is not lista2) #true
print (lista3 is lista1) #false

#Operadores de comparación
#Podemos comparar listas utilizando los operadores de comparación, 
# estos comparan los elementos de las listas uno a uno
print ("Menor y Menor Igual que")
print ([1,2,3] <= [1,2,4])#true
print ([1,2,3] <= [1,2,2,2])#false
print ([1,2,3] <= [2])#true
print ([1,2,3] < [1,2,3])#false
print ([1,2,3] <= [1,2,3])#true

print ("Mayor y Mayor Igual que")
print ([1,2,3] >= [1,2,4])#false
print ([1,2,3] >= [1,2,2,2])#true
print ([1,2,3] >= [2])#false
print ([1,2,3] > [1,2,3])#false
print ([1,2,3] >= [1,2,3])#true

print ("Igual y Desigual que")
print ([1,2,3] == [1,2,3])#true
print ([1,2,3] == [1,2,4])#false
print ([1,2,3] != [1,2,3])#false
print ([1,2,3] != [1,2,4])#true

#Listas anidadas
#Las listas anidadas son listas que contienen otras listas como 
# elementos
#Se pueden crear listas anidadas de cualquier profundidad#
print ("Listas anidadas")
lista = [1,2,3,[4,5,6]]
print (lista)
print (type(lista))
valor_lista = lista[3]
print (valor_lista)
print (type(valor_lista))
valor = valor_lista[1]
print (valor)
print (type(valor))



















