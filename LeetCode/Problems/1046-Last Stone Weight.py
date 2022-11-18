import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-1*x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            if x!= y:
                heapq.heappush(stones, -1*abs(x-y))
        return 0 if not stones else -1*stones[0]
        