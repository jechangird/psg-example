'''Anita y Pepito llevan saliendo juntos por 4 semanas, cada vez que salen 
van a comer a una plaza de comidas. Ambos quieren saber que tan compatibles
son viendo cuantos platos de comida tienen en común. A continuación tienes 
los platos de comida que ambos han ido pidiendo a los largo de sus citas:
Anita: Sushi, Pizza, Tacos, Hamburguesa, Pasta, Alitas
Pepito: Pizza, Tacos, Ensalada, Pasta, Helado, Milanesa
Si la cantidad platos de comida que tienen en comunes mayor a 50% entonces 
ambos seguirán saliendo'''

conjunto_anita = {'Sushi', 'Pizza', 'Tacos', 'Hamburguesa', 'Pasta', 'Alitas'}
conjunto_pepito = {'Pizza', 'Tacos', 'Ensalada', 'Pasta', 'Helado', 'Milanesa'}

interseccion = conjunto_anita.intersection(conjunto_pepito)
cantidad_platos = len(conjunto_anita)
platos_comunes = len(interseccion)
porcentaje_platos_comunes = (platos_comunes * 100) / cantidad_platos

print(cantidad_platos)
print(platos_comunes)
print(interseccion)
print(porcentaje_platos_comunes)

if porcentaje_platos_comunes > 50:
   print('Anita y Pepito continuaran saliendo juntos')
else:
   print('Anita y Pepito NO continuaran saliendo juntos')



