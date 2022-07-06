import math
n = int(input())
l=[]
mi=math.inf
ma=-math.inf
for i in range(n):
    x, y = [int(j) for j in input().split()]
    mi=min(mi,x)
    ma=max(ma,x)
    l.append([y,x])
l.sort()
if n%2==0:
    fy=(l[n//2-1][0]+l[n//2][0])/2
else:
    fy=l[n//2][0]

res=ma-mi+sum([abs(y[0]-fy) for y in l])
print(int(res))