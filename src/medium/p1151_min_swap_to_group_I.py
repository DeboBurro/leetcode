class Solution:
    def minSwaps(self, data: List[int]) -> int:
        windowSize = sum(data)
        if windowSize < 2 : return 0
        zeroCounter = [0]
        for i in data:
            if i == 0:
                zeroCounter.append(zeroCounter[-1] + 1)
            else:
                zeroCounter.append(zeroCounter[-1])
        mini = windowSize
        for right in range(0 + windowSize, len(zeroCounter)):
            mini = min(mini, zeroCounter[right] - zeroCounter[right-windowSize])
        return mini
