class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[0 for _ in range(n)] for _ in range(n)]
        for k in range(n):
            dp[k][k]=1
        for k in range(n-1):
            if s[k]==s[k+1]:
                dp[k][k+1]=1
        for l in range(2,n):
            for k in range(n-l):
                if s[k]==s[k+l] and dp[k+1][k+l-1]:
                    dp[k][k+l]=1
        ans = sum(list(map(sum,dp)))
        return ans
            