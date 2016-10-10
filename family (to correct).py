# for trying
from collections import defaultdict
d = {}
m = set()
s = defaultdict(list)
s2 = defaultdict(list)
dict = defaultdict(list)
for i in range(int(input()) - 1):
    child, parent = input().split()
    s[parent].append(child)
    m.add(child)
i = - 2
j = -1
import copy
s1 = copy.deepcopy(s)
#print(s1)
#print(s1)
for m in range(len(s)):
    for key, value in s.items():
        if key not in [v for value in s1.values() for v in value] and key not in s2.keys() and key not in [v for value in s2.values() for v in value]: # or key not in m:
            i += 2
            j += 2
            if i == 0:
                print(key, i)
            print(s[key], j) # ЛУЧШЕ привязать s[key] к i
            del s1[key] # удалили пару (Peter_I:['Alexei', 'Anna', 'Elizabeth'])
                #print(s1)
            for v in s[key]:
                s2[key].append(v) # # добавили в s2 пару (Peter_I:['Alexei', 'Anna', 'Elizabeth'])
            #print(s[key], j)
                if v in s1.keys():
                    print(s1[v], i + 2)
                    del (s1[v])
                    s2[v].append(s[v])
print(s1)
print(s2)
