# Author: Malloumario
#!/usr/bin/env python
from bisect import bisect_left
import os
from math import ceil, factorial, fmod,pi,sqrt,log
import sys
from collections import Counter
from io import BytesIO, IOBase, StringIO

def modFact(n, p):
    if n >= p:
        return 0   
 
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % p
 
    return result
 
def calculate(p, q):
     
    mod = 998244353
    expo = 0
    expo = mod - 2
 
    # Loop to find the value
    # until the expo is not zero
    while (expo):
 
        # Multiply p with q
        # if expo is odd
        if (expo & 1):
            p = (p * q) % mod
        q = (q * q) % mod
 
        # Reduce the value of
        # expo by 2
        expo >>= 1
 
    return p
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

def bin_search(num, arr):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid=(start+end)//2
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            end= mid-1
        else:
            start = mid + 1
    return -1


def factors(n) :
     
    # Note that this loop runs till square root
    i = 1
    ans=[]
    while i <= sqrt(n):
         
        if (n % i == 0) :
             
            # If divisors are equal, print only one
            if (n / i == i) :
                ans.append(i)
            else :
                # Otherwise print both
                
                ans.append(i)
                ans.append(int(n/i))
        i = i + 1
    return ans

def is_palindrome(n):
    for j in range(len(n)//2):
        if n[j]!=n[len(n)-j-1]:
            return False
    return True

def nCr(n, r):
     
    return (fact(n) / (fact(r)
                * fact(n - r)))
 
# Returns factorial of n
def fact(n):
 
    res = 1
     
    for i in range(2, n+1):
        res = res * i
    return res


 
# endregion
 
def read_arr():
    return [int(x) for x in input().split()]

def solve():
    o=[int(x) for x in input().split()]
    l=0
    for i in o:
        if i>=o[0]:
            l+=1
    print(l-1)

def main():
    T=1
    T=int(input())
    while(T):
        solve()
        T-=1     

if __name__ == "__main__":
    main()