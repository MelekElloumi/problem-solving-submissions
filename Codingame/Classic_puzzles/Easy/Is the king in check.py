c=[]
kx,ky=-1,-1
for i in range(8):
    chess_row = input().replace(' ','')
    if 'K' in chess_row:
        ky=i
        kx=chess_row.index('K')
    c.append(chess_row)
for i in range(8):
    for j in range(8):
        if c[i][j]=='R':
            if i==ky or j==kx:
                print("Check")
                exit(0)
        if c[i][j]=='B':
            if abs(i-ky)==abs(j-kx):
                print("Check")
                exit(0)  
        if c[i][j]=='Q':
            if abs(i-ky)==abs(j-kx) or i==ky or j==kx:
                print("Check")
                exit(0)
        if c[i][j]=='N':
            if (abs(ky-i)==2 and abs(kx-j)==1) or (abs(ky-i)==1 and abs(kx-j)==2):
                print("Check")
                exit(0)  
print("No Check")