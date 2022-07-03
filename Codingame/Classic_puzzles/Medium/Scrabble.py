score=[1,3,3,2,3,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
n = int(input())
scores=[]
for i in range(n):
    w=input()
    scores.append([sum([score[ord(c)-97]for c in w]),w,i])

scores.sort(reverse=True)

letters = input()

result=list(filter(lambda x:len(x[1])==sum([c in letters and letters.count(c)>=x[1].count(c) for c in x[1]]),scores))
final=[]
for i in result:
    if result[0][0]==i[0]:
        final.append(i)
    else:
        break
print(sorted(final,key=lambda x:x[2])[0][1])