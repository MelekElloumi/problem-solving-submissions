I,P=input,print
if I()=='0':P(0)
l=list(map(int,I().split()))
t=min(l,key=abs)
P(-t)if-t in l and t<0 else P(t)