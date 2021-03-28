# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        if not head.next:
            return False

        current = head

        visited = {}

        while current:
            if current in visited:
                return True
            visited[current] = True
            current = current.next
        return False