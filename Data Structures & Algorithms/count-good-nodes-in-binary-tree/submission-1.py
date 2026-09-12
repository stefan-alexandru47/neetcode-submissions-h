# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = [-101]

        def traverse(root):
            nonlocal res
            top_val = stack[-1]

            if not root:
                return

            if root.val >= top_val:
                stack.append(root.val)
                res += 1

            left = traverse(root.left)
            right = traverse(root.right)

            if root.val >= top_val:
                stack.pop(-1)

        traverse(root)
        return res


# do DFS
# before calling next root, save value to stack
# check if value is smaller than biggest, and if bigger then add 1 to res
# 