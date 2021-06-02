# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_recursive(self, curr, prev):
        next_node = curr.next
        curr.next = prev
        if not next_node:
            return curr
        return self.reverse_recursive(next_node, curr)

    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        next_node = head.next
        head.next = None

        if next_node:
            return self.reverse_recursive(next_node, head)
        return head
