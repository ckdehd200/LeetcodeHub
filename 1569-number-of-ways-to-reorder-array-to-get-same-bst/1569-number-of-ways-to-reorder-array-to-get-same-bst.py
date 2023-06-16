class Solution:
    def __init__(self):
        self.const = 10**9+7
    #     self.nchoosek = [[1 for j in range(i+1)] for i in range(1001)]
    #     for i in range(2,1001):
    #         for j in range(1,i):
    #             self.nchoosek[i][j] = (self.nchoosek[i-1][j] + self.nchoosek[i-1][j-1]) % self.const
        
    def no(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 1
        
        larger, smaller = [],[]
        for i in range(1,len(nums)):
            if nums[i]>nums[0]:
                larger.append(nums[i])
            else:
                smaller.append(nums[i])
        n,k = len(nums)-1, len(larger)
        # return (self.no(larger)*self.no(smaller)*self.nchoosek[n][k])%self.const
        return (self.no(larger)*self.no(smaller)*comb(n,k))%self.const
        
    def numOfWays(self, nums: List[int]) -> int:
        return (self.no(nums)-1)%self.const