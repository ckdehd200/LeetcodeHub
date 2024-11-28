class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        heap = []
        m,n = len(grid), len(grid[0])
        dist = [[m*n for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        dist[0][0]=0
        heapq.heappush(heap, [0,0,0])
        
        while heap:
            d, i, j = heapq.heappop(heap)
            if i==m-1 and j==n-1:
                return d
            if visited[i][j]:
                continue
            else:
                visited[i][j]=True
                dist[i][j]=d
                if i>0:
                    heapq.heappush(heap, [d+grid[i-1][j], i-1, j])
                if i<m-1:
                    heapq.heappush(heap, [d+grid[i+1][j], i+1, j])
                if j>0:
                    heapq.heappush(heap, [d+grid[i][j-1], i, j-1])
                if j<n-1:
                    heapq.heappush(heap, [d+grid[i][j+1], i, j+1])
        