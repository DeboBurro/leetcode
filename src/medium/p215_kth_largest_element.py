
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # solution 2 : Quick select , O(2n)
        # Time complexity : 
        # n + n/2 + n*/4 + .... + n* (1/2^m)
        # = n * (1 - (1/2)^m) / (1 - 1/2)
        # = n * (1 - 0) / ( 1/2 )
        # = 2n
        if not nums:
            return
        pivot = random.choice(nums)
        gt = [val for val in nums if val > pivot]
        eq = [val for val in nums if val == pivot]
        lt = [val for val in nums if val < pivot]
        if k <= len(gt):
            return self.findKthLargest(gt, k)
        elif k > len(gt) + len(eq):
            return self.findKthLargest(lt, k - len(gt) - len(eq))
        else:
            return eq[0]
        
        # sol 1 : heapq , O(n log n)
        # nums = [-1 * i for i in nums]
        # heapq.heapify(nums)
        # for _ in range(k):
        #     val = heapq.heappop(nums)
        # return -1 * val