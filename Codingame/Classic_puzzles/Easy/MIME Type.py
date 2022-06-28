n = int(input()) 
q = int(input())  
l={}
for i in range(n):
    ext, mt = input().split()
    l[ext.lower()]=mt
for i in range(q):
    g = input()
    if '.' not in g:
        print("UNKNOWN")
        continue
    f=g.split('.')
    print(l[f[-1].lower()]) if f[-1].lower() in l else print("UNKNOWN")