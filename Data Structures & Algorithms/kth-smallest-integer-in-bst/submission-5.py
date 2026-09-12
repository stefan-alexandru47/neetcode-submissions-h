# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        i = 0
        res = 0
        done = False
        
        def dfs(root, k):
            nonlocal i
            nonlocal res
            nonlocal done
            
            if not root or done:
                return

            dfs(root.left, k)
            i += 1
            if i == k:
                res = root.val
                i += 1
                return

            dfs(root.right, k)

            if i == k:
                res = root.val
                i += 1

        dfs(root, k)
        return res