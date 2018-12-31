course = 'Curso'
my_string = 'Codigo Facilito!'
#print(course[-1]+" "+course[0]+" "+course[0:4]);
"""Formato"""
result = '{} de {}'.format(course,my_string)
#result = '{a} de {b}'.format(b = course,a = my_string);
result = result.upper() #Toda a mayusulas
result = result.title() #Lo pone como titulo
result = result.lower() #pasa todo a minusculas

"""Busqueda"""
pos = result.find('Codigo')
cont = result.count('c') #Cuenta cuanras veces se repite
new_string = result.replace('c', 'x') #remplasa la primera x por class
new_string = result.split(' ') #lo seciona en partes
print(new_string);
