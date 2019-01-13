def mutate_string(string, position, character):
    result = ""
    for i in range(len(string)):
        if position == i:
            result+=character
        else:
            result+=string[i]
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
