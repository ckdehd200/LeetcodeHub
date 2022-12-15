class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<int> dp(text1.size()+1, text2.size());
        dp[0]=-1;
        unordered_map<int, vector<int>> cnt2;
        int m=0;
        for(int j=0;j<text2.size();j++){
            cnt2[text2[j]-'a'].push_back(j);
        }
        for(int i=0;i<text1.size();i++){
            int k=m, j=cnt2[text1[i]-'a'].size()-1; 
            // cout << "k " << k << " j " << j << endl;
            while(j>=0 && k >=0){
                if(cnt2[text1[i]-'a'][j] > dp[k]){
                    dp[k+1]=min(dp[k+1], cnt2[text1[i]-'a'][j]);
                    m=max(m,k+1);
                    j--;
                }
                else{
                    k--;
                }
            }
        }
        return m;
    }
};