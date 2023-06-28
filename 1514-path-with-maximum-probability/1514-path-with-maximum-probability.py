class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            a,b = edges[i]
            graph[a].append([succProb[i],b])
            graph[b].append([succProb[i],a])
        
        d = [0 for _ in range(n)]
        d[start]=1
        dq = [[-1, start]]
        ans = 0
        while dq:
            p, v = heapq.heappop(dq)
            if v==end:
                ans = -p
                break
            p*=-1
            for p0, w in graph[v]:
                if d[w] < p*p0:
                    d[w] = p*p0
                    heapq.heappush(dq,[-p*p0, w])
        return ans