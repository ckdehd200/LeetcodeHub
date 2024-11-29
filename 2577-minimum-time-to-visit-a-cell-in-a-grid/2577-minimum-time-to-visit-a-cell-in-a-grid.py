class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        else:
            m,n = len(grid), len(grid[0])
            # print(m,n)
            dist = [[float('inf') for _ in range(n)] for _ in range(m)]
            dist[0][0]=0
            heap=[]
            heapq.heappush(heap, (1, 1, 0))
            heapq.heappush(heap, (1, 0, 1))
            while heap:
                d, i, j = heapq.heappop(heap)
                new_d = max(d, grid[i][j]+1-((((i+j)&1))==((grid[i][j])&1)))
                if i==m-1 and j==n-1:
                    return new_d

                if new_d >= dist[i][j]: continue
                else:
                    dist[i][j] = new_d
                    if i>0:
                        heapq.heappush(heap, (new_d+1, i-1, j))
                    if i<m-1:
                        heapq.heappush(heap, (new_d+1, i+1, j))
                    if j>0:
                        heapq.heappush(heap, (new_d+1, i, j-1))
                    if j<n-1:
                        heapq.heappush(heap, (new_d+1, i, j+1))
                
                    