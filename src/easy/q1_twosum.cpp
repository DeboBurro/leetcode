#include <vector>
#include <map>
#include <iostream>

std::ostream &operator<<(std::ostream& os, const std::vector<int>& v){
    os << '['  << v[0] << ',' << v[1] <<  ']' << '\n';
    return os;
}



class Solution {
public:
	std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::map<int, int> m;
        for(int i = 0; i < nums.size() ; i++){
            if(m.find(target - nums[i]) != m.end()  )   {
                return {m[target - nums[i]], i};
            }else{
                m[nums[i]] = i;
            }
        }
        return {-1, -1};
    }
};

int main(){
    std::vector<int> nums = {2,7,11,15};
    int target = 9;
	Solution s;
    std::cout << s.twoSum(nums, target);
}
