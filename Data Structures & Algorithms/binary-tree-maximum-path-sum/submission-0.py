# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def path(root):
            if not root: return 0
            nonlocal res
            
            left = path(root.left)
            right = path(root.right)

            sum = root.val + left + right
            res = max(res, sum)

            if sum < 0:
                return 0
            
            return root.val + max(left, right)
        
        path(root)
        return res


"""
we do this recursively, bottom up, and at every node, we sum its children (including only positive values) then save that as max_value if bigger than previous max_value

when returning you must save max(left, right) because the parents can't fork, they can only choose one path

10

-5 -> None
15
5
20 + 15 + 5 -> 40

-15 + 10 + 40 = 35
"""
