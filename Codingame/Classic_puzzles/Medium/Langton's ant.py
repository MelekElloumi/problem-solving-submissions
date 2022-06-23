import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
left={}
left["N"]="W"
left["W"]="S"
left["S"]="E"
left["E"]="N"
right={}
right["N"]="E"
right["W"]="N"
right["S"]="W"
right["E"]="S"
w, h = [int(i) for i in input().split()]
x, y = [int(i) for i in input().split()]
d = input()
t = int(input())
g=[]
for i in range(h):
    g.append(input())
for _ in range(t):
    if g[y][x]=='.':
        d=left[d]
        g[y]=g[y][:x]+'#'+g[y][x+1:]
    else:
        d=right[d]
        g[y]=g[y][:x]+'.'+g[y][x+1:]
    if d=='N':
        y=y-1
    if d=='S':
        y=y+1
    if d=='E':
        x=x+1
    if d=='W':
        x=x-1
print(*g,sep="\n")
