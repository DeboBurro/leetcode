# First solution: O(NlogN) time complexity
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        arr = sorted(intervals, key = lambda x : x[0])
        res = [arr[0]]
        for inter in arr[1:]:
            if inter[0] <= res[-1][1]:
                res[-1][1] = max(inter[1], res[-1][1])
            else:
                res.append(inter)
        return res