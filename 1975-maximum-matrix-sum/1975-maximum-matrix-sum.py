class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minabs = float('inf')
        negcnt = 0
        tot = 0
        n, m = len(matrix), len(matrix[0])
        for r in range(n):
            for c in range(m):
                if matrix[r][c] <0 :
                    negcnt += 1
                tot += abs(matrix[r][c])
                minabs = min(minabs, abs(matrix[r][c]))
                
        if negcnt&1 : 
            return tot-2*minabs
        else:
            return tot