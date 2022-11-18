# Author: Malloumario
#!/usr/bin/env python
from bisect import bisect_left
import os
from math import ceil, factorial, fmod,pi,sqrt,log
import sys
from collections import Counter, deque, defaultdict
import heapq
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


BUFSIZE = 8192
 
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# endregion
 
def read_arr():
    return [int(x) for x in input().split()]

m="Yes"*335
def solve():
    x=input()
    if x in m:
        print("YES")
    else:
        print("NO")

def main():
    T=1
    T=int(input())
    while(T):
        solve()
        T-=1     

if __name__ == "__main__":
    main()