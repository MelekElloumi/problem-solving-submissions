w = int(input())
h = int(input())

m=[[0]*(w+2)]
for i in range(h):
    m.append([0]+list(map(int,input().split()))+[0])
m.append([0]*(w+2))

for i in range(1,h+1):
    for j in range(1,w+1):
        if m[i][j]==1:
            continue

        if i not in [1,h] and j not in [1,w]:
            c=8
        elif i in [1,h] and j in [1,w]:
            c=3
        else:
            c=5
        
        x=m[i-1][j-1]
        x+=m[i-1][j]
        x+=m[i-1][j+1]
        x+=m[i][j-1]
        x+=m[i][j+1]
        x+=m[i+1][j-1]
        x+=m[i+1][j]
        x+=m[i+1][j+1]

        if x==c:
            print(j-1,i-1)
            exit(0)