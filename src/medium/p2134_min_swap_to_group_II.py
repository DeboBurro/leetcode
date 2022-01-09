class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Approach 2 : Count minimum of zeros we have in the sliding window (in-place metohd)
        windowSize = sum(nums)
        nums = nums + nums
        if windowSize < 2 : return 0
        res = windowSize
        x = 0
        for i in range(len(nums)):
            if i >= windowSize and nums[i - windowSize] == 0:
                x -= 1
            if nums[i] == 0:
                x += 1
            if i >= windowSize:
                res = min(res, x)
        return res
        
        
        ''' Approach 1 : Count minimum of zeros we have in the sliding window (by prefixSum)
        windowSize = sum(nums)
        nums = nums + nums
        if windowSize < 2 : return 0
        zeroPrefixSum = [0]
        for i in nums:
            if i == 0:
                zeroPrefixSum.append(zeroPrefixSum[-1] + 1)
            else:
                zeroPrefixSum.append(zeroPrefixSum[-1])
        mini = windowSize
        for right in range(0 + windowSize, len(zeroPrefixSum)):
            mini = min(mini, zeroPrefixSum[right] - zeroPrefixSum[right-windowSize])
        return mini
        '''