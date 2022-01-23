class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # Approach 2 : Math solves, not yet understand....
        
        # Approach 1: from https://leetcode.com/problems/super-egg-drop/discuss/158974/C%2B%2BJavaPython-2D-and-1D-DP-O(KlogN)
        dp = [[0] * (k+1) for _ in range(n+1)]
        for m in range(1, n+1):
            for j in range(1, k+1):
                dp[m][j] = dp[m-1][j-1] + dp[m-1][j] + 1
                if dp[m][j] >= n:
                    return m