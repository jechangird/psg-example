#De la palabra "Fluorescente" mostrar solo los caracteres con índice par
palabra = 'fluorescente'
pares = []
for i in palabra:
    a = palabra.index(i)
    if a%2 == 0:
        pares.append(i)
        print(i)
    
print(pares)

   
