# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.graph = {}
    def find_tree_graph(self, root, n=0):
        if n not in self.graph:
            self.graph[n]=[]
        self.graph[n].append(root.val)
        if root.left is not None:
            self.find_tree_graph(root.left, n+1)
        if root.right is not None:
            self.find_tree_graph(root.right, n+1)
        
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.find_tree_graph(root)
        answer = []
        keys = sorted(self.graph.keys())
        for k in keys:
            answer.append(max(self.graph[k]))
        return answer
            
            