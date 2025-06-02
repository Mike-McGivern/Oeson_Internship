# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current != None:
            stack.append(current)
            current = current.next
        
        if not stack:
            return None
        
        newHead = stack.pop()
        current = newHead
        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None
        return newHead
