'''Gestión de hábitats en peligro: Crea un diccionario que asocie 
especies animales en peligro de extinción con información sobre sus 
hábitats amenazados, lo que permite priorizar la protección de áreas 
críticas para la supervivencia de estas especies
habitats = {"polo norte" : {"especies": {"oso polar", "morsa", "ballena"}}, "amazonas" : {"especies": {"tigre", "mono", "guacamayo"}}}'''

habitats = {"polo norte" : {"especies": {"oso polar", "morsa", "ballena"}},
            "amazonas" : {"especies": {"tigre", "mono", "guacamayo"}}}

print('1. ',habitats)

#Añade al diccionario de habitats 2 habitats más usando update()
habitats.update({'desierto': {'especies' : {'serpiente','bachaco'}}})
habitats.update({'llano': {'especies' : {'venado','chiguire'}}})

print('2. ',habitats)

#Existe en el diccionario de habitats el habitat 'amazonas'?
existe_amazonas = 'amazonas' in habitats
print('3. ',existe_amazonas)

#Añade al diccionario de amazonas la especie 'anaconda'
habitats.update({'amazonas': {'especies' : {"tigre", "mono", "guacamayo",'anaconda',}}})
print('4. ',habitats)