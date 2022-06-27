import numpy as np

n = int(input())
a=[]
b=[]
for i in range(n):
    num, t = [int(j) for j in input().split()]
    a.append(num)
    b.append(t)
nums=np.array(a)
comp=np.array(b)
#print('1',comp.std(),comp.mean(),comp.mean()*0.2,sep=' | ')
if (comp.std()<comp.mean()*0.1):
    print("O(1)")
else:
    comp2=comp/np.log(nums)
    #print('log',comp2.std(),comp2.mean(),comp2.mean()*0.2,sep=' | ')
    if (comp2.std()<comp2.mean()*0.3):
        print("O(log n)")
    else:
        comp2=comp2/nums
        #print('nlog',comp2.std(),comp2.mean(),comp2.mean()*0.2,sep=' | ')
        if (comp2.std()<comp2.mean()*0.2):
            print("O(n log n)")
        else:
            comp=comp/nums
            #print('n',comp.std(),comp.mean(),comp.mean()*0.2,sep=' | ')
            if (comp.std()<comp.mean()*0.2):
                print("O(n)")
            else:
                comp2=comp2/nums
                #print('n2log',comp2.std(),comp2.mean(),comp2.mean()*0.2,sep=' | ')
                if (comp2.std()<comp2.mean()*0.2):
                    print("O(n^2 log n)")
                else:
                    comp=comp/nums
                    #print('n2',comp.std(),comp.mean(),comp.mean()*0.2,sep=' | ')
                    if (comp.std()<comp.mean()*0.3):
                        print("O(n^2)")
                    else:
                        comp=comp/nums
                        #print('n3',comp.std(),comp.mean(),comp.mean()*0.2,sep=' | ')
                        if (comp.std()<comp.mean()*3):
                            print("O(2^n)")
                        else:
                            print("O(n^3)")