class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Solution 2: more understandable
        res = []
        if not matrix or not matrix[0]: return res
        n = len(matrix)
        m = len(matrix[0])
        up, down, left, right = 0, n-1, 0, m-1
        while len(res) < n * m:
            for j in range(left, right + 1):
                if len(res) < n * m:
                    res.append(matrix[up][j])
            up += 1
            for i in range(up, down + 1):
                if len(res) < n * m:
                    res.append(matrix[i][right])
            right -= 1
            for j in range(right, left-1, -1):
                if len(res) < n * m:
                    res.append(matrix[down][j])
            down -= 1
            for i in range(down, up-1, -1):
                if len(res) < n * m:
                    res.append(matrix[i][left])
            left +=1
        return res
            
        # Solution 1 : a solution from alien
        # res = []
        # while matrix:
        #     res.extend(matrix.pop(0))
        #     matrix = [*zip(*matrix)][::-1]
        # return res
