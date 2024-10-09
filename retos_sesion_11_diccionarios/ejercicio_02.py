'''Crea un diccionario para almacenar información de comidas de animales 
por ejemplo
comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}
'''

comidas = {"carne"  : {"animales": ["león", "tigre"]}, 
           "frutas" : {"animales": ["mono", "elefante"]}}

'''1.Añade al diccionario de comidas 4 alimentos más usando 
update(clave=valor)'''
comidas.update({'vegetales' : {'animales' : ['danta','morrocoy']}}),
comidas.update({'insectos'  : {'animales' : ['arana','oso hormiguero']}})
print(comidas)

'''2. Existe en el diccionario de comidas la comida 'carne'?'''
existe_carne  = 'carne' in comidas
print(existe_carne)

'''3. Elimina la comida 'frutas' del diccionario de comidas'''
del comidas['frutas']
print(comidas)