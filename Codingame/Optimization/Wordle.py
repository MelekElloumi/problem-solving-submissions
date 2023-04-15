import sys
import math


word_count = int(input())  # Number of words in the word set
words=[]
for word in input().split():
    # word: Word in the word set
    words.append(word)

answer=[""]*6
a=-1
# game loop
while True:
    for i,s in enumerate(input().split()):
        state = int(s)
        if state==3:
            answer[i]=chr(97+a)
        
    a+=1
    if a==25:
        answer = ['z' if x == "" else x for x in answer]
    if "" not in answer:
        print("".join(answer))
    else:
        print(chr(97+a)*6)