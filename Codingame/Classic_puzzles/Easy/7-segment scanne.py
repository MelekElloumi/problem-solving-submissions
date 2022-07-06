line_1 = input()
line_2 = input()
line_3 = input()


for i in range(0,len(line_1),3):
    if line_2[i:i+3]=='| |':
        print(0,end="")
    elif line_2[i:i+3]=='  |':
        if line_1[i:i+3]=='   ':
            print(1,end="")
        else:
            print(7,end="")
    elif line_2[i:i+3]==' _|':
        if line_3[i:i+3]=='|_ ':
            print(2,end="")
        else:
            print(3,end="")
    elif line_2[i:i+3]=='|_ ':
        if line_3[i:i+3]=='|_|':
            print(6,end="")
        else:
            print(5,end="")
    else:
        if line_3[i:i+3]=='  |':
            print(4,end="")
        elif line_3[i:i+3]=='|_|':
            print(8,end="")
        else:
            print(9,end="")