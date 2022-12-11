# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_triple(self, root):
        ans = [root.val for _ in range(3)]
        fromleft = [-float('inf') for _ in range(3)]
        fromright = [-float('inf') for _ in range(3)]
        if root.left:
            fromleft = self.dfs_triple(root.left)
            ans[1] += max(max(fromleft[1:]), 0)
            ans[0] += max(max(fromleft[1:]), 0)
        if root.right : 
            fromright = self.dfs_triple(root.right)
            ans[2] += max(max(fromright[1:]), 0)
            ans[0] += max(max(fromright[1:]), 0)
        ans[0] = max(max(ans), fromleft[0], fromright[0])
        return ans

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        L = self.dfs_triple(root)
        return L[0]