class Solution:
   def twoSum(self, n: List[int], t: int) -> List[int]:
       s = {}
       for i, v in enumerate(n):
           r=t-n[i]       
           if r in s:
               return [i, s[r]]           
           s[v] = i 