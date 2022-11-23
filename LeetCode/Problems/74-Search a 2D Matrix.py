class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]==target:
                return True
            if matrix[m][0]<target and matrix[m][-1]>=target:
                break
            if matrix[m][0]<target :
                l=m+1
            else:
                r=m-1
        
        l,r=0,len(matrix[0])-1
        
        while l<=r:
            k=(l+r)//2
            if matrix[m][k]==target:
                return True
            if matrix[m][k]<target:
                l=k+1
            else:
                r=k-1
        
        return False