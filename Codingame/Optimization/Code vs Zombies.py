import sys
import math
import time
import random
# Save humans, destroy zombies!

def strategy(zombies):
    moves=[]
    for i in range(random.randrange(3)):
        moves.append([random.randrange(16000),random.randrange(9000)])
    random.shuffle(zombies)
    for i in zombies:
        moves.append([(i[3]+i[1])//2,(i[4]+i[2])//2])
    return moves

def simulate(zombies,x,y,moves):
    score=0
    return score
#tt=0

while True:
    start_time = time.time()
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    humans=[]
    for i in range(human_count):
        #human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append([int(j) for j in input().split()])
    zombie_count = int(input())
    zombies=[]
    for i in range(zombie_count):
        #zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies.append([int(j) for j in input().split()])
    
    dhzs=[]
    for z in zombies:
        for h in humans:
            dhz=math.sqrt((h[1]-z[1])**2+(h[2]-z[2])**2)
            dhzs.append([dhz,h[1],h[2]])
    dhzs.sort()
    print(dhzs, file=sys.stderr, flush=True)
    if human_count==1:
        print(humans[0][1],humans[0][2])
    else:
        for i in dhzs:
            dhp=math.sqrt((i[1]-x)**2+(i[2]-y)**2)
            if i[0]//400 > int(math.ceil(dhp//1000)):
                print(i[1],i[2])
                break
    #tt=max(tt,time.time()-start_time)
    print(time.time()-start_time, file=sys.stderr, flush=True)
