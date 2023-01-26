class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f,t,c in flights:
            graph[f].append([t,c])
        dp=[[float('inf') for _ in range(k+2)] for _ in range(n)]
        dp[src][0]=0
        stack = deque([[src, 0]])
        ans = float('inf')
        while stack:
            # print(stack)
            source, step = stack.popleft()
            if source == dst : 
                ans = min(ans, dp[source][step])
                continue
            if step == k+1:
                continue
            for arrival, cost in graph[source]:
                # print(source, arrival)
                if dp[arrival][step+1]==float('inf') or dp[arrival][step+1] > dp[source][step]+cost :
                    stack.append([arrival, step+1])
                    dp[arrival][step+1] = dp[source][step] + cost
        # print(graph)
        # print(dp)
        if ans == float('inf'):
            return -1
        return ans