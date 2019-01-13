def binary(n):
    binary = ""
    while n!=0:
        binary = str(n%2)+binary
        n = int(n/2)
    return binary

def octal(n):
    octal = ""
    while n>0:
        octal = str(n%8)+octal
        n = int(n/8)
    return octal

def f(x):
    if x == 10:
        return "A"
    elif x == 11:
        return "B"
    elif x == 12:
        return "C"
    elif x == 13:
        return "D"
    elif x == 14:
        return "E"
    else:
        return "F"

def hexadecimal(n):
    hexa = ""
    while n>0:
        aux = n%16
        if(aux > 9 and aux < 16):
            hexa = f(aux) + hexa
        else:
            hexa = str(aux) + hexa
        n = int(n/16)
    return hexa

def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1,number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, octal(i), hexadecimal(i), binary(i), width=width))
        #print(str(i)+" "+octal(i)+" "+hexadecimal(i)+" "+binary(i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
