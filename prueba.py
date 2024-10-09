impares = tuple(i for i in range(1,11) if i % 2 != 0)
print(impares,type(impares))

print ("Ejemplo 20")
for i in range(1, 3):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

while True:
    numero = int(input('ingrese numero: '))
    if numero == 0:
        break
    print(f'Tabla del {numero}')
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')
print('fin')

