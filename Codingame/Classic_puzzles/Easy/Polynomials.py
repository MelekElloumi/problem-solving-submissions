import sys
import math

def f(a,b,c,x):
    return a*x**2+b*x+c

a, b, c = [float(i) for i in input().split()]

l=[]
if a==0 and b==0:
    if c==0:
        print('(0,0)')
    else:
        print(f'(0,{round(c,2)})')
    exit(0)
l+=[[0,f(a,b,c,0)]]
if a==0:
    l+=[[-c/b,0]]
else:      
    d=b**2-4*a*c
    if d<0:
        pass
    elif d>0:
        l+=[[(-b+math.sqrt(d))/(2*a),0]]
        l+=[[(-b-math.sqrt(d))/(2*a),0]]
    else:
        l+=[[-b/(2*a),0]]

l.sort()
for x in l:
    x[0]=round(x[0],2)
    if x[0]%1==0:
        x[0]=int(x[0])
    x[1]=round(x[1],2)
    if x[1]%1==0:
        x[1]=int(x[1])
print(*['('+str(i[0])+','+str(i[1])+')' for i in l],sep=',')
