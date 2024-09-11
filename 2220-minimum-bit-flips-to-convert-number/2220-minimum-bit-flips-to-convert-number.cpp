class Solution {
public:
    int minBitFlips(int start, int goal) {
        int bits = start^goal;
        int ans=0;
        while (bits>0) {bits &= bits-1; ans+=1;}
        return ans;
    }
};