# def triangularSum(self, nums: List[int]) -> int:
#     n = len(nums)
#     for i in range(n, 0, -1):
#         for j in range(i-1):
#             nums[j] = (nums[j] + nums[j+1])  % 10
#     return nums[0]

def triangularSum(nums):
    res, nCr, n = 0, 1, len(nums) - 1
    for r, num in enumerate(nums):
        res = (res + num  * nCr) % 10
        nCr = nCr * (n - r) // (r + 1)
    return res


nums = [1,2,3,4,5]
print(triangularSum(nums))