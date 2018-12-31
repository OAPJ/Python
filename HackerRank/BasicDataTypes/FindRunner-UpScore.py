if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
f = arr[0]
p = -100000
for i in arr:
    if i>f:
        p=f
        f=i;
    elif i<f and i>p:
        p=i
print(p)
