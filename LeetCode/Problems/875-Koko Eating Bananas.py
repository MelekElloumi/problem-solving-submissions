class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        m=max(piles)
        
        l,r=1,m
        res=m
        
        while l<=r:
            k=(l+r)//2
            t=sum([math.ceil(x/k) for x in piles])
            if t>h:
                l=k+1
            else:
                res=min(res,k)
                r=k-1
        return res
        