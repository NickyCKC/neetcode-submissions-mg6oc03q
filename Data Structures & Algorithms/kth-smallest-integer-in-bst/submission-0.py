# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = []
        ls = self.arrange(root, ls)
        ls.sort()
        print(ls)
        return ls[k-1]

    def arrange(self, root: Optional[TreeNode], ls: list):
        if root is None:
            return ls
        
        ls.append(root.val)

        ls = self.arrange(root.left, ls)
        ls = self.arrange(root.right, ls)

        return ls
