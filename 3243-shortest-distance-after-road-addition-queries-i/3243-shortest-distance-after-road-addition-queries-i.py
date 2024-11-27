class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {i: [i+1] for i in range(n-1)}
        answer = []
        for s, d in queries:
            graph[s].append(d)
        
            dp = [float('inf') for _ in range(n)]
            dp[0]=0
            for s in range(n-1):
                for d in graph[s]:
                    dp[d] = min(dp[d], dp[s]+1)
            answer.append(dp[n-1])
        return answer