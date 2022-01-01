class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []
        leftmaxi = 0
        rightmaxi = 0
        res = 0
        for i in height:
            leftmaxi = max(leftmaxi, i)
            left.append(leftmaxi)
        for i in height[::-1]:
            rightmaxi = max(rightmaxi, i)
            right.insert(0, rightmaxi)
        for i in range(len(height)):
            res += max(0 , min(left[i], right[i]) - height[i])
        return res