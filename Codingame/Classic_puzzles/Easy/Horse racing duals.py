n = int(input())
l=[]
for i in range(n):
    pi = int(input())
    l+=[pi]
l.sort()
m=abs(l[1]-l[0])
for i in range(2,n):
    m=min(m,abs(l[i]-l[i-1]))
print(m)
