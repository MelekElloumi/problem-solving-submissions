t = input().split()
for x in t:
    if x=="nl":
        print()
    elif "bS" in x:
        print('\\'*int(x[:-2]),end='')
    elif "sQ" in x:
        print('\''*int(x[:-2]),end='')
    elif "sp" in x:
        print(' '*int(x[:-2]),end='')
    else:
        print(x[-1]*int(x[:-1]),end='')