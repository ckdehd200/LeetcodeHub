class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        tot, plen = n*m, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=-1:
                    plen+=1
                if grid[i][j]==1:
                    start=i*n+j
                elif grid[i][j]==2:
                    end=i*n+j
        
        init = [0 for _ in range(tot)]
        stack = deque([])
        stack.append([init, start])
        ans = 0
        while stack:
            visited, pos = stack.popleft()
            new = visited[:]
            new[pos]=sum(visited)+1
            # print(new, pos)
            if pos==end:
                if sum(new)==2**plen-1:
                    ans+=1
                    # print(new)
                continue
            x,y = pos//n, pos%n
            if grid[x][y]==-1:
                continue
            
            if pos+1<tot and pos%n!=n-1 and visited[pos+1]==0: 
                stack.append([new, pos+1])
            if pos-1>=0 and pos%n!=0 and visited[pos-1]==0:
                stack.append([new, pos-1])
            if pos+n<tot and visited[pos+n]==0:
                stack.append([new, pos+n])
            if pos-n>=0 and visited[pos-n]==0:
                stack.append([new, pos-n])
        return ans