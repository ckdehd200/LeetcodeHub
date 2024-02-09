class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[nums[i]] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(dp[j])>=len(dp[i]):
                    dp[i] = dp[j][:]
                    dp[i].append(nums[i])
        ans = []
        for i in range(len(dp)):
            if len(dp[i])>len(ans):
                ans = dp[i]
        return ans