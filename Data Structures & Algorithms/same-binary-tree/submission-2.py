# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.array1 = []
        self.array2 = []

        def single1(root):
            if not root:
                return
            left = single1(root.left)
            right = single1(root.right)

            self.array1.append(left)
            self.array1.append(right)

            return root.val

        def single2(root):
            if not root:
                return
            left = single2(root.left)
            right = single2(root.right)

            self.array2.append(left)
            self.array2.append(right)
            
            return root.val


        def check(p, q):
            root_p = single1(p)
            root_q = single2(q)

            self.array1.append(root_q)
            self.array2.append(root_p)

            print(self.array1, self.array2)
            
            if self.array1 != self.array2:
                return False
            return True

        return check(p, q)
