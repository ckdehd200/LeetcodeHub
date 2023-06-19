class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        tot, ans = 0, 0
        for k in gain:
            tot+=k
            if tot>ans:
                ans=tot
        return ans