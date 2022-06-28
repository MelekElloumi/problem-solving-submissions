import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

ax = float(input().replace(',','.'))
ay = float(input().replace(',','.'))
n = int(input())
dm=math.inf
di=''
for i in range(n):
    f = input().split(';')
    bx,by=float(f[4].replace(',','.')),float(f[5].replace(',','.'))
    x=(bx-ax)*math.cos((ay+by)/2)
    y=(by-ay)
    d=math.sqrt(x**2+y**2)*6371
    dm=min(dm,d)
    if dm==d:
        di=f[1]
print(di)
