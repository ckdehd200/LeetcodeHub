class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1 for _ in range(len(nums))]
        if 2*k+1>n:
            return ans
        ksum = [sum(nums[:2*k+1])]
        for i in range(2*k+1,n):
            ksum.append(ksum[-1]+nums[i]-nums[i-(2*k+1)])
        for i in range(k,n-k):
            ans[i]=ksum[i-k]//(2*k+1)
        # print(ksum)
        return ans
            