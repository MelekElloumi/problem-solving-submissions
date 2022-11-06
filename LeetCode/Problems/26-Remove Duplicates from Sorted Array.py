class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for n in nums[1:]:
            if n!=nums[k-1]:
                nums[k]=n
                k+=1
        return k