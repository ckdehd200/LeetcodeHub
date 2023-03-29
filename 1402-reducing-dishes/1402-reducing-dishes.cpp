using namespace std;

class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end(), greater<int>());
        long long int s=0, ans=0, pointer=0;
        while(pointer<satisfaction.size() && s+satisfaction[pointer]>0){
            s+=satisfaction[pointer];
            ans+=s;
            pointer++; 
        }
        return ans;
    }
};