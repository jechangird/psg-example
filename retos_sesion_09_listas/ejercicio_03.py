print('Crear una lista de personas con 10 nombres de personas')
nombres = ['maria','jose','ana','juana','elvira','daniel','ernesto','joel','isidro','ale']
print(nombres)

print('1.Obtener una sub lista de 2 a 7')
nombres1 = nombres[2:7]
print(nombres1)

print('2.Buscar si existe el nombre "Jhon" en la lista original')
valor = 'jhon'
print (valor, nombres.count(valor))

print('3. Ordenar la sub lista alfabéticamente')
nombres1.sort()
print(nombres1)

print('#4.Ordenar la lista original alfabéticamente de forma descendente')
nombres.sort(reverse=True)
print(nombres)






