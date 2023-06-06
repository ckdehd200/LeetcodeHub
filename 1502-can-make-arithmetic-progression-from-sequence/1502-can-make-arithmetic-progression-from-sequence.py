class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1]-arr[0]
        # ans=True
        for k in range(2,len(arr)):
            if arr[k]-arr[k-1]!=d:
                return False
        else:
            return True