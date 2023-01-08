from math import gcd
from functools import reduce
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        lines = defaultdict(set)
        for i in range(len(points)):
            for j in range(i):
                p_i = tuple(points[i])
                x1,y1 = points[i]
                p_j = tuple(points[j])
                x2,y2 = points[j]
                line = [y2-y1, x1-x2, y1*x2 - x1*y2]
                d = reduce(gcd, line, 0)
                coef = tuple(map(lambda x:x//d, line))
                if p_i not in lines[coef]:
                    lines[coef].add(p_i)
                if p_j not in lines[coef]:
                    lines[coef].add(p_j)
        ans = 0
        for s in lines.values():
            ans = max(ans, len(s))
        return ans