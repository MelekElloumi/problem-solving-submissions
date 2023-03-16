def solve(protons_start: int, neutrons_start: int, protons_target: int, neutrons_target: int) -> List[str]:
    '''

    Args:

        - protons_start (int): The initial number of protons
        - neutrons_start (int): The initial number of neutrons
        - protons_target (int): The desired number of protons
        - neutrons_target (int): The desired number of neutrons
    '''
    l=[]
    while protons_start>protons_target:
        l.append("ALPHA")
        protons_start-=2
        neutrons_start-=2
    while neutrons_start>neutrons_target:
        l.append("ALPHA")
        protons_start-=2
        neutrons_start-=2
    while neutrons_start!=neutrons_target:
        l.append("NEUTRON")
        neutrons_start+=1
    while protons_start!=protons_target:
        l.append("PROTON")
        protons_start+=1
    return l