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
            n = len(queue)
            for _ in range(n):
                root = queue.pop(0)

                if n <= 1:
                    visible.append(root.val) # if it is the right-most element in the layer, we append its value

                if root.left: 
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                n -= 1

        return visible

# fo dis we need implement BFS
# in di for loop, if after popping der is noting left
# we return dis root to result
# return result

# for each n, we do n * 2 as we have to loop through n twice