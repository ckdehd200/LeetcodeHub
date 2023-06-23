class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        dp = [[1]*1001 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = dp[j][d] + 1
        
        L = [max(dp[i]) for i in range(len(nums))]
        # L = [max(dp[i].values()) for i in range(len(nums))]
        return max(L)