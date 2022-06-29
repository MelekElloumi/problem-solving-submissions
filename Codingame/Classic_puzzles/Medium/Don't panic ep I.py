import sys

def xor(x, y):
    return bool((x and not y) or (not x and y))

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elev={}
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elev[elevator_floor]=elevator_pos

clon={}
x=1
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  
    clone_pos = int(inputs[1])  
    direction = inputs[2]  
    if clone_floor==-1:
        continue
    if x:
        print("WAIT")
        x=0

    if clone_floor==exit_floor:

        if clone_floor not in clon.keys():
            if  not xor(direction=="LEFT", exit_pos>clone_pos):           
                print("BLOCK")
                clon[clone_floor]=clone_pos
            else:
                print("WAIT")
        else:
            print("WAIT")
    else:
        if clone_floor not in clon.keys():
            if elev[clone_floor]==clone_pos:
                print("WAIT")
            elif  not xor(direction=="LEFT", elev[clone_floor]>=clone_pos):  
                print("BLOCK")
                clon[clone_floor]=clone_pos
            else:
                print("WAIT")
        else:
            print("WAIT")