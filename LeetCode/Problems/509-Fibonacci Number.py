class Solution: 
    def __init__(self):
        self.dp={}
    
    def fib(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        if n<2:
            self.dp[n]=n
            return n
        self.dp[n]=self.fib(n-1)+self.fib(n-2)
        return self.dp[n]