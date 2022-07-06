s=[]
for i in range(9):
    s.append(list(map(int,input().split())))

t='true'
for i in range(1,10):
    for j in range(9):
        if i not in s[j]:
            t='false'
        if i not in [row[j] for row in s]:
            t='false'
    GRID_SIZE=9
    SUBGRID_SIZE=3
    for subgrid_col in range(0,GRID_SIZE,SUBGRID_SIZE):
        for subgrid_row in range(0,GRID_SIZE,SUBGRID_SIZE):
            sg=[]
            for d in range(SUBGRID_SIZE):
                for c in range(SUBGRID_SIZE):
                    sg.append(s[subgrid_col+d][subgrid_row+c])
            if  i not in sg:
                t='false'
print(t)