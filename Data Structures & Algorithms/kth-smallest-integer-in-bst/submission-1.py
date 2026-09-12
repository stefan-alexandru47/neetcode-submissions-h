# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(curr, k):
            stack = []
            i = 0

            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop()
                i += 1

                if i == k:
                    return curr.val
                    
                curr = curr.right
        
        return dfs(root, k)

"""        
            8
          /   \
         3     10
        / \      \
       1   6      14
          / \
         4   8
"""