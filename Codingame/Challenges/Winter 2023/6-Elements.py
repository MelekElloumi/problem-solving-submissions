def collisions(particles: List[List[int]]) -> int:
    '''

    Args:

        - particles (List[List[int]]): the list of coordinates of the particles, in nm

    Returns:

        The number of potential collisions
    '''
    x=0
    for i in range(len(particles)):
        for j in range(i+1,len(particles)):
            if ((particles[i][0]-particles[j][0])**2+(particles[i][1]-particles[j][1])**2)**0.5<=1000:
                x+=1
    return x