w = int(input())
h = int(input())
g=[]
for i in range(h):
    g.append(list(input()))

for i in range(h):
    for j in range(w):
        x=0
        if g[i][j]=='.':
            for xi in range(max(0,i-1),min(h-1,i+1)+1):
                for xj in range(max(0,j-1),min(w-1,j+1)+1):
                    if g[xi][xj]=='x':
                        x+=1
            if x!=0:
                g[i][j]=str(x)
for i in g:
    print(''.join(i).replace('x','.'))
