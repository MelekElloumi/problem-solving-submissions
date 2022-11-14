class Solution:
    def hammingWeight(self, n: int) -> int:
        answer=0
        while n!=0:
            n=n & (n-1)
            answer+= 1
        return answer