# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        queue = []
        if root:
            queue.append(root)

        while queue:
            array = []
            for _ in range(len(queue)):
                root = queue.pop(0)
                array.append(root.val)

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(array)
        
        return res


# do BFS, and at every layer, add node.values to array
# we can implement the BF traversal into the function using a for loop
# and return res after