class dsu:
    def __init__(self, N):
        self.par = [i for i in range(N)]
        
    def find(self, n):
        if self.par[n] == n :
            return n
        else :
            self.par[n] = self.find(self.par[n])
            return self.par[n]
    
    def union(self, x, y):
        x,y=self.find(x), self.find(y)
        if x>y:
            x,y=y,x
        self.par[y]=x
        

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def str2list(s):
            return list(map(lambda x:ord(x)-ord('a'), s))
        L_s1 = str2list(s1)
        L_s2 = str2list(s2)
        L_base = str2list(baseStr)
        
        par=dsu(26)
        for i in range(len(L_s1)):
            par.union(L_s1[i], L_s2[i])
        for i in range(len(L_base)):
            L_base[i] = par.find(L_base[i])
            
        def list2str(L):
            return ''.join(list(map(lambda x:chr(x+ord('a')), L)))
        
        return list2str(L_base)