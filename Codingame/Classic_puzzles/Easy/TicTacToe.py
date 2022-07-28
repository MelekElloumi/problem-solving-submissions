l=[]
for i in range(3):
    line = input()
    l.append(list(line))

for i in range(3):
    if l[i].count('O')==2 and '.' in l[i]:
        l[i][l[i].index('.')]='O'
        print(*[''.join(c) for c in l],sep='\n')
        exit(0)

for i in range(3):
    line=[c[i] for c in l]
    if line.count('O')==2 and '.' in line:
        l[line.index('.')][i]='O'
        print(*[''.join(c) for c in l],sep='\n')
        exit(0)

d1=[l[i][i] for i in range(3)]
d2=[l[i][2-i] for i in range(3)]
if d1.count('O')==2 and '.' in d1:
        l[d1.index('.')][d1.index('.')]='O'
        print(*[''.join(c) for c in l],sep='\n')
        exit(0)
if d2.count('O')==2 and '.' in d2:
        l[d2.index('.')][d2.index('.')]='O'
        print(*[''.join(c) for c in l],sep='\n')
        exit(0)
print("false")