class Solution:
    
    def minImpossibleOR(self, nums: List[int]) -> int:
        return min([1<<e for e in range(40) if 1<<e not in set(nums)])