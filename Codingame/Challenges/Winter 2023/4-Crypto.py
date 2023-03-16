def decrypt(first_a: str, first_b: str, second_b: str, second_c: str, secret_c: str) -> str:
    '''

    Args:

        - first_a (str): A first sentence (containing every letter from A to Z) in the alphabet A
        - first_b (str): The same sentence as firstA, translated in the alphabet B
        - second_b (str): A second sentence (containing every letter from A to Z) in the alphabet B
        - second_c (str): The same sentence as secondB, translated in the alphabet C
        - secret_c (str): The secret message in alphabet C to be deciphered

    Returns:

        The message secretC translated to the alphabet A
    '''
    d1={}
    for i in range(len(first_a)):
        d1[first_b[i]]=first_a[i]
    d2={}
    for i in range(len(second_b)):
        d2[second_c[i]]=second_b[i]
    x=""
    for i in range(len(secret_c)):
        x+=d1[d2[secret_c[i]]]
    return x