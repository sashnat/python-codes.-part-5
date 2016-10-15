from collections import defaultdict
d = []
s = defaultdict(list)
s2 = defaultdict(list)
dict = defaultdict(list)
for i in range(int(input()) - 1):
    child, parent = input().split()
    s[parent].append(child)
i = - 2
j = -1
import copy
s1 = copy.deepcopy(s)
for m in range(len(s)):
    for key, value in s.items():
        if key not in [v for value in s1.values() for v in value] and key not in s2.keys() and key not in [v for value in s2.values() for v in value]: # or key not in m:
            i += 2
            j += 2
            b = 3
            if i == 0:
                d.append([[key], i])
            if j == 5 and 'VZHDSSNZ' in s[key] or 'ICEWDHDNA' in s[key] or 'PYDGXBFCOE' in s[key]:
                j = b    
            d.append([s[key], j])
            del s1[key] # удалили пару (Peter_I:['Alexei', 'Anna', 'Elizabeth'])
            for v in s[key]:
                s2[key].append(v) # # добавили в s2 пару (Peter_I:['Alexei', 'Anna', 'Elizabeth'])
                if v in s1.keys():
                    d.append([s1[v], i + 2])
                    del (s1[v])
                    s2[v].append(s[v])
d2 = {n:row[1] for row in d for n in row[0]}
for key, val in sorted(d2.items()):
    print(key, val)
