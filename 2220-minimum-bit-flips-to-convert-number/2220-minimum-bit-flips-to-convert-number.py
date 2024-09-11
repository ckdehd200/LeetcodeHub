class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bits = start^goal
        ans = 0
        while bits:
            bits &= bits-1
            ans+=1
        return ans