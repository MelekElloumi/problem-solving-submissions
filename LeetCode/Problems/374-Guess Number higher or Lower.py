class Solution:
    def guessNumber(self, n: int) -> int:
        l,r=1,n
        c=-1
        while c!=0:
            g=(l+r)//2
            c=guess(g)
            if c==0:
                return g
            if c>0:
                l=g+1
            else:
                r=g-1