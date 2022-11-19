import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k>len(nums)//2:
            heapq.heapify(nums)
            for i in range(len(nums)-k+1):
                a=heapq.heappop(nums)
            return a
        else:
            nums=[-1*x for x in nums]
            heapq.heapify(nums)
            for i in range(k):
                a=heapq.heappop(nums)
            return -1*a