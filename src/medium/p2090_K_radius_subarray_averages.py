class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Approach 2 : prefix Sum
        n = len(nums)
        prefixSum = [0]
        for i in range(n):
            prefixSum.append(prefixSum[-1] + nums[i])
        res = [-1] * n
        for i in range(k, n-k):
            res[i] = ((prefixSum[i+k+1] - prefixSum[i-k]) // (2*k +1))
        return res

        # Approach 1 : sliding window
        # n = len(nums)
        # if n < 2 * k + 1: return [-1] * n
        # summa = sum(nums[:2*k+1])
        # res = [summa]
        # for i in range(k+1, n-k):
        #     res.append(res[-1] + nums[i+k] - nums[i-k-1])
        # for idx, val in enumerate(res):
        #     res[idx] = val // (2*k+1)
        # res = [-1] * k + res + [-1] * k
        # return res