def intersect(x1,y1,r1,x2,y2,r2):
    distSq = (x1 - x2)**2+ (y1 - y2)**2
    radSumSq = (r1 + r2)**2
    if (distSq <= radSumSq):
        return True
    else:
        return False

n, index = [int(i) for i in input().split()]
apples=[]
for i in range(n):
    x,y,z,r= [int(j) for j in input().split()]
    apples.append([i,x,y,z,r,0])


falling=[apples[index]]
apples[index][5]=1
fell=1
while len(falling)!=0:
    f=falling[0]
    for a in apples:
        if a[5]==0:
            if intersect(f[1],f[2],f[4],a[1],a[2],a[4]) and f[3]>=a[3]:
                fell+=1
                a[5]=1
                falling.append(a)
    falling.pop(0)


print(len(apples)-fell)