'''Dos mochileros se encuentran en el Salar de Uyuni y se ponen a comparar 
la cantidad de lugares que han visitado
Cada uno quiere saber en que parte del mundo ha estado el otro que el no 
haya visitado

mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
"Peru", "Chile", "Colombia", "Bolivia"}

mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
"Argentina","Brasil","Panama","Bolivia"}

Ahora quieren saber en que ciudades han estado ambos mochileros'''

mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
"Peru", "Chile", "Colombia", "Bolivia"}

mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
"Argentina","Brasil","Panama","Bolivia"}

faltante_a = mochilero_b.difference(mochilero_a)
print(faltante_a)

faltante_b = mochilero_a.difference(mochilero_b)
print(faltante_b)

ambos = mochilero_a.intersection(mochilero_b)
print(ambos)