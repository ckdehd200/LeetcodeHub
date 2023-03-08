class Solution:
    
    def minImpossibleOR(self, nums: List[int]) -> int:
        return min([1<<e for e in range(40) if 1<<e not in {k:1 for k in nums}.keys()])