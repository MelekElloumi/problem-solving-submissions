def nex(x):
    return x+sum([int(i)for i in str(x)])

x= int(input())
y= int(input())

while x!=y:
    if x<y:
        x=nex(x)
    elif x>y:
        y=nex(y)

if x==y:
    print(x)
