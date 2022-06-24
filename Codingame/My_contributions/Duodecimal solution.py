s="0123456789AB"

def decimal(x):
    res=0
    for i in range(len(x)):
        res+= 12**i * s.index(x[-i-1])
    return res

def duodecimal(x):
    res='' if x!=0 else '0'
    while x>0:
        res=s[x%12]+res
        x//=12
    return res

n = input()
m = int(input())
print(decimal(n[2:]))
print("0w"+duodecimal(m))