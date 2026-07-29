# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dicti = {value: index for index, value in enumerate(inorder)}
        self.preIdx = 0
        l, r = 0, len(inorder) - 1

        def arrange(l, r):
            if l > r:
                return None

            cur_value = preorder[self.preIdx]
            self.preIdx += 1
            node = TreeNode(cur_value)
            inordIdx = dicti[cur_value]
            node.left = arrange(l, inordIdx - 1)
            node.right = arrange(inordIdx + 1, r)
            return node
            

        return arrange(l, r)

