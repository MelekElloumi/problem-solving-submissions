import sys
import math

def res_and(signal1,signal2):
    l=[]
    for i in range(len(signal1)):
        if signal1[i]=='-' and signal2[i]=='-':
            l.append('-')
        else:
            l.append('_')
    return ''.join(l)


def res_or(signal1,signal2):
    l=[]
    for i in range(len(signal1)):
        if signal1[i]=='_' and signal2[i]=='_':
            l.append('_')
        else:
            l.append('-')
    return ''.join(l)

def res_xor(signal1,signal2):
    l=[]
    for i in range(len(signal1)):
        if signal1[i]==signal2[i]:
            l.append('_')
        else:
            l.append('-')
    return ''.join(l)

def res_not(signal1):
    l=[]
    for i in range(len(signal1)):
        if signal1[i]=='-':
            l.append('_')
        else:
            l.append('-')
    return ''.join(l)

def res_nand(signal1,signal2):
    return res_not(res_and(signal1,signal2))

def res_nor(signal1,signal2):
    return res_not(res_or(signal1,signal2))

def res_nxor(signal1,signal2):
    return res_not(res_xor(signal1,signal2))

n = int(input())
m = int(input())
sinput={}
for i in range(n):
    input_name, input_signal = input().split()
    sinput[input_name]=input_signal
for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    if _type == "AND":
        result=res_and(sinput[input_name_1],sinput[input_name_2])
    elif _type == "OR":
        result=res_or(sinput[input_name_1],sinput[input_name_2])
    elif _type == "XOR":
        result=res_xor(sinput[input_name_1],sinput[input_name_2])
    elif _type == "NAND":
        result=res_nand(sinput[input_name_1],sinput[input_name_2])
    elif _type == "NOR":
        result=res_nor(sinput[input_name_1],sinput[input_name_2])
    else:
        result=res_nxor(sinput[input_name_1],sinput[input_name_2])
    print(output_name,result)
