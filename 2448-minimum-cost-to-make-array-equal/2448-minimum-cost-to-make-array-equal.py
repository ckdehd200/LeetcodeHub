class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pos = []
        for i in range(len(nums)):
            pos.append([nums[i], cost[i]])
        pos.sort(key=lambda x:x[0])
        # print(pos)
        slope = -sum(cost)
        ans = 0
        for k in range(len(nums)):
            # print(k,pos[k],slope)
            if slope*(slope+2*pos[k][1])<=0:
                for j in range(len(nums)):
                    ans += abs(nums[j]-pos[k][0])*cost[j]
                return ans
            slope+=2*pos[k][1]