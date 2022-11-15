class Solution:
    
    def rob(self, nums: List[int]) -> int:
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        return max(nums[0]+self.rob(nums[2:]),self.rob(nums[1:]))
        
        TLE
        """
        r1,r2=0,0
        for n in nums:
            temp=max(r1+n,r2)
            r1=r2
            r2=temp
        return max(r1,r2)