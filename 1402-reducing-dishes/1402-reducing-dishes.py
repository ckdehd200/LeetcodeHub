class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        s = 0
        ans = 0
        satisfaction.sort(reverse=True)
        pointer = 0
        while pointer < len(satisfaction):
            if s + satisfaction[pointer] <= 0:
                return ans
            else:
                s+=satisfaction[pointer]
                ans+=s
            pointer += 1
        return ans