l = int(input())
h = int(input())
t = input().upper()
r=[]
for i in range(h):
    r.append(input())
res=[''for j in range(h)]
for i in range(len(t)):
    if t[i].isalpha():
        x=ord(t[i])-65
    else:
        x=26
    for j in range(h):
        res[j]=res[j]+r[j][x*l:x*l+l]
print(*res,sep='\n')
