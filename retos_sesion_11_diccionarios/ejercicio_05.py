'''Eres NOE y tienes que guardar dos animales de cada especie en un arca, 
crea un diccionario con las especies'''

arca = {"perro" : 2, 
        "gato" : 2, 
        "tigre" : 2, 
        "mono" : 2, 
        "unicornio" : 0, 
        "jirafa" : 1}
print(arca)

#Añade al arca 2 especies más usando update()
arca.update({'chiguire': 2})
arca.update({'babo': 2})
print('1. ',arca)

#Toma lista de los animales en el arca iterando el diccionario
#notas = {'juan':[2,4,6,2],'pedro':[4,6,2,1],'jose':[10,4,0,3]}
for x,y in arca.items():
    print(x,y)

#Existe en el arca la especie 'dragon'?
existe_dragon = 'dragon' in arca
print('3. ',existe_dragon)

#Elimina la especie 'unicornio' del arca
del arca['unicornio']
print('4. ',arca)

#Modifica el valor de la especie 'jirafa' por 2
arca.update({'jirafa' : 2})
print('5. ',arca)

#Vacía el arca después del diluvio
arca.clear()
print('5. ',arca)
