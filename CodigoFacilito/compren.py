
lista = [i for i in range(0,101)]
lista = [i for i in range(0,101) if i%2 == 0]
tupla = tuple( (i for i in range(0,101) if i%2 == 0))
diccionario = {i:valor for i, valor in enumerate(lista) if i<10}
print(lista)
print()
print(tupla)
print()
print(diccionario)
