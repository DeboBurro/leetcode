class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Approach 2: in a while loop
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                leftStr = s[l+1:r+1]
                rightStr = s[l:r]
                return leftStr == leftStr[::-1] or rightStr == rightStr[::-1]
            l += 1
            r -= 1
        return True
    
    
    # Approach 1 : recursive
#     def validPalindrome(self, s: str) -> bool:
#         l = 0
#         r = len(s)-1
#         return self.helper(s, l, r, 1)

#     def helper(self, s, l, r, n):
#         # print(s, l, r)
#         if l < r:
#             if s[l] == s[r]:
#                 return self.helper(s, l+1, r-1, n)
#             else:
#                 if n == 0:
#                     return False
#                 else:
#                     n -= 1
#                     return self.helper(s, l+1, r, n) or self.helper(s, l, r-1, n)
#         return True
