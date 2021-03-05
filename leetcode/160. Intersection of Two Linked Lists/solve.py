# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currentheadB = headB

        visited = {}
        while(headA):           
            visited[headA] = True
            headA = headA.next

        while(headB):
            if(headB in visited):
                return headB
            headB = headB.next

        return None