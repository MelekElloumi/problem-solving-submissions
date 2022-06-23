x=input()[0]
#x,y,a,b=[int(i)for i in input().split()]
if x=='7':
    print("W\n"*30)
elif x=='5':
    print("S\n"*30)
elif x=='0':
    print("SW\n"*17+"W\n"*20)  
else:
    print("SE\n"*14+"E\n"*30)