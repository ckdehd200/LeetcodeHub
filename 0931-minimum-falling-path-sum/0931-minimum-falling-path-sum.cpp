class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n=matrix.size();
        vector<vector<int> > dp(n, vector<int>(n, 10000));
        for(int row=0; row<n; row++){
            for(int col=0; col<n; col++){
                if(row==0){
                    dp[row][col]=matrix[row][col];
                }
                else{
                    int pos=dp[row-1][col];
                    if(col>0){pos=min(pos, dp[row-1][col-1]);}
                    if(col<n-1){pos=min(pos, dp[row-1][col+1]);}
                    dp[row][col]=pos+matrix[row][col];
                }
            }
        }
        int ans=10000;
        for(int col=0;col<n;col++){
        ans = min(ans, dp[n-1][col]);}
        // for(int row=0;row<n;row++){
        //     for(int col=0;col<n;col++){
        //         cout << dp[row][col] << ' ';
        //     }
        //     cout << endl;
        // }
        return ans;
    }
};