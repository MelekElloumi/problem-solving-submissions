class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        cur=1
        for i in range(1,n+1):
            if i==cur*2:
                cur=i
            ans[i]=1+ans[i-cur]
        return ans