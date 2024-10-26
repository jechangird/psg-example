#1 funciones sin argumentos ni retornod
print('funciones sin argumentos ni retorno')
def funcion_basica():
    print('funcion basica')

funcion_basica()

#2 crear una funcion para imprimir una funciones sin argumentos ni retornod y
#llamarla dos veces

print('2.lista de numeros pares')
def numeros_pares():
    pares = [i for i in range(1,21) if i % 2 == 0]
    print(pares)

numeros_pares()
numeros_pares()

#ejercicio 1: crear una funcion que imprima un mensaje de bienvenida
print('ejercicio 1')
def mensajes():
   mensaje = {'bienvenidos','hello','quihubo'}
   print (mensaje.pop())

mensajes()

#ejercicio 2 devolver una fruta aleatoria del siguiente conjunto
print('ejercicio 2')
def devolver_fruta():
    frutas = {'🍅','🍌','🍎','🍇','🍉'}
    return frutas.pop()

fruta = devolver_fruta()
print(fruta)

#ejercicio 3:devolver una fruta y un color aleatorio
print('ejercicio 3')
def fruta_color():
    frutas = {'🍅','🍌','🍎','🍇','🍉'}
    colores = {'🔴','🟠','🟡','🟢','🔵'}
    return frutas.pop(),colores.pop()

fruta,color = fruta_color()
print(fruta,color)

#Ejercicio 4, Crear una función que imprima el mensaje de 
# bienvenida de acuerdo al un idioma enviado como argumento, 
# si no existe imprimir un mensaje por defecto
print('ejercicio 4')

def mensaje(idioma):
    mensajes = {"es":"Bienvenido al Python Study Group 🐍",
                "en": "Hello and welcome to the Python Study Group! ✨",
               }
    print(mensajes.get(idioma,'quihubo...'))

mensaje_enviado = mensaje("tu")

#Ejercicio 5, Crear una función que reciba una lista de animales, 
# un entero e imprima una lista con los animales repetidos el número 
# de veces
print('Ejercicio 5')

def repetir(animal,veces):
    lista = [animal*veces for animal in animales]
    print(lista)

animales = ['🐶','🐱','🐭','🐹','🐰']
repetir(animales,5)

#Ejercicio 6, Crear una función que reciba dos enteros y una cadena 
# devolver el resultado de la operación de los números según la cadena 
# puede ser suma, resta, multiplicación o división
print('ejercicio 6')

def operaciones(numero1,numero2,operacion):
    if operacion == '+':
        resultado = numero1 + numero2
    elif operacion == '-':
        resultado = numero1 - numero2
    elif operacion == '*':
        resultado = numero1 * numero2
    elif operacion == '/':
        resultado = numero1 / numero2 
    else:
        resultado = "operacion no permitida"
    return resultado

res = operaciones(10,8,'+')
print(res)

#Ejercicio 7, Crear una juego de piedra papel o tijera, donde reciba dos 
# jugadas por teclado y devuelva las jugadas y el resultado, si ingresa 
# salir terminar el juego

#Ejercicio 8, De la siguiente cadena global convertir en formato título 
# y contar las vocales aeiou con una función
print('Ejercicio 8')
cadena = "python es un lenguaje de programación"
def titulo():
    cadena_titulo = cadena.title()
    vocales = sum([1 for letra in cadena_titulo if letra in "aeiouAEIOU"])
    return cadena_titulo, vocales

resultado = titulo()
print(resultado)

#Ejercicio 9, Crear una función que reciba N objetos y genere una tupla 
# y una lista con los objetos usando *args
print('ejercicio 9')
def objetos(*args):
    tupla = tuple(args)
    lista = list(args)
    print(lista)
    print(tupla)

objetos(1, 1.1, True, "🍎" )   

print ("Ejemplo 10")
print ("1. Definir función")
def datos_persona(**datos):
    mensaje = ""
    for clave, valor in datos.items():
        mensaje += f"{str(clave).title()}: {str(valor).upper()}\n"
    return mensaje
print ("2. Llamar función")
resultado = datos_persona(nombre="Jhon", apellido="Doe", edad=20, boliviano=True)
print (resultado)

#Ejercicio 10, Crea un simulador de lavar platos con una función que 
# reciba los objetos a lavar y el tiempo de lavado de cada objeto devuelva 
# un mensaje con los objetos lavados y el tiempo total de lavado
print('ejercicio 10')

def lavar_platos(**utensilios):
    '''rutina lava platos'''
    mensaje = ''
    tiempo = 0
    for clave, valor in utensilios.items():
        tiempo += tiempo
        mensaje += f"{(clave).title()}: {(valor)}\n"
    print(f"tiempo total : {tiempo}")
    return mensaje


resultado = lavar_platos(plato=5, vaso=3, tenedor=1, cuchara=0.5)

print(resultado)
print(lavar_platos.__doc__)

#Ejercicio 11, Crear funciones de limpieza de una cadena para obtener 
# las letras y convertir todo en mayúsculas crea funciones de limpieza y 
# función una principal
print('ejercicio 11 funciones anidadas')

cadena = "Python es un lenguaje de programación 🎈. Feliz Aprendizaje el 2024"
def limpiar_letras(cadena):
    """
    Elimina los números de una cadena y espacios
    """
    return "".join([letra for letra in cadena if letra.isalpha()])
def limpiar_mayusculas(cadena):
    """
    Convierte una cadena en mayúsculas
    """
    return cadena.upper()

def limpiar(cadena):
    cadena = limpiar_letras(cadena)
    cadena = limpiar_mayusculas(cadena)
    return cadena

cadena = "Python es un lenguaje de programación 🎈. Feliz Aprendizaje el 2024"
def limpiar_letras(cadena):
    """
    Elimina los números de una cadena y espacios
    """
    return "".join([letra for letra in cadena if letra.isalpha()])
def limpiar_mayusculas(cadena):
    """
    Convierte una cadena en mayúsculas
    """
    return cadena.upper()

def limpiar(cadena):
    cadena = limpiar_letras(cadena)
    cadena = limpiar_mayusculas(cadena)
    return cadena


def limpiar_letras(cadena):
    """
    Elimina los números de una cadena y espacios
    """
    return "".join([letra for letra in cadena if letra.isalpha()])
def limpiar_mayusculas(cadena):
    """
    Convierte una cadena en mayúsculas
    """
    return cadena.upper()

def limpiar(cadena):
    cadena = limpiar_letras(cadena)
    cadena = limpiar_mayusculas(cadena)
    return cadena

cadena = "Python es un lenguaje de programación 🎈. Feliz Aprendizaje el 2024"
resultado = limpiar(cadena)
print (cadena)
print (resultado)

print ("Ejemplo 12 funciones recursivas")
print ("1. Definir función")
def numero_par(numero):
    if numero == 0:
        return 0
    else:
        return numero_par(numero-1) + 2
 
print ("2. Llamar función")
resultado = numero_par(10)
print (resultado)

print('ejercicio de recursividad, factorial')
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero*factorial(numero-1)

resultado = factorial(5)
print (resultado)

print('funciones lambda')
print ("Ejemplo 13")
cuadrado = lambda numero: numero**2
resultado = cuadrado(5)
print (resultado)
resultado = cuadrado(10)
print (resultado)




