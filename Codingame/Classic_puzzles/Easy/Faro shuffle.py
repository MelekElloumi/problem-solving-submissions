n = int(input())
l = input().split()

for _ in range(n):
    l1=l[:len(l)//2+len(l)%2]
    l2=l[len(l)//2+len(l)%2:]
    nl=[]
    for i in range(len(l2)):
        nl.append(l1[i])
        nl.append(l2[i])
    if len(l)%2:
        nl.append(l1[-1])
    l=nl[:]

print(*l)
