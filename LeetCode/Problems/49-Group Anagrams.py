class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang={}
        for i in strs:
            x=''.join(sorted(i))
            if x in ang:
                ang[x].append(i)
            else:
                ang[x]=[i]
        return list(ang.values())