# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def getHeight(root):
            if not root:
                return 0

            left_h = getHeight(root.left)
            right_h = getHeight(root.right) 

            self.max_diameter = max(self.max_diameter, left_h + right_h)

            return 1 + max(left_h, right_h)
        
        getHeight(root)
        return self.max_diameter

        # largest diameter = left depth + right depth 
        # current diameter is max(left depth, right depth)