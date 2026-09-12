class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        res = 0
        
        def dfs(root, k):
            nonlocal i
            nonlocal res
            
            if not root:
                return

            dfs(root.left, k)

            i += 1
            if i == k:
                res = root.val
                i += 1

            dfs(root.right, k)

        dfs(root, k)
        return res