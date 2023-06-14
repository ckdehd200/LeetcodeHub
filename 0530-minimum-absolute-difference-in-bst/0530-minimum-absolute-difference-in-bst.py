# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minmax(self, root):
        l,r = root.val, root.val
        if root.left:
            l = self.minmax(root.left)[0]
        if root.right:
            r = self.minmax(root.right)[1]
        return l,r
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        L, R = None, None
        if root.left:
            ans = min(ans, self.getMinimumDifference(root.left))
            L = self.minmax(root.left)
            ans = min(ans, abs(root.val - L[1]))
        if root.right:
            ans = min(ans, self.getMinimumDifference(root.right))
            R = self.minmax(root.right)
            ans = min(ans, abs(root.val - R[0]))
        if root.left and root.right:
            ans = min(ans, R[0]-L[1])
#         print(root.val, ans, L, R)
        
#         print()
        return ans