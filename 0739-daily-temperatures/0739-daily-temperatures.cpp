class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> hotter(n,0);
        vector<vector<int> > stack; 
        stack.push_back({temperatures[0], 0});
        for(int i=1; i<n; i++){
            int temp = temperatures[i]; 
            while(stack.size()){
                vector<int> prev=stack.back(); 
                if(prev[0]<temp){
                    hotter[prev[1]] = i - prev[1]; 
                    stack.pop_back(); 
                }
                else{
                    break;
                }
            }
            stack.push_back({temp, i});
        }
        return hotter; 
    }
};