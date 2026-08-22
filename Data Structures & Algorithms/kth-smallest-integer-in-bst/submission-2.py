# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def treeList(root):
            if not root:
                return
            else:
                tree_list.append(root.val)
            treeList(root.left)
            treeList(root.right)
        
        tree_list = []
        treeList(root)
        heapq.heapify(tree_list)
        for n in range(k-1):
            heapq.heappop(tree_list)
        return heapq.heappop(tree_list)
                