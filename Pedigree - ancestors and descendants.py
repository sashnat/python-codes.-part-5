def f(d, a1, a2):
    s = a1
    while s in d:
        s = d[s]
        if s == a2:
            return 2
    s = a2      
    while s in d:
        s = d[s]
        if s == a1:
            return 1 
    return 0
 
N = int(input())
d = {}
 
for i in range(N-1):
    a1, a2 = input().split()
    d[a1] = a2
    
N = int(input())
for i in range(N):
    a1, a2 = input().split()
    print(f(d, a1, a2), end=" ")
