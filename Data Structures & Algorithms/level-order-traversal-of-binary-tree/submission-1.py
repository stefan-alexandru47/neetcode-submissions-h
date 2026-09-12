# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.BFS(root)
        return self.res
        
    def BFS(self, root):
        if not root:
            return
        queue = []
        queue.append(root)

        while queue:
            array = []
            n = len(queue)

            for _ in range(n):
                node = queue.pop(0)

                array.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            self.res.append(array)