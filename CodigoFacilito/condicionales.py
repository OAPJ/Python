fruta = 'kiwi'

if fruta == 'kiwi':
    print("El valor es kiwi")
elif fruta == 'manzana':
    print("Es una manzana")
elif fruta == 'manzana2':
    pass #si no sabemos que poner y no marque error
else:
    print("No son iguales")

mensaje = 'El valor es kiwi' if fruta == 'kiwis' else False
print(mensaje)
