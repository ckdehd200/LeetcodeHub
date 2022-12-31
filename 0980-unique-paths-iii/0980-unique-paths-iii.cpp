class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        int m=grid.size(), n=grid[0].size();
        int tot=m*n, plen=0;
        int start, end;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]!=-1){
                    plen++;
                }
                if(grid[i][j]==1){
                    start=i*n+j;
                }
                if(grid[i][j]==2){
                    end=i*n+j;
                }
            }
        }
        
        int ans = 0;
        deque<pair<vector<int>, int> > dq; 
        vector<int> init(tot, 0);
        dq.push_back({init, start});
        while(dq.size()>0){
            auto [visited, pos] = dq.front();
            dq.pop_front();
            visited[pos] = 1;
            if(pos==end){
                if(accumulate(visited.begin(), visited.end(), 0)==plen){
                    ans++;
                }
                continue;
            }
            int x=pos/n, y=pos%n;
            if(grid[x][y]==-1){
                continue;
            }
            
            if(pos+1<tot && (pos%n)!=n-1 && visited[pos+1]==0){
                dq.push_back({visited, pos+1});
            }
            if(pos-1>=0 && (pos%n)!=0 && visited[pos-1]==0){
                dq.push_back({visited, pos-1});
            }
            if(pos+n<tot && visited[pos+n]==0){
                dq.push_back({visited, pos+n});
            }
            if(pos-n>=0 && visited[pos-n]==0){
                dq.push_back({visited, pos-n});
            }
        }
        return ans;
    }
};