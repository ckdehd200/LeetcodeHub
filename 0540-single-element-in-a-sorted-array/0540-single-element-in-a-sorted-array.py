class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        k = n // 2
        l,r = 0,k
        while l<r:
            mid = (l+r)//2
            c = 2*mid + 1
            if nums[c]==nums[c-1]:
                l=mid+1
            elif nums[c]==nums[c+1]:
                r=mid
            else:
                return nums[c]
        return nums[2*l]