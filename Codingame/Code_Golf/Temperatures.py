I=input
print(0if I()<'1'else max((-x*x,x)for x in map(int,I().split()))[1])