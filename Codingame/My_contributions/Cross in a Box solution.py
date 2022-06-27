n = int(input())
m=2*n+1
l=["#"*(m+2)]
for i in range(n):
    l.append('#'+' '*i+'X'+' '*(m-2-2*i)+'X'+' '*i+'#')
d=l+['#'+' '*n+'X'+' '*n+'#']+l[::-1]
print(*d,sep='\n')