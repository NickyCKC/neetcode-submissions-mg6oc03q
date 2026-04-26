# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Handle edge case of empty root
        if not root:
            return 0
        
        # Continue normal execution
        if root.left:
            root.left.val = 1
        if root.right:
            root.right.val = 1
        if not root.left and not root.right:
            return 1
        
        # Recursive
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + max(l, r)
        