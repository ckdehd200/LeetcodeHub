class Solution {
public:
    int numTilings(int n) {
        int MOD = 1000000007;
        vector<vector<int> > dp(2+n, vector<int>(3,0));
        dp[1][0] = 1;
        dp[2] = {2,1,1};
        for(int i=3;i<n+1;i++){
            dp[i][0]=(dp[i-1][0]+dp[i-2][0])%MOD;
            dp[i][0]=(dp[i][0]+dp[i-1][1])%MOD;
            dp[i][0]=(dp[i][0]+dp[i-1][2])%MOD;
            dp[i][1]=(dp[i-1][2]+dp[i-2][0])%MOD;
            dp[i][2]=(dp[i-1][1]+dp[i-2][0])%MOD;
        }
        return dp[n][0];
    }
};