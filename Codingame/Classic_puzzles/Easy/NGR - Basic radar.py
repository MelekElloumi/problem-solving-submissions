from datetime import datetime

d={}
l=[]
n = int(input())
for i in range(n):
    inputs = input().split()
    plate = inputs[0]
    radarname = inputs[1]
    timestamp = int(inputs[2])
    tt=datetime.fromtimestamp(int(timestamp/1000))
    
    if plate in d:
        tt2=d[plate]
        delta=tt-tt2
        sp=int(13*3600/delta.total_seconds())
        if sp>130:
            l.append((plate,sp))
    else:
        d[plate]=tt
    
l.sort(key=lambda x:x[0])
for p,s in l:
    print(p,s)