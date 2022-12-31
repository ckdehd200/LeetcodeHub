class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int CONST = 1000000007;
        int n = tasks.size();
        int E = 1;
        while(E<n){
            E*=2;
        }
        vector<vector<int> > st_enq(2*E, vector<int>(2,CONST));
        for(int i=0;i<n;i++){
            st_enq[E+i]=tasks[i];
        }
        for(int i=E-1;i>0;i--){
            if(st_enq[2*i][0] < st_enq[2*i+1][0]){
                st_enq[i]=st_enq[2*i];
            }
            else{
                st_enq[i]=st_enq[2*i+1];
            }
        }
        vector<vector<int> > st_proc(2*E, vector<int>(2,CONST));
        vector<int> ans;
        long long pos_time = 0;
        while(ans.size()<n){
            if(pos_time<st_enq[1][0] && pos_time<st_proc[1][0]){
                pos_time = st_enq[1][0];
            }
            while(pos_time>=st_enq[1][0] && st_enq[1][0]!=CONST){
                int pos=1;
                while(pos<E){
                    if(st_enq[2*pos]==st_enq[pos]){
                        pos*=2;
                    }
                    else{
                        pos=2*pos+1;
                    }
                }
                st_proc[pos]=st_enq[1]; 
                st_enq[pos]={CONST,CONST};
                while(pos>1){
                    pos/=2;
                    if(st_proc[2*pos][1]<=st_proc[2*pos+1][1]){
                        st_proc[pos]=st_proc[2*pos];
                    }
                    else{
                        st_proc[pos]=st_proc[2*pos+1];
                    }
                    
                    if(st_enq[2*pos][0]<st_enq[2*pos+1][0]){
                        st_enq[pos]=st_enq[2*pos];
                    }
                    else{
                        st_enq[pos]=st_enq[2*pos+1];
                    }
                }
            }
            
            pos_time+=st_proc[1][1];
            int pos=1;
            while(pos<E){
                if(st_proc[2*pos]==st_proc[pos]){
                    pos*=2;
                }
                else{
                    pos=2*pos+1;
                }
            }
            st_proc[pos]={CONST,CONST};
            ans.push_back(pos-E);
            while(pos>1){
                pos/=2;
                if(st_proc[2*pos][1]<=st_proc[2*pos+1][1]){
                    st_proc[pos]=st_proc[2*pos];
                }
                else{
                    st_proc[pos]=st_proc[2*pos+1];
                }
            }
        }
        return ans;
    }
};