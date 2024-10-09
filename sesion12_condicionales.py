print ("Ejemplo 11")
animales = ['🐶','🐱','🐰','🐭']
for i, animal in enumerate(animales):
    print(i, animal,animales[i])

'''Ejercicio 2, imprimir la cantidad de veces los elementos 
de la cadena '⚽🏀🏐🎱' de acuerdo a su posición más 1'''


cadena = '⚽🏀🏐🎱'
print(cadena)
for i, cadena in enumerate(cadena):
    print(cadena*(i+1))

#imprimir numeros <=5
numero = 0
while numero <= 5:
    print(numero)
    numero += 1

'''Ejemplo 13, sumar los números mientras no se ingrese por teclado 
el número 0

suma = 0
numero = int(input('ingrese numero :'))
while numero != 0:
    suma = suma + numero
    numero = int(input('ingrese numero :'))

print(suma)'''

'''Ejemplo 14, De la siguiente lista de frutas imprimir los elementos hasta que se encuentre 
un gusano 🐛 con for'''

frutas = ['🍎','🍌','🍇','🍉','🍊','🐛','🍋','🍍']
for fruta in frutas:
    if fruta == '🐛':
        break
    print(fruta, end = '')
print('fin')

#lo mismo pero con while
print(frutas)
i = ""
while i != '🐛':
    i = frutas.pop(0)
    print(i, end = '')

print('fin')

#ciclos infinitos
print('ciclios infinitos')
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 10:
       break

'''Ejemplo 16, Crear un ciclo infinito que pida una cadena de texto la 
ponga en mayúsculas y la imprima hasta que se ingrese la palabra salir'''

while True:
    palabra = input('Ingrese una palabra :')
    if palabra == 'salir':
       break

    print(palabra.upper())
print('fin')








