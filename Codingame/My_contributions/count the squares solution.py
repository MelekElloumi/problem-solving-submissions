n,m=[int(x) for x in input().split()]
n,m=min(n,m),max(n,m)
count=n*m
for i in range(2,n+1):
    count+=(n-i+1)*(m-i+1)
print(count)