d = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    d[child] = parent
def f(x, d):
    list = [x]
    while True:
        try:
            x = d[x]
            list.append(x)
        except KeyError:
            break
    #print(list)
    return list
    
m = int(input())
for i in range(m):
    a1, a2 = input().split()
    for a in f(a2, d):
        if a in f(a1, d):
            print(a)
            break
