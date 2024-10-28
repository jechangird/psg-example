from ast import While


print ("Inicio Ejemplo 1 try except simple")
try:
    x = 1 / 0
    print (x)
except Exception as e:
    print("💀 Error:", e, type(e))
print ("Fin Ejemplo 1")

#Ejercicio 1, Crear un programa que solicite dos números y realice la 
# división de ambos números Si hay un error mostrar un mensaje de error 
# El programa se detiene si se ingresa "salir"
print('ejercicio 1')
while True:
    try:
        numero1 = (input('ingrese dividendo: '))
        
        if numero1 == 'salir':
            break
        numero2 = (input('ingrese divisor: '))
        if numero2 == 'salir':
            break

        numero1 = int(numero1)
        numero2 = int(numero2)
        division = numero1 / numero2
        print('la division es ',division)
    except Exception as x:
        print('Error :', x, type(x))

    #Ejercicio 2, Crear un programa que solicite dos números y mediante 
    #una función devuelva la división de ambosSi hay un error mostrar
    # un mensaje de error. El programa se detiene si se ingresa "salir"
    # Añadir un bloque else que muestre el resultado de la función
print('ejercicio 2')
def division(numero1,numero2):
    division = numero1 / numero2

while True:
    try:
        numero1 = input('ingrese el primer numero ')
        if numero1 == 'salir':
            break
        numero2 = input('ingrese el segundo numero ')
        if numero2 == 'salir':
            break
        numero1 = float(numero1)
        numero2 = float(numero2)
        resultado = numero1 / numero2
        
    except ZeroDivisionError as x:
        print('Error :', x, type(x))
    except TypeError as x:
        print('Error :', x, type(x))
    except Exception as x:
        print('Error :', x, type(x))
    else:
        print('Resultado: ',resultado)

#Ejercicio 3, Escriba un programa que solicite un número por teclado y 
# se almacene en una listaSi es 0 se genera una excepción. Si la 
# ejecución es correcta muestra "🎉Agregado"
#Termina la ejecución sólo con la palabra "salir" utilizar la excepción 
# KeyboardInterrupt
#Finalmente imprima siempre la suma de los números y la lista

print('ejercicio 3')
numeros = []
while True:
    try:
        num = input("Ingrese un número: ")
        if num == "salir":
            break
        num = float(num)
        if num == 0:
            raise Exception("No se puede agregar el número 0")
        numeros.append(num)
    except KeyboardInterrupt as e:
        print('🚫 Para salir escriba "salir"')
    except Exception as e:
        print("💀 Error:", e)
    else:
        print("🎉 Número agregado")
    finally:
        print("Suma:", sum(numeros))


#Ejemplo 8, Tienes un frutero, saca las frutas mientras no sea un 
# gusano y genera una excepción
print("Inicio Ejemplo 8")
class GusanoError(Exception):
    pass
 
frutero = ['🍎', '🍌', '🍐', '🐛', '🍇']
for fruta in frutero:
    try:
        if fruta == '🐛':
            raise GusanoError("😱 Ewww!")
        print(fruta)
    except GusanoError as e:
        print("🐛 Error:", e)
    except Exception as e:
        print("💀 Error:", e)
print("Fin Ejemplo 8")

'''Ejercicio 4, Crear un programa que solicite palabras por teclado y 
almacene en una lista
Si se inserta caracteres no alfabéticos se genera una excepción 
personalizada y no se almacena
Si se ingresa "salir" se termina la ejecución
Mostrar el mensaje "🎉 Palabra agregada" si no hay errores
Finalmente imprimir la lista de palabras'''




        




