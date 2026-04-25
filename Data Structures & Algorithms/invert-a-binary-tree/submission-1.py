# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Handle edge case of empty list
        if not root:
            return root
        # Handle list with one item only
        if root and not root.left and not root.right:
            return root

        # Cotinue normal execution
        if not root.left and not root.right:
            return
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
        
        # Use recursive
        self.invertTree(root.left)
        self.invertTree(root.right)
        return(root)