class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for op in operations:
            if op=="+":
                score.append(score[-1]+score[-2])
            elif op=="D":
                score.append(score[-1]*2)
            elif op=="C":
                score.pop()
            else:
                score.append(int(op))
        return sum(score)