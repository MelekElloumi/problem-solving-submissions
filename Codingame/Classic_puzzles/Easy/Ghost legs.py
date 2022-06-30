w, h = [int(i) for i in input().split()]
l=[]
for i in range(h):
    l.append(input())
st={}
for i,x in enumerate(l[0].split()):
    st[i]=x
n=len(st)
en={}
for i,x in enumerate(l[-1].split()):
    en[i]=x
for ia,a in enumerate(st):
    lane=ia
    for d in range(1,h-1):
        if lane==0:
            if l[d][lane*3+1]=='-':
                lane+=1
        elif lane==n-1:
            if l[d][lane*3-1]=='-':
                lane-=1
        else:
            if l[d][lane*3+1]=='-':
                lane+=1
            elif l[d][lane*3-1]=='-':
                lane-=1
    b=en[lane]
    print(st[a],b,sep='')
