class Solution {
public:
    int climbStairs(int n) {
        if(n==1){
            return n;
        }
        else if(n==2){
            return n;
        }
        else{
            int cnt=2;
            int p1=1, p2=2;
            while(cnt<n){
                p2+=p1;
                p1=p2-p1;
                cnt+=1;
            }
            return p2;
        }
    }
};