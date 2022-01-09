"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        l1 = p
        l2 = q
        while p != q:
            if p.parent:
                p = p.parent
            else:
                p = l2
            if q.parent:
                q = q.parent
            else:
                q = l1
        return p