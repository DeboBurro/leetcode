# class Solution {
#     public long subArrayRanges(int[] nums) {
#         long result = 0;
#         Stack<Integer> inc = new Stack<>();
#         Stack<Integer> dec = new Stack<>();
#         for(int i = 0 ; i <= nums.length ; i ++){
#             while(!inc.isEmpty() && ( i == nums.length || nums[inc.peek()] < nums[i])){
#                 int currIndex = inc.pop();
#                 int leftBound = inc.isEmpty() ? -1 : inc.peek(); 
#                 int rightBound = i;
#                 result += (currIndex - leftBound) * (rightBound - currIndex) * (long) nums[currIndex];                
#             }
#             while(!dec.isEmpty() && (i == nums.length || nums[dec.peek()] > nums[i])){
#                 int currIndex = dec.pop();
#                 int leftBound = dec.isEmpty()? -1 : dec.peek(); 
#                 int rightBound = i;
#                 result -= (currIndex - leftBound) * (rightBound - currIndex) * (long) nums[currIndex];
#             }
#             inc.push(i);
#             dec.push(i);
#         }
        
#         return result;
#     }
# }


# like leetcode 2104: https://leetcode.com/problems/sum-of-subarray-ranges/
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        inc_stack = []
        dec_stack = []
        for i in range(len(nums)+1):
            while inc_stack and  ( i == len(nums) or nums[inc_stack[-1]] < nums[i]):
                mid_idx  = inc_stack.pop()
                left_bound_idx = -1 if not inc_stack else inc_stack[-1]
                right_bound_idx = i
                result += (mid_idx - left_bound_idx) * (right_bound_idx - mid_idx) * nums[mid_idx]
            while dec_stack and  ( i == len(nums) or nums[dec_stack[-1]] > nums[i]):
                mid_idx = dec_stack.pop()
                left_bound_idx = -1 if not dec_stack else dec_stack[-1]
                right_bound_idx = i
                result -= (mid_idx - left_bound_idx) *(right_bound_idx - mid_idx) * nums[mid_idx]
            inc_stack.append(i)
            dec_stack.append(i)
            # print(inc_stack, dec_stack, result)
        return result