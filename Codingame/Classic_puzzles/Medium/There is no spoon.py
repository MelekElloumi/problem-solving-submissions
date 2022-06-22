l=[]
w = int(input())
h = int(input())  
for i in range(h):
    l.append(input())

for i in range(h):
    for j in range(w):
        if l[i][j]=='.':
            continue
        print(j,i,end=' ')
        m=1
        for x in range(j+1,w):
            if l[i][x]=='0':
                print(x,i,end=' ')
                m=0
                break
        if m:
            print("-1 -1",end=' ')
        m=1
        for x in range(i+1,h):
            if l[x][j]=='0':
                print(j,x)
                m=0
                break
        if m:
            print("-1 -1") 