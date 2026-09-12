# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        visible = []
        queue = []

        if root:
            queue.append(root)

        while queue:
            layer = []
            for _ in range(len(queue)):
                root = queue[0]
                
                if len(queue) <= 1:
                    visible.append(root.val)

                if root.left:
                    layer.append(root.left)
                if root.right:
                    layer.append(root.right)
                queue.pop(0)
                
            for roots in layer:
                queue.append(roots)

        return visible

# fo dis we need implement BFS
# in di for loop, if after popping der is noting left
# we return dis root to result
# return result