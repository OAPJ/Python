if __name__ == '__main__':

    clase = []
    mas_bajo = 100
    segundo_mas_bajo2 = 99
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista2 = [name,score]
        clase.append(lista2)
        if score < mas_bajo:
            mas_bajo = score

    lista3 = []
    contador = 0;
    for i in range(len(clase)):
        if clase[i][1] > mas_bajo and clase[i][1] == segundo_mas_bajo2:
            lista3.insert(contador,clase[i][0])
            contador+=1
        elif clase[i][1] > mas_bajo and clase[i][1] < segundo_mas_bajo2:
            segundo_mas_bajo2 = clase[i][1]
            lista3 = []
            lista3.insert(0,clase[i][0])
            contador+=1

    lista3.sort()
    for i in range(len(lista3)):
        print(lista3[i])
