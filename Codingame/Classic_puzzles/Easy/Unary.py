m = input()
s=''
for i in m:
    s+='{0:07b}'.format(ord(i))
x=s[0]
i=1
d=1
while i<len(s):
    if s[i]==x:
        d+=1
    else:
        print("0"+"0"*(1-int(x))+" "+"0"*d,end=' ')
        x=s[i]
        d=1
    i+=1

print("0"+"0"*(1-int(x))+" "+"0"*d,end='')