# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_depth = 0


    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right) 
        child_max = max(left, right)

        depth = 1 + child_max

        return depth
