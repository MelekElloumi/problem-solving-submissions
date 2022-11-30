class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def inorder(root,s):
            if not root:
                return False      
            s+=root.val
            if not root.left and not root.right:
                return s==targetSum
            return inorder(root.left,s) or inorder(root.right,s)
        return inorder(root,0)