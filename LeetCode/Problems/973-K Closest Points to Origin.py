import math
import heapq
class Solution:
    def dist(self,x,y):
        return math.sqrt(x**2+y**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[(self.dist(p[0],p[1]),p[0],p[1]) for p in points]
        heapq.heapify(distances)
        res=[]
        for i in range(k):
            dist, x, y = heapq.heappop(distances)
            res.append([x, y])
        return res
