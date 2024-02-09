class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> dp;
        vector<int> ans;
        for(int i=0;i<n;i++){
            dp.push_back({nums[i]}); 
            for(int j=0;j<i;j++){
                if(nums[i]%nums[j]==0 && dp[j].size()>=dp[i].size()){
                    dp[i]=dp[j];
                    dp[i].push_back(nums[i]);
                }
            }
            if(dp[i].size()>ans.size()){
                ans=dp[i];
            }
        }
        
        return ans;
    }
};