class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        int n=piles.size();
        int e=0;
        while(n>0){
            n/=2;
            e+=1;
        }
        int E=1;
        for(int i=0;i<e;i++){
            E*=2;
        }
        vector<int> segtree(2*E, 0);
        long long tot=0;
        for(int i=0;i<piles.size();i++){
            segtree[E+i]=piles[i];
            tot+=piles[i];
        }
        for(int i=E-1;i>0;i--){
            segtree[i]=max(segtree[2*i],segtree[2*i+1]);
        }
        while(k>0){
            k--;
            int pos=1; 
            while(pos<E){
                if(segtree[pos]==segtree[2*pos]){
                    pos*=2;
                }
                else{
                    pos=2*pos+1;
                }
            }
            // cout << pos-E << ' ' << segtree[pos] << endl;
            tot-=segtree[pos]/2;
            segtree[pos]-=segtree[pos]/2;
            while(pos>1){
                pos/=2;
                segtree[pos]=max(segtree[2*pos], segtree[2*pos+1]);
            }
        }
        return tot;
    }
};