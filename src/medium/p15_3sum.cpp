#include <vector>
#include <map>
#include <iostream>

// TODO : figure out how to compile code with the best optimization
// TODO : Better to initialize the result when constructing.
// TODO : How to proper overload operators inside a class
// TODO : look at the compile code and comparing on different compilers (make it clang-tidy)
// TODO : How to make some class headers that other file can link to
// TODO : How to make virtual functions so other file can rewrite it


std::ostream &operator<<(std::ostream& os, const std::vector<int>& v){
    os << v[0] << v[1] << v[2] << '\n';
	return os;
}

class Solution{
public:
        std::vector<int> threeSum(std::vector<int>& nums, int target){
		    std::map<int, int> m;
			return {1,2,3};
		}
};


int main(){
  std::vector<int> nums = {1,2,3,7,8};
  int target = 11;
  Solution s;
  std::cout << s.threeSum(nums, target);
}


