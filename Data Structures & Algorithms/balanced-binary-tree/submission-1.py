# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.da_bool = True

        def check(root):
            if not root:
                return 0
            if self.da_bool == False:
                return 0

            left = check(root.left)
            right = check(root.right)

            if abs(left - right) > 1:
                self.da_bool = False
            return 1 + max(left, right)
        
        check(root)
        
        return self.da_bool
