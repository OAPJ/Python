if __name__ == '__main__':

    clase = []
    mas_bajo = 100
    segundo_mas_bajo2 = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista2 = [name,score]
        clase.append(lista2)
        if _ == 0:
            mas_bajo = lista2[1]
            print(str(mas_bajo)+" "+str(segundo_mas_bajo2))
        elif lista2[1] < mas_bajo:
            if mas_bajo != segundo_mas_bajo2 :
                print(str(mas_bajo)+" "+str(segundo_mas_bajo2))
                segundo_mas_bajo2 = mas_bajo
                lista3 = [lista2]
            elif mas_bajo == segundo_mas_bajo2:
                print(str(mas_bajo)+" "+str(segundo_mas_bajo2))
                lista3.append(lista2)
            mas_bajo = lista2[1]


print(lista3)
