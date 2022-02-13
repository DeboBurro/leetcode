#include <map>
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::map<int, int> m;
        for(auto i: nums){
            auto it = m.find(i);
            if(it == m.end()){
                m[i] = 1;
            }else{
                it->second += 1;
            }
        };
        auto it = m.begin();
        while(true){
            if(2*it->second >= nums.size()){
                return it->first;
            }
            *it++;
        }
        return 0;
    }
};
