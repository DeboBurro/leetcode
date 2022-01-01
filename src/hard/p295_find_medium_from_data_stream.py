class MedianFinder:

    def __init__(self):
        self.middle = None
        self.arr = []

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
        else:
            ind = self.binary_insert(num, 0, len(self.arr)-1)
            self.arr.insert(ind, num)

    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2:
            return self.arr[n // 2]
        else:
            return (self.arr[n//2] + self.arr[n//2 -1]) /2
    
    def binary_insert(self, val, start, end):
        if start == end:
            if self.arr[start] > val:
                return start
            return start + 1
        if start > end:
            return start
        mid = (start + end) // 2
        if self.arr[mid] < val:
            return self.binary_insert(val, mid + 1, end)
        elif self.arr[mid] > val:
            return self.binary_insert(val, start, mid - 1)
        else:
            return mid

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()