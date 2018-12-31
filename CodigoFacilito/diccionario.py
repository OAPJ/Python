diccinario = {'a':True, 5:"esto es un string", 'a':100, 'a':False}

diccinario['c'] = 'nuevo string'
diccinario['a'] = False

valor = diccinario.get('z', False) #key, lo que queremos que muestre si no encuentra la key

#sdel diccinario[] #eliminar la key

print(diccinario)
print(valor)

llaves = list(diccinario.keys()) #transforma a lista
valores = tuple(diccinario.values())
#print(llaves)
#print(valores)

diccinario2 = {'z':23, 'w':88}

diccinario.update(diccinario2)
print(diccinario)
