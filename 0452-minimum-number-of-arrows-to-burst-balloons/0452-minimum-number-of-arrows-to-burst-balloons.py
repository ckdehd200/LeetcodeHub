class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort(key = lambda x:x[1], reverse=True)
        while points:
            _, y = points.pop()
            ans+=1
            while points and points[-1][0] <= y <= points[-1][1]:
                points.pop()
        return ans