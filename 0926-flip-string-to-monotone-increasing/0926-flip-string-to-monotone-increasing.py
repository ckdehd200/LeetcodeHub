class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n=len(s)
        ones = [0 for _ in range(n+1)]
        zeros = [0 for _ in range(n+1)]
        for i in range(n):
            if s[i]=='1':
                ones[i+1]=ones[i]+1
            else:
                ones[i+1]=ones[i]
                
        for i in reversed(range(n)):
            if s[i]=='0':
                zeros[i] = zeros[i+1]+1
            else:
                zeros[i] = zeros[i+1]
        m = ones[n]
        for i in range(n):
            m = min(ones[i] + zeros[i], m)
        # print(ones)
        # print(zeros)
        return m
        