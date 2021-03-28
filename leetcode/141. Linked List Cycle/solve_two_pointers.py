# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        pointer1 = head
        pointer2 = head

        while pointer1.next != None and pointer2.next != None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

            if not pointer2.next:
                return False

            pointer2 = pointer2.next

            if pointer1 == pointer2:
                return True
        return False