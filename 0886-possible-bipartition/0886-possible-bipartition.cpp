class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        unordered_map<int, vector<int> > group; 
        for(int j=0; j<dislikes.size();j++){
            int a=dislikes[j][0]; 
            int b=dislikes[j][1]; 
            group[a].push_back(b);
            group[b].push_back(a);
        }
        
        vector<int> used(n+1, 0);
        for(int i=1;i<n+1;i++){
            vector<vector<int> > stack; 
            stack.push_back({i,1});
            while(stack.size() > 0){
                vector<int> v = stack.back(); 
                int c=v[0], gr=v[1]; 
                stack.pop_back();
                if(used[c]>0){
                    continue;
                }
                // cout << c << " first " << gr << endl;
                used[c]=gr; 
                for(int j=0;j<group[c].size();j++){
                    int child = group[c][j];
                    if(used[child]==gr){
                        return false;
                    }
                    stack.push_back({child, 3-gr});
                }
            }
        }
        return true;
    }
};