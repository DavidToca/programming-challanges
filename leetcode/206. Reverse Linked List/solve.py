# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        prev_node = head
        next_node = head.next
        prev_node.next = None

        while next_node:
            head = next_node
            next_node = head.next
            head.next = prev_node
            prev_node = head

        return head
