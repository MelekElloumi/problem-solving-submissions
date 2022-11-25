class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def inorder(root):
            if not root:
                return 0
            return 1+max(inorder(root.right),inorder(root.left))
            
        
        return inorder(root)