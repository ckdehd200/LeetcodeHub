# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def levelsum(root):
            l,r = [],[]
            if root.left:
                l=levelsum(root.left)
            if root.right:
                r=levelsum(root.right)
            if len(l)>len(r):
                l,r=r,l
            ans = [root.val]
            for k in range(len(l)):
                ans.append(l[k]+r[k])
            for k in range(len(l),len(r)):
                ans.append(r[k])
            return ans
        ans, M = 0, -float('inf')
        s = levelsum(root)
        for k in range(len(s)):
            if M<s[k]:
                ans=k+1
                M=s[k]
        return ans