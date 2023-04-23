class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        CONST = 10**9+7
        n=len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1 
        for e in range(1,n+1):
            for l in range(1,10):
                if e-l<0:
                    break
                st = e-l
                arr = s[st:e]
                if arr[0]!='0' and int(arr)<=k :
                    dp[e]+=dp[st]
            dp[e]%=CONST
        return dp[n]