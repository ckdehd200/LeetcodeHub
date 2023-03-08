class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        while l<r: 
            mid = (l+r)//2
            cnt = 0
            for k in piles:
                cnt+=((k-1)//mid)+1
            if cnt > h : 
                l=mid+1
            else:
                r=mid
        return l
    