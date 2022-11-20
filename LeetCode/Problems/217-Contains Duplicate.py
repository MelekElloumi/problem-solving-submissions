from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h=defaultdict(int)
        for i in nums:
            h[i]+=1
            if h[i]>1:
                return True
        return False
        