# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if head.next == head: return head
        if not head.next: return None
        ptr_1 = head
        ptr_2 = head
        while ptr_1 and ptr_2 and ptr_2.next:
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next.next
            # print("slow : ", ptr_1.val, "fast : ", ptr_2.val)
            if ptr_1 == ptr_2:
                break
        if ptr_1 == ptr_2:
            while ptr_1 != head:
                ptr_1 = ptr_1.next
                head = head.next
            return ptr_1
        return None