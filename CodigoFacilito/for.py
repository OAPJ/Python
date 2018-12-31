lista = [1,2,3,4,5,6,7,8,9,10]

for i in lista:
    pass

nuevo_rango = range(20)
nuevo_rango = range(10,20)
nuevo_rango = range(0,20,2) #donde inicia, donde termina, aumenta en 2 en 2
nuevo_rango = range(0, len(lista)) #len deveulve el tamaño

for i in nuevo_rango:
    print(i)
