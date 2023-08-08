class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        else:
            pivot = 0
            n = len(nums)
            l,r = 0, n-1
            if nums[0]>nums[n-1]:
                while l<r:
                    mid=(l+r)//2
                    if nums[mid]>nums[mid+1]:
                        pivot = mid+1
                        break
                    elif nums[mid]>nums[0]:
                        l=mid+1
                    else:
                        r=mid
            l,r = pivot, pivot+n-1
            while l<r:
                mid = (l+r)//2
                if nums[mid%n]==target:
                    return mid%n
                elif nums[mid%n]>target:
                    r=mid
                else:
                    l=mid+1
            if nums[l%n]==target:
                return l%n
            else:
                return -1