import sys
import math
from collections import defaultdict
# Made by Tanvir

word_count = int(input())  # Number of words in the word set
words=[]
letter_count=defaultdict(int)
for word in input().split():
    # word: Word in the word set
    for c in word.lower():
        letter_count[c]+=1
letters = sorted([(value,key)for key,value in letter_count.items()],reverse=True)
#l="etaoinsrhdlucmfywgpbvkxqjz"
#letters=[(0,x)for x in l]
answer=[""]*6
a=-1
# game loop
while True:
    for i,s in enumerate(input().split()):
        state = int(s)
        if state==3:
            answer[i]=letters[a][1]
        
    a+=1
    if a==25:
        answer = [letters[a][1] if x == "" else x for x in answer]
    if "" not in answer:
        print("".join(answer))
    else:
        print(letters[a][1]*6)