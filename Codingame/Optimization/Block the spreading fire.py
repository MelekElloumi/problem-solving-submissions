import sys
import math
# Read the constant data of the map before the main loop, then read the state of the fire and give an action at each turn
def dist(x,y,a,b):
    return abs(x-a)+abs(y-b)
# tree_treatment_duration: cooldown for cutting a "tree" cell
# tree_fire_duration: number of turns for the fire to propagate on adjacent cells from a "tree" cell
# tree_value: value lost if a "tree" cell is burnt or cut
tree_treatment_duration, tree_fire_duration, tree_value = [int(i) for i in input().split()]
# house_treatment_duration: cooldown for cutting a "house" cell
# house_fire_duration: number of turns for the fire to propagate on adjacent cells from a "house" cell
# house_value: value lost if a "house" cell is burnt or cut
house_treatment_duration, house_fire_duration, house_value = [int(i) for i in input().split()]
# width: number of columns in the grid
# height: number of rows in the grid
width, height = [int(i) for i in input().split()]
# fire_start_x: column where the fire starts
# fire_start_y: row where the fire starts
houses=[]
trees=[]
fx, fy = [int(i) for i in input().split()]
g=[]
for i in range(height):
    grid_line = input()
    g.append(list(grid_line))
    for j in range(len(grid_line)):
        if grid_line[j]=='X':
            houses.append([j,i])
        if grid_line[j]=='.':
            trees.append([j,i])
solution=[]

no=0
if tree_treatment_duration<tree_fire_duration and len(houses)==1:
    solution+=[[[fx,fy+1],[fx,fy+1]],[[fx,fy-1],[fx,fy-1]],[[fx-1,fy],[fx-1,fy]],[[fx+1,fy],[fx+1,fy]]]
    no=1    
if len(houses)==0 and len(trees)<30:
    solution+=[[[fx,fy+1],[fx,fy+1]],[[fx,fy-3],[fx,fy-3]]]
    no=1
if len(houses)==0 and len(trees)>80:
    no=1
    for j in reversed(range(0,fx)):
        solution+=[[[j,height-j-2],[j,height-j-2]],[[width-j-2,height-width+j],[width-j-2,height-width+j]]]
    for j in range(width*2//3,width-1):
        solution+=[[[j,height+width*2//3-2-j],[j,height+width*2//3-2-j]]]
if len(houses) in range(3,8) and len(trees)>50:
    no=1
    jo=1
    mi=height
    for i in reversed(range(min(fy,houses[0][1]),max(fy,houses[0][1])+1)):
        #ll=[row[j] for row in g].count('.')
        ll=g[i].count('.')
        if ll>0 and ll<=mi:
            mi=ll
            jo=i
    for t in trees:
        if t[1]==jo:
            #solution+=[[[jo,t[1]],[jo,t[1]]]]
            solution+=[[[t[0],jo],[t[0],jo]]]
if len(houses)>120:
    iw=height-2
    no=1
    for i in range(height-1):
        s=''.join(g[i])
        sl=s.lstrip('#')
        nl=len(s)-len(sl)
        s=sl.rstrip('#')
        if '#' in s:
            si=s.index('#')
            for j in range(nl,nl+si):
                solution+=[[[j,i-1],[j,i-1]]]
            break
if len(houses)<120 and len(houses)>80:
    no=1
    for j in range(1,height//2+2):
        if [j,height//2+2-j] in trees or [j,height//2+2-j] in houses:
            solution+=[[[j,height//2+2-j],[j,height//2+2-j]]]
if no==0:
    if len(houses)!=0:
        po=[]
        for k in houses:
            po.append([dist(fx,fy,k[0],k[1]),k])
        po.sort()
        for i in reversed(range(len(houses))):
            x1=po[i][1][0]
            y1=po[i][1][1]
            solution+=[[[x1,y1],[x1,y1-1]],[[x1,y1],[x1-1,y1]],[[x1,y1],[x1+1,y1]],[[x1,y1],[x1,y1+1]]]

    if len(trees)!=0:
        pa=[]
        for k in trees:
            pa.append([dist(fx,fy,k[0],k[1]),k])
        pa.sort()
        for i in reversed(range(len(trees))):
            x1=pa[i][1][0]
            y1=pa[i][1][1]
            solution+=[[[x1,y1],[x1,y1-1]],[[x1,y1],[x1-1,y1]],[[x1,y1],[x1+1,y1]],[[x1,y1],[x1,y1+1]]]


# game loop
x=0
while True:
    cooldown = int(input())  # number of turns remaining before you can cut a new cell
    for i in range(height):
        for j in input().split():
            # fire_progress: state of the fire in this cell (-2: safe, -1: no fire, 0<=.<fireDuration: fire, fireDuration: burnt)
            fire_progress = int(j)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if cooldown>0:
        print("WAIT")
    else:
        while x<len(solution) and (g[solution[x][1][1]][solution[x][1][0]]=='#' or g[solution[x][0][1]][solution[x][0][0]]=='#'):
            x+=1
        if x<len(solution):    
            print(solution[x][1][0],solution[x][1][1])
            g[solution[x][1][1]][solution[x][1][0]]='#'
            x+=1
        else:
            print("WAIT")
