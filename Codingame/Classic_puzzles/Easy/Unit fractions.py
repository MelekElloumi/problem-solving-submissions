n = int(input())

for y in range(n+1,2*n+1):
    x=n*y/(y-n)
    if x%1==0:
        print(f'1/{n} = 1/{int(x)} + 1/{y}')