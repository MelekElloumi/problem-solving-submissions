def decrypt(s1: str, s2: str) -> str:
    '''

    Args:

        - s1 (str): the first line of the page, composed of uppercase letters only
        - s2 (str): the second line, composed of uppercase letters and of the same length as s1

    Returns:

        the decrypted message, created by alternating the letters of s1 and s2
    '''
    x=""
    for i in range(len(s1)):
        x+=s1[i]+s2[i]
    return x