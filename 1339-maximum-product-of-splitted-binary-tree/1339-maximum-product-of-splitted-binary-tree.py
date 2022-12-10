# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:        
        MOD = 10**9+7
        D = []
        def dfs(root):
            ans = root.val
            if root.left:
                ans+=dfs(root.left)
            if root.right:
                ans+=dfs(root.right)
            D.append(ans)
            return ans
        dfs(root)
        m=max(D)
        ans = 0
        for k in D:
            ans = max(ans,k*(m-k))
        return ans % MOD
                