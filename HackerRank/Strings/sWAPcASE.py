def swap_case(s):
    respuesta = ""
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <=122:
            respuesta+=s[i].upper()
        elif ord(s[i]) >= 65 and ord(s[i]) <=90:
            respuesta+=s[i].lower()
        else:
            respuesta+=s[i]
    return respuesta

if __name__ == '__main__':
    S = input()
    print(swap_case(S))
