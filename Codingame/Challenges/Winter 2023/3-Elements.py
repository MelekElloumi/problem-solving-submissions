def solve(grid: List[List[int]], rules: List[dict]) -> List[List[int]]:
    '''

    Args:

        - grid (List[List[int]]): The initial grid of elements
        - rules (List[dict]): Transition rules between elements
    '''
    s=[]
    for i in range(len(grid)-1):
        m=[]
        for j in range(len(grid)-1):
            x=[grid[i][j],grid[i][j+1],grid[i+1][j],grid[i+1][j+1]]
            m.append(x)
        s.append(m)
    for i in range(len(s)):
        for j in range(len(s)):
            p=True
            for k in rules:
                if k["pattern"]==s[i][j]:
                    s[i][j]=k["result"]
                    p=False
                    break
            if p:
                s[i][j]=0         
    return s