from collections import defaultdict

class Solution:
    def tr(self,n):
        return (n*(n+1))//2
    
    def cnts(self, nums, minK, maxK):
        if minK==maxK:
            return self.tr(len(nums))
        n = len(nums)
        Ms, ms = [-1], [-1]
        for i in range(n):
            if nums[i] == maxK:
                Ms.append(i)
            if nums[i] == minK:
                ms.append(i)
        if Ms==[-1] or ms==[-1]:
            return 0
        else:
            Ms.append(n)
            ms.append(n)
            ans = self.tr(len(nums))
            for i in range(len(Ms)-1):
                ans -= self.tr(Ms[i+1] - Ms[i] - 1)
            for i in range(len(ms)-1):
                ans -= self.tr(ms[i+1] - ms[i] - 1)
            tot = Ms+ms[1:-1]
            tot.sort()
            for i in range(len(tot)-1):
                ans += self.tr(tot[i+1]-tot[i]-1)
            return ans
        
        
    
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        arrays = []
        array = []
        for i in nums:
            if i>maxK or i<minK:
                if array:
                    arrays.append(array)
                    array=[]
            else:
                array.append(i)
        if array:
            arrays.append(array)
        if len(arrays)==0:
            return 0
        else:
            ans = 0
            for l in arrays:
                ans+=self.cnts(l, minK, maxK)
            return ans