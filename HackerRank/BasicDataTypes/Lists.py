if __name__ == '__main__':
    N = int(input())

    elements = []
    posicion = ""
    dato = ""
    for i in range(N):
        commands = input()
        longitud = len(commands)
        if commands[0:6] == "insert" :
            if(commands[8] == " "):
                posicion = commands[7]
                dato = commands[9:longitud+1]
            elif commands[9] == " ":
                posicion = commands[7:8]
                dato = commands[10:longitud+1]
            elements.insert(int(posicion),int(dato))
        elif commands == "print":
            print(elements)
        elif commands[0:6] == "remove":
            elements.remove(int(commands[7:longitud+1]))
        elif commands[0:6] == "append":
            elements.append(int(commands[7:longitud+1]))
        elif commands == "sort":
            elements.sort()
        elif commands == "pop":
            elements.pop()
        else:
            elements.reverse()
