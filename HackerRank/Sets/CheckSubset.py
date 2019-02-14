for i in range(int(input())):
    na, a = int(input()), set(map(int,input().split()))
    nb, b = int(input()), set(map(int,input().split()))
    c = 0
    if(len(a) > len(b)):
        print("False")
        c = 1
    elif len(a.union(b)) == len(a):
        print("True")
        c = 1
    elif len(b.union(a)) == len(b):
        print("True")
        c = 1
    if c == 0:
        print("False")
