# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        s = ''
        current = head
        while current:
            s += str(current.val)
            current = current.next

        res = int(s, 2)
        return res